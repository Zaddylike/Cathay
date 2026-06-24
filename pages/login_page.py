from playwright.sync_api import Page, expect
from config.settings import BASE_URL_DEV, DEFAULT_TIMEOUT
from pages.elements import Elements
from pages.base_page import BasePage
import allure

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = Elements(page)
        self.base_page = BasePage(page)

    @allure.step("開啟瀏覽器")
    def open_browser(self):
        try:
            self.page.set_default_timeout(DEFAULT_TIMEOUT)
            self.page.goto(
                BASE_URL_DEV,
                wait_until="load", # "load", "domcontentloaded" 用這兩就好
                timeout=DEFAULT_TIMEOUT,
            )
        except Exception as e:
            raise Exception(f"Failed to open browser: {e}")

    @allure.step("驗證目標頁面是否正確")
    def verify_title(self):
        try:
            expect(self.page).to_have_title("Omni")
        except Exception as e:
            raise AssertionError(f"Failed to verify page title: {e}")
    
    def change_language(self, language: str):
        try:
            self.base_page.click_expect(self.elements.language_arrow, self.elements.language_list)
            self.base_page.click_expect(self.elements.language_option_en if language == "EN" else self.elements.language_option_zh)
            self.base_page.wait_loading_disapper()
        except Exception as e:
            raise Exception(f"Failed to change language: {e}")

    @allure.step("點擊登入按鈕/輸入帳號密碼: {account}")
    def user_login(self, account: str, password: str):
        try:
            self.elements.btn_login.click()
            self.elements.input_account.fill(account)
            self.elements.input_password.fill(password)
            self.base_page.click_expect(self.elements.btn_login, self.elements.btn_user_avatar)
        except Exception as e:
            raise Exception(f"Failed to log in: {e}")

    def user_login_google(self, account: str, password: str):
        try:
            self.elements.btn_login.click()
            self.base_page.click_expect(self.elements.btn_login_google)
        except Exception as e:
            raise Exception(f"Failed to log in with Entra ID: {e}")
        try:
            self.elements.input_account_google.fill(account)
            self.page.get_by_text("下一步").first.click()
            self.elements.input_password_google.fill(password)
            self.page.get_by_text("下一步").last.click()
            expect(self.elements.btn_user_avatar).to_be_visible(timeout=10000)
        except Exception as e:
            raise Exception(f"Failed to log in with Entra ID: {e}")
        
    def user_login_entra(self,account: str, password: str):
        try:
            self.elements.btn_login.click()
            self.base_page.click_expect(self.elements.btn_login_entra, self.elements.logo_entra)
        except Exception as e:
            raise Exception(f"Failed to log in with Entra ID: {e}")
        try:
            self.elements.input_account_entra.fill(account)
            self.elements.btn_login_nextStep.click()
            self.elements.input_password_entra.fill(password)
            self.base_page.click_expect(self.elements.btn_login_nextStep, self.elements.btn_user_avatar)
        except Exception as e:
            raise Exception(f"Failed to log in with Entra ID: {e}")
        
    def user_logout(self):
        try:
            self.elements.btn_user_avatar.click()
            self.elements.btn_logout.click()
        except Exception as e:
            raise Exception(f"Failed to log out: {e}")
            
