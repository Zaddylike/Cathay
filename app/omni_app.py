from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.operation_page import OperationPage
from pages.login_page import LoginPage
from pages.project_page import ProjectPage
from pages.project_member_page import ProjectMemberPage
from pages.application_page import ApplicationPermissionPage, ApplicationSingleSignOnPage, ApplicationServerToServerPage
import allure

class OmniApp:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
        self.base_page = BasePage(page)
        self.project_page = ProjectPage(page)
        self.project_member_page = ProjectMemberPage(page)
        self.permission_page = ApplicationPermissionPage(page)
        self.single_signon_page = ApplicationSingleSignOnPage(page)
        self.server_to_servser_page = ApplicationServerToServerPage(page)

    @allure.step("開啟瀏覽器")
    def login_by_account(self, account: str, password: str):
        try:
            self.login_page.open_browser()
            self.login_page.verify_title()
            self.login_page.user_login(account, password)
        except Exception as e:
            raise Exception(f"Failed to login by account: {e}")
