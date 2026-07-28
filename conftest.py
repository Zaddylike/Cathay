from collections.abc import Iterator
from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest
from playwright.sync_api import BrowserContext, Error as PlaywrightError, Page

from app.omni_app import OmniApp
from config.settings import (
    ACCOUNT_PASSWORD,
    ACCOUNT_USERNAME,
    ACCOUNT_USERNAME_2,
    ACCOUNT_PASSWORD_2,
    ACCOUNT_USERNAME_3,
    ACCOUNT_PASSWORD_3,
    BASE_URL_DEV,
    BROWSER_ARGS,
    HEADLESS,
    DELAY_TIME,
    PERMISSION_PROJECT_ABBR,
    PERMISSION_S2S_APPLICATION_NAME,
    PERMISSION_SCOPE_CODE,
    PERMISSION_SSO_APPLICATION_NAME,
    PROJECT_ABBR_PREFIX,
    PROJECT_DESCRIPTION_PREFIX,
    PROJECT_EN_NAME_PREFIX,
    PROJECT_ZH_NAME_PREFIX,
)
from utils.data_mode import DATA_MODES, KEEP, permission_project_lock, should_cleanup
from utils.permission_baseline import (
    create_permission_initialization,
    ensure_permission_baseline,
    ensure_sso_application,
)
from utils.resource_cleanup import CleanupRegistry



# Browser settings

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": browser_type_launch_args.get("headless", HEADLESS),
        "slow_mo": DELAY_TIME,
        "args": [
            *browser_type_launch_args.get("args", []),
            *BROWSER_ARGS,
        ],
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "java_script_enabled": True,
        "locale": "zh-TW",
        "no_viewport": True,
        "extra_http_headers": {
            **browser_context_args.get("extra_http_headers", {}),
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        },
    }

@pytest.fixture
def context(new_context) -> Iterator[BrowserContext]:
    browser_context = new_context()
    recorded_pages: list[Page] = []
    browser_context.on("page", lambda created_page: recorded_pages.append(created_page))

    yield browser_context

    browser_context.close()

    for index, recorded_page in enumerate(recorded_pages, start=1):
        try:
            video = recorded_page.video
            if video is None:
                continue

            allure.attach.file(
                video.path(),
                name=f"Playwright video {index}",
                attachment_type=allure.attachment_type.WEBM,
            )
        except PlaywrightError:
            continue

@pytest.fixture
def page(page: Page, browser_name: str, browser_type_launch_args):
    is_headless = browser_type_launch_args.get("headless", True)

    if browser_name == "chromium" and not is_headless:
        cdp_session = page.context.new_cdp_session(page)
        try:
            window = cdp_session.send("Browser.getWindowForTarget")
            cdp_session.send(
                "Browser.setWindowBounds",
                {
                    "windowId": window["windowId"],
                    "bounds": {"windowState": "maximized"},
                },
            )
        finally:
            cdp_session.detach()

    return page



# Parameters

def pytest_addoption(parser):
    parser.addoption(
        "--data-mode",
        action="store",
        choices=DATA_MODES,
        default="isolated",
        help="Test data lifecycle: isolated deletes fixture data; keep retains it",
    )

@pytest.fixture(scope="session")
def data_mode(pytestconfig) -> str:
    return pytestconfig.getoption("--data-mode")



# threading accounts

@pytest.fixture
def thread_account(worker_id):
    ACCOUNTS_Rollbook = [
        {
            "username": ACCOUNT_USERNAME,
            "password": ACCOUNT_PASSWORD,
        },
        {
            "username": ACCOUNT_USERNAME_2,
            "password": ACCOUNT_PASSWORD_2,
        },
        {
            "username": ACCOUNT_USERNAME_3,
            "password": ACCOUNT_PASSWORD_3,
        },
    ]

    if worker_id == "master":
        return ACCOUNTS_Rollbook[0]
    worker_index = int(worker_id.replace("gw", ""))
    if worker_index >= len(ACCOUNTS_Rollbook):
        pytest.exit(
            f"Thread數量超過可用帳號數量："
            f"{worker_index + 1} Workers / {len(ACCOUNTS_Rollbook)} Accounts"
        )
        
    return ACCOUNTS_Rollbook[worker_index]



# All type of page object

# 用途: 建立 Basic Object。
@pytest.fixture
def app(page: Page):
    try:
        return OmniApp(page)
    except Exception as error:
        raise Exception(f"Failed to initialize OmniApp: {error}")

# 用途: 建立 Basic Object後運行前置登入。
@pytest.fixture
def logged_app(page: Page, thread_account):
    try:
        omni_app = OmniApp(page)
        omni_app.login_by_account(thread_account["username"], thread_account["password"])
        return omni_app
    except Exception as error:
        raise Exception(f"Failed to log in: {error}")

