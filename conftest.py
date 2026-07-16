import pytest
from playwright.sync_api import Page

from app.omni_app import OmniApp
from config.settings import ACCOUNT_PASSWORD, ACCOUNT_USERNAME, HEADLESS, BROWSER_ARGS
from utils.data_mode import DATA_MODES, KEEP, permission_project_lock
from utils.permission_baseline import ensure_permission_baseline


def pytest_addoption(parser):
    """
    用途：集中管理專案自訂的 pytest CLI 參數。

    執行流程：
        1. --data-mode 控制測試資料是否於 teardown 清除。
    """
    parser.addoption(
        "--data-mode",
        action="store",
        choices=DATA_MODES,
        default="isolated",
        help="Test data lifecycle: isolated deletes fixture data; keep retains it",
    )


@pytest.fixture(scope="session")
def data_mode(pytestconfig) -> str:
    """
    用途：將 --data-mode 轉成其他 fixtures 可以注入使用的字串。

    執行流程：
        1. pytest 解析 CLI。
        2. 未傳入時回傳 isolated。
        3. 傳入 --data-mode=keep 時回傳 keep。
    """
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


@pytest.fixture
def permission_project_app(logged_app: OmniApp, data_mode: str) -> OmniApp:
    """
    運行順序:
        1. 建立Page object -> logged_app.
        2. 分流測試模式: [ isolated、keep ]
        3.1.keep:
            1. 進入程序鎖.
            2. 檢查前置作業, 有缺就補.
        3.2.isolated:
            1. 檢查前置作業, 有缺就報錯.
        4. 回傳Page object, 開始測試.
    """
    if data_mode == KEEP:
        with permission_project_lock():
            ensure_permission_baseline(logged_app, create_missing=True)
    else:
        ensure_permission_baseline(logged_app, create_missing=False)
    return logged_app


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": browser_type_launch_args.get("headless", HEADLESS),
        # "slow_mo": 500,
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
