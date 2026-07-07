import allure
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.operate_page import OperatePage
from pages.login_page import LoginPage
from pages.project_page import ProjectPage
from pages.project_member_page import ProjectMemberPage
from pages.role_page import RolePage
from pages.scope_page import ScopePage
from pages.group_page import GroupPage
from pages.assign_permission_page import AssignPermissionPage
from pages.default_permission_page import DefaultPermissionPage
from pages.application_page import ApplicationPermissionPage, ApplicationSingleSignOnPage, ApplicationServerToServerPage


class OmniApp:
    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)
        self.login_page = LoginPage(page)
        self.project_page = ProjectPage(page)
        self.project_member_page = ProjectMemberPage(page)
        self.scope_page = ScopePage(page)
        self.role_page = RolePage(page)
        self.group_page = GroupPage(page)
        self.assign_permission_page = AssignPermissionPage(page)
        self.default_permission_page = DefaultPermissionPage(page)
        self.permission_page = ApplicationPermissionPage(page)
        self.single_signon_page = ApplicationSingleSignOnPage(page)
        self.server_to_servser_page = ApplicationServerToServerPage(page)

    @allure.step("開啟瀏覽器&確認目標網站&登入作業")
    def login_by_account(self, account: str, password: str):
        try:
            self.login_page.open_browser()
            self.login_page.verify_title()
            self.login_page.user_login(account, password)
        except Exception as e:
            raise Exception(f"Failed to login by account: {e}")
