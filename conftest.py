from collections.abc import Iterator
from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest
from playwright.sync_api import Page

from app.omni_app import OmniApp
from config.settings import (
    ACCOUNT_PASSWORD,
    ACCOUNT_USERNAME,
    BASE_URL_DEV,
    BROWSER_ARGS,
    HEADLESS,
    DELAY_TIME,
    PERMISSION_PROJECT_ABBR,
    PERMISSION_ROLE_CODE,
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
    ensure_permission_project_member,
    ensure_sso_application,
)


"""
用途:集中管理專案自訂的 pytest CLI 參數。

執行流程:
    1. --data-mode 控制測試資料是否於 teardown 清除。
"""
def pytest_addoption(parser):
    parser.addoption(
        "--data-mode",
        action="store",
        choices=DATA_MODES,
        default="isolated",
        help="Test data lifecycle: isolated deletes fixture data; keep retains it",
    )

"""
用途:將 --data-mode 轉成其他 fixtures 可以注入使用的字串。

執行流程:
    1. pytest 解析 CLI。
    2. 未傳入時回傳 isolated。
    3. 傳入 --data-mode=keep 時回傳 keep。
"""
@pytest.fixture(scope="session")
def data_mode(pytestconfig) -> str:
    return pytestconfig.getoption("--data-mode")


@pytest.fixture
def app(page: Page):
    try:
        return OmniApp(page)
    except Exception as error:
        raise Exception(f"Failed to initialize OmniApp: {error}")


@pytest.fixture
def logged_app(page: Page):
    try:
        omni_app = OmniApp(page)
        omni_app.login_by_account(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
        return omni_app
    except Exception as error:
        raise Exception(f"Failed to log in: {error}")


"""
運行順序:
    1. 建立 Page object -> logged_app。
    2. 分流測試模式:[ isolated、keep ]。
    3.1.keep:
        1. 進入跨程序鎖。
        2. 檢查固定 project-abbr-main 與 Permission Init,有缺就補。
        3. 測試結束後保留資料。
    3.2.isolated:
        1. 建立本次測試專屬 UUID Project。
        2. 在 UUID Project 建立最小 Permission Init。
        3. yield 將 Project context 交給下游 fixture 與測試。
        4. 測試結束後先刪除 Application,再刪除 UUID Project。

平行運行:
    1. isolated 每個測試使用不同 UUID Project,不共用測試資料。
    2. keep 透過跨程序鎖補建固定 baseline,避免多個 worker 同時建立。
"""
@pytest.fixture
def permission_project(logged_app: OmniApp,data_mode: str) -> Iterator["PermissionProjectContext"]:
    if data_mode == KEEP:
        with permission_project_lock():
            ensure_permission_baseline(logged_app, create_missing=True)
        yield PermissionProjectContext(
            app=logged_app,
            abbreviation=PERMISSION_PROJECT_ABBR,
        )
        return

    suffix = uuid4().hex[:8]
    project_abbreviation = f"{PROJECT_ABBR_PREFIX}permission-{suffix}"
    context = PermissionProjectContext(
        app=logged_app,
        abbreviation=project_abbreviation,
    )

    try:
        logged_app.page.goto(BASE_URL_DEV)
        logged_app.project_page.create_project(
            project_abbreviation,
            f"{PROJECT_ZH_NAME_PREFIX}permission-{suffix}",
            f"{PROJECT_EN_NAME_PREFIX}permission-{suffix}",
            f"{PROJECT_DESCRIPTION_PREFIX}permission-{suffix}",
        )
        logged_app.page.goto(BASE_URL_DEV)
        logged_app.operate_page.go_to_permission_page(project_abbreviation)
        create_permission_initialization(logged_app)
        logged_app.page.goto(BASE_URL_DEV)
        logged_app.operate_page.go_to_permission_page(project_abbreviation)
        yield context
    finally:
        if should_cleanup(data_mode):
            try:
                if project_abbreviation == PERMISSION_PROJECT_ABBR:
                    raise AssertionError(
                        "Isolated Permission cleanup received the baseline project"
                    )

                logged_app.page.keyboard.press("Escape")
                logged_app.page.goto(BASE_URL_DEV)
                if logged_app.project_page.project_exists(project_abbreviation):
                    logged_app.operate_page.go_to_permission_page(project_abbreviation)
                    logged_app.single_sign_on_page.delete_application_if_exists(
                        PERMISSION_SSO_APPLICATION_NAME
                    )
                    logged_app.server_to_server_page.delete_application_if_exists(
                        PERMISSION_S2S_APPLICATION_NAME
                    )
                    logged_app.page.goto(BASE_URL_DEV)
                    logged_app.operate_page.go_to_permission_page(project_abbreviation)
                    if not logged_app.application_permission_page.permission_initialization_available():
                        logged_app.default_permission_page.delete_default_permission_if_exists(
                            PERMISSION_ROLE_CODE
                        )
                        logged_app.role_page.delete_role_if_exists(PERMISSION_ROLE_CODE)
                        logged_app.scope_page.delete_scope_if_exists(PERMISSION_SCOPE_CODE)
                    logged_app.page.goto(BASE_URL_DEV)
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


@dataclass(frozen=True)
class PermissionProjectContext:
    app: OmniApp
    abbreviation: str


"""
用途:維持 Scope/Role/Default Permission 原本只取得 OmniApp 的介面。

permission_project 先完成 Project 前置與生命週期管理,這裡只取出同一個OmniApp object.
確保下游 fixtures 與 teardown 都操作同一個 browser page。
"""
@pytest.fixture
def permission_project_app(
    permission_project: PermissionProjectContext,
) -> OmniApp:
    return permission_project.app


"""
用途:提供 Assign Permission 額外需要的專案成員與固定 SSO Application。

執行流程:
    1. permission_project 先準備 keep 主專案或 isolated UUID Project。
    2. 將固定第二位測試成員加入「本次 context 指定的專案」。
    3. 確認/建立 Assign Permission 成員清單需要的固定 SSO。
    4. keep 使用跨程序鎖;isolated 因 Project 不共用,不需要鎖。
    5. 最後回到該專案的身份驗證首頁,交給 Assign Permission 測試。
"""
@pytest.fixture
def assign_permission_project_app(
    permission_project: PermissionProjectContext,
    data_mode: str,
) -> OmniApp:
    context = permission_project

    def prepare_prerequisites() -> None:
        ensure_permission_project_member(
            context.app,
            context.abbreviation,
            create_missing=True,
        )
        context.app.page.goto(BASE_URL_DEV)
        context.app.operate_page.go_to_permission_page(context.abbreviation)
        ensure_sso_application(context.app, create_missing=True)
        context.app.page.goto(BASE_URL_DEV)
        context.app.operate_page.go_to_permission_page(context.abbreviation)

    if data_mode == KEEP:
        with permission_project_lock():
            prepare_prerequisites()
    else:
        prepare_prerequisites()

    return context.app


"""
用途:提供 Group 額外需要的固定 SSO Application。

執行流程:
    1. permission_project 先準備 keep 主專案或 isolated UUID Project。
    2. 只確認/建立 Group 必要的 SSO,不建立 S2S。
    3. keep 使用跨程序鎖;isolated 的固定 SSO 建在專屬 UUID Project 內。
    4. isolated teardown 由 permission_project 先刪除 SSO,再刪除 Project。
"""


@pytest.fixture
def group_permission_project_app(
    permission_project: PermissionProjectContext,
    data_mode: str,
) -> OmniApp:
    context = permission_project

    def prepare_sso() -> None:
        context.app.page.goto(BASE_URL_DEV)
        context.app.operate_page.go_to_permission_page(context.abbreviation)
        ensure_sso_application(context.app, create_missing=True)
        context.app.page.goto(BASE_URL_DEV)
        context.app.operate_page.go_to_permission_page(context.abbreviation)

    if data_mode == KEEP:
        with permission_project_lock():
            prepare_sso()
    else:
        prepare_sso()

    return context.app


#  Browser settings

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