# 用途: Lock Permission 測試使用的 App 與 Project 識別資料。
@dataclass(frozen=True)
class PermissionProjectContext:
    app: OmniApp
    abbreviation: str

# 用途: 建立 lodded_app object後, 建立測試Permission需要的project。
@pytest.fixture
def permission_project(logged_app: OmniApp, data_mode: str) -> Iterator["PermissionProjectContext"]:

    if data_mode == KEEP:
        with permission_project_lock():
            ensure_permission_baseline(logged_app, create_missing=True)
        yield PermissionProjectContext(
            app=logged_app,
            abbreviation=PERMISSION_PROJECT_ABBR,
        )
        return

    suffix = uuid4().hex[:4]
    project_abbreviation = f"{PROJECT_ABBR_PREFIX}-permission-{suffix}"
    context = PermissionProjectContext(
        app=logged_app,
        abbreviation=project_abbreviation,
    )

    try:
        logged_app.project_page.create_project(
            project_abbreviation,
            f"{PROJECT_ZH_NAME_PREFIX}-permission-{suffix}",
            f"{PROJECT_EN_NAME_PREFIX}-permission-{suffix}",
            f"{PROJECT_DESCRIPTION_PREFIX}-permission-{suffix}",
        )

        logged_app.operate_page.go_to_permission_page(project_abbreviation)
        create_permission_initialization(logged_app)

        yield context

    finally:
        if should_cleanup(data_mode):
            try:
                if project_abbreviation == PERMISSION_PROJECT_ABBR:
                    raise AssertionError("Isolated Permission cleanup received the baseline project")

                logged_app.operate_page.reset_to_anchor(BASE_URL_DEV)

                if logged_app.project_page.project_exists(project_abbreviation):
                    logged_app.operate_page.go_to_permission_page(project_abbreviation)
                    logged_app.single_sign_on_page.delete_application_if_exists(
                        PERMISSION_SSO_APPLICATION_NAME
                    )
                    logged_app.server_to_server_page.delete_application_if_exists(
                        PERMISSION_S2S_APPLICATION_NAME
                    )
                    if not logged_app.application_permission_page.permission_initialization_available():
                        logged_app.scope_page.delete_scope_if_exists(PERMISSION_SCOPE_CODE)


                    logged_app.operate_page.reset_to_anchor(BASE_URL_DEV)
                    logged_app.project_page.delete_project_if_exists(project_abbreviation)
            except Exception as error:
                allure.attach(
                    str(error),
                    name=f"Permission project cleanup failed: {project_abbreviation}",
                    attachment_type=allure.attachment_type.TEXT,
                )
                raise AssertionError(
                    f"Permission isolated cleanup failed for {project_abbreviation}: {error}"
                ) from error

# 用途: 建立lodded_app Object後, 建立測試Permission需要的Project。
@pytest.fixture
def permission_settings_app(
    permission_project: PermissionProjectContext,
) -> OmniApp:
    """開啟目前測試專案的權限設定頁。"""
    permission_project.app.operate_page.open_to_permissions_page()
    return permission_project.app

"""
用途: 
1. 建立lodded_app Object後, 建立測試Permission需要的Project。
2. 補齊 Group 與 Assign Permission 共用的 SSO 前置資料。
"""
@pytest.fixture
def permission_project_with_sso(
    permission_project: PermissionProjectContext,
    data_mode: str,
) -> PermissionProjectContext:

    def prepare_sso() -> None:
        ensure_sso_application(permission_project.app, create_missing=True)

    if data_mode == KEEP:
        with permission_project_lock():
            prepare_sso()
    else:
        prepare_sso()

    return permission_project

# 用途: 建立lodded_app Object後, 建立測試Permission需要的Project。
@pytest.fixture
def permission_settings_sso_app(
    permission_project_with_sso: PermissionProjectContext,
) -> OmniApp:
    """完成 SSO 前置後開啟權限設定頁。"""
    permission_project_with_sso.app.operate_page.open_to_permissions_page()
    return permission_project_with_sso.app



# clean

@pytest.fixture
def cleanup_registry(data_mode: str) -> Iterator[CleanupRegistry]:
    registry = CleanupRegistry(enabled=should_cleanup(data_mode))

    yield registry
    
    registry.cleanup()


@pytest.fixture
def project_cleanup(logged_app: OmniApp, cleanup_registry: CleanupRegistry):
    def delete_project(project_abbreviation: str) -> None:
        logged_app.page.keyboard.press("Escape")
        logged_app.page.goto(BASE_URL_DEV)
        logged_app.project_page.delete_project_if_exists(project_abbreviation)

    def register(project_abbreviation: str) -> None:
        def cleanup() -> None:
            delete_project(project_abbreviation)

        cleanup_registry.register(
            "Project",
            project_abbreviation,
            cleanup,
        )

    return register