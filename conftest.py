import pytest
from playwright.sync_api import (
    sync_playwright,
    Playwright,
    Browser,
    BrowserContext,
    Page
)
from app.omni_app import OmniApp

"""
fixture
測試前置動作
測試後置動作
Page Object 初始化
測試失敗截圖
登入狀態
瀏覽器 context 設定
"""

@pytest.fixture
def app(page: Page):
    try:
        return OmniApp(page)
    except Exception as e:
        raise Exception(f"Failed to initialize OmniApp: {e}")


@pytest.fixture
def logged_app(page: Page):
    try:
        omni_app  = OmniApp(page)
        omni_app.login_by_account("testuser01", "testuser01")
        return omni_app
    except Exception as e:
        raise Exception(f"Failed to log in: {e}")
    

@pytest.fixture(scope="session")
def playwright_instance():
    try:
        with sync_playwright() as playwright:
            yield playwright
    except Exception as e:
        raise Exception(f"Failed to start Playwright: {e}")


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright):
    try:
        browser = playwright_instance.chromium.launch(
            channel="chrome",
            headless=False,
            args=[
                "--disable-features=Translate,TranslateUI",
                "--disable-translate",
                # "--lang=zh-TW",
                # "--headless=new"
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled",
            ],
        )

        yield browser

        browser.close()

    except Exception as e:
        raise Exception(f"Failed to launch browser: {e}")


@pytest.fixture
def context(browser: Browser):
    try:
        context = browser.new_context(
            java_script_enabled=True,
            locale="zh-TW",
            viewport={
                "width": 1500,
                "height": 768,
            },
            extra_http_headers={
                "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
            },
        )

        yield context

        context.close()

    except Exception as e:
        raise Exception(f"Failed to create browser context: {e}")


@pytest.fixture
def page(context: BrowserContext):
    try:
        page = context.new_page()

        yield page

        page.close()

    except Exception as e:
        raise Exception(f"Failed to create page: {e}")

# @pytest.fixture(scope="session")
# def browser_type_launch_args(browser_type_launch_args):
#     try:
#         return {
#             **browser_type_launch_args,
#             "headless": False,
#             "args": [
#                 "--disable-blink-features=AutomationControlled",
#                 "--no-sandbox",
#                 "--disable-setuid-sandbox",
#                 "--disable-dev-shm-usage",
#             ],
#         }
#     except Exception as e:
#         raise Exception(f"Set browser launch args failed: {e}")


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     try:
#         return {
#             **browser_context_args,
#             "java_script_enabled": True,
#             "viewport": {
#                 "width": 1500,
#                 "height": 768,
#             },
#         }
#     except Exception as e:
#         raise Exception(f"Set browser context args failed: {e}")