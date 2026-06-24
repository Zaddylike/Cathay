from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.project_page import ProjectPage
import allure

class OmniApp:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
        self.base_page = BasePage(page)
        self.project_page = ProjectPage(page)
        
    @allure.step("開啟瀏覽器")
    def login_by_account(self, account: str, password: str):
        try:
            self.login_page.open_browser()
            self.login_page.verify_title()
            self.login_page.user_login(account, password)
        except Exception as e:
            raise Exception(f"Failed to login by account: {e}")
