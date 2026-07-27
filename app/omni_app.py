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
from pages.application_permission_page import ApplicationPermissionPage
from pages.application_s2s_page import ApplicationServerToServerPage
from pages.application_sso_page import ApplicationSingleSignOnPage


class OmniApp:
    def __init__(self, page: Page):
        self.shared_page = (self.base_page, self.operate_page)

        self.page = page
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page, self.base_page)
        self.login_page = LoginPage(page, self.base_page)
        self.project_page = ProjectPage(page, self.base_page, self.operate_page)
        self.project_member_page = ProjectMemberPage(page, *self.shared_page)
        self.scope_page = ScopePage(page, self.base_page, self.operate_page)
        self.role_page = RolePage(page, self.base_page, self.operate_page)
        self.group_page = GroupPage(page, self.base_page, self.operate_page)
        self.assign_permission_page = AssignPermissionPage(page, *self.shared_page)
        self.default_permission_page = DefaultPermissionPage(page, *self.shared_page)
        self.application_permission_page = ApplicationPermissionPage(page, *self.shared_page)
        self.single_sign_on_page = ApplicationSingleSignOnPage(page, *self.shared_page)
        self.server_to_server_page = ApplicationServerToServerPage(page, *self.shared_page)
        self.permission_page = self.application_permission_page
        self.single_signon_page = self.single_sign_on_page
        self.server_to_servser_page = self.server_to_server_page

    @allure.step("開啟瀏覽器 & 確認網頁Title & 登入程序")
    def login_by_account(self, account: str, password: str):
        try:
            self.login_page.open_browser()
            self.login_page.verify_title()
            self.login_page.user_login(account, password)
        except Exception as e:
            raise Exception(f"Failed to login by account: {e}")
