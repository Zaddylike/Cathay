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
    PERMISSION_SCOPE_CODE,
    PERMISSION_SSO_APPLICATION_NAME,
    PROJECT_ABBR_PREFIX,
    PROJECT_DESCRIPTION_PREFIX,
    PROJECT_EN_NAME_PREFIX,
    PROJECT_ZH_NAME_PREFIX,
)
from utils.data_mode import DATA_MODES, KEEP, permission_project_lock, should_cleanup
from utils.permission_baseline import (
    ensure_permission_initialization,
    ensure_shared_project,
    ensure_sso_application,
)
from utils.resource_cleanup import CleanupRegistry



# All type of page object

# 用途: 建立尚未登入的 OmniApp Page Object。
@pytest.fixture
def app(page: Page):
    try:
        return OmniApp(page)
    except Exception as error:
        raise Exception(f"Failed to initialize OmniApp: {error}")

# 用途: 建立並完成帳號登入的 OmniApp Page Object。
@pytest.fixture
def logged_app(page: Page, thread_account):
    try:
        omni_app = OmniApp(page)
        omni_app.login_by_account(thread_account["username"], thread_account["password"])
        return omni_app
    except Exception as error:
        raise Exception(f"Failed to log in: {error}")

# 用途: 保存 Permission 測試使用的 App 與 Project 識別資料。
@dataclass(frozen=True)
class PermissionProjectContext:
    app: OmniApp
    abbreviation: str

# 用途: 建立 Permission 測試專案 Context，並在 isolated 模式結束時刪除專案。
@pytest.fixture
def permission_project_context(
    logged_app: OmniApp,
    data_mode: str,
) -> Iterator[PermissionProjectContext]:
    if data_mode == KEEP:
        with permission_project_lock():
            ensure_shared_project(logged_app, create_missing=True)
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

        yield context

    finally:
        if should_cleanup(data_mode):
            try:
                if project_abbreviation == PERMISSION_PROJECT_ABBR:
                    raise AssertionError("Isolated Permission cleanup received the baseline project")

                logged_app.operate_page.reset_to_anchor(BASE_URL_DEV)

                if logged_app.project_page.project_exists(project_abbreviation):
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

# 用途: 完成 Permission Init 並保留 Project Context，結束時清理基準 Scope。
@pytest.fixture
def permission_initialized_context(
    permission_project_context: PermissionProjectContext,
    data_mode: str,
) -> Iterator[PermissionProjectContext]:
    context = permission_project_context
    app = context.app

    def prepare_permission_initialization() -> None:
        app.operate_page.go_to_permission_page(context.abbreviation)
        ensure_permission_initialization(app, create_missing=True)

    try:
        if data_mode == KEEP:
            with permission_project_lock():
                prepare_permission_initialization()
        else:
            prepare_permission_initialization()

        yield context
    finally:
        if should_cleanup(data_mode):
            app.operate_page.reset_to_anchor(BASE_URL_DEV)
            if app.project_page.project_exists(context.abbreviation):
                app.operate_page.go_to_permission_page(context.abbreviation)
                if not app.application_permission_page.permission_initialization_available():
                    app.operate_page.open_to_permissions_page()
                    app.scope_page.delete_scope_if_exists(PERMISSION_SCOPE_CODE)


# 用途: 提供已完成 Permission Init 且位於權限設定頁的 OmniApp。
@pytest.fixture
def permission_settings_app(
    permission_initialized_context: PermissionProjectContext,
) -> OmniApp:
    context = permission_initialized_context
    context.app.operate_page.go_to_permission_page(context.abbreviation)
    context.app.operate_page.open_to_permissions_page()
    return context.app


# 用途: 建立 SSO 前置並保留 Project Context，結束時清理基準 SSO。
@pytest.fixture
def permission_sso_context(
    permission_initialized_context: PermissionProjectContext,
    data_mode: str,
) -> Iterator[PermissionProjectContext]:
    context = permission_initialized_context
    app = context.app

    def prepare_sso() -> None:
        app.operate_page.go_to_permission_page(context.abbreviation)
        ensure_sso_application(app, create_missing=True)

    try:
        if data_mode == KEEP:
            with permission_project_lock():
                prepare_sso()
        else:
            prepare_sso()

        yield context
    finally:
        if should_cleanup(data_mode):
            app.operate_page.reset_to_anchor(BASE_URL_DEV)
            if app.project_page.project_exists(context.abbreviation):
                app.operate_page.go_to_permission_page(context.abbreviation)
                app.single_sign_on_page.delete_application_if_exists(
                    PERMISSION_SSO_APPLICATION_NAME
                )


# 用途: 提供已完成 Permission Init、SSO 前置且位於權限設定頁的 OmniApp。
@pytest.fixture
def permission_sso_app(
    permission_sso_context: PermissionProjectContext,
) -> OmniApp:
    context = permission_sso_context
    context.app.operate_page.go_to_permission_page(context.abbreviation)
    context.app.operate_page.open_to_permissions_page()
    return context.app



# Clean testing data

# 用途: 集中登記測試資料 cleanup，並在 teardown 時反向執行。
@pytest.fixture
def cleanup_registry(data_mode: str) -> Iterator[CleanupRegistry]:
    registry = CleanupRegistry(enabled=should_cleanup(data_mode))

    yield registry
    
    registry.cleanup()


# 用途: 提供 Project cleanup 登記函式。
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



# Browser settings

# 用途: 統一設定瀏覽器啟動參數。
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

# 用途: 統一設定瀏覽器 Context 語系。
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "java_script_enabled": True,
        "locale": "zh-TW",
        "extra_http_headers": {
            **browser_context_args.get("extra_http_headers", {}),
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        },
    }

# 用途: 建立 Browser Context，並在測試結束後關閉 Context 與附加錄影。
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

# Parameters

def pytest_addoption(parser):
    parser.addoption(
        "--data-mode",
        action="store",
        choices=DATA_MODES,
        default="isolated",
        help="Test data lifecycle: isolated deletes fixture data; keep retains it",
    )

# 用途: 提供測試資料保留或隔離模式。
@pytest.fixture(scope="session")
def data_mode(pytestconfig) -> str:
    return pytestconfig.getoption("--data-mode")



# threads

# 用途: 依 pytest worker 分配登入帳號。
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
