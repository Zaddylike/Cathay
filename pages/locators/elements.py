from playwright.sync_api import Page

from pages.locators.application_permission_locators import ApplicationPermissionLocators
from pages.locators.application_s2s_locators import ApplicationS2sLocators
from pages.locators.application_sso_locators import ApplicationSsoLocators
from pages.locators.common_locators import CommonLocators
from pages.locators.login_locators import LoginLocators
from pages.locators.operation_locators import OperationLocators
from pages.locators.project_locators import ProjectLocators
from pages.locators.project_member_locators import ProjectMemberLocators


class BaseElements(CommonLocators):
    def __init__(self, page: Page):
        self.page = page


class LoginElements(CommonLocators, LoginLocators):
    def __init__(self, page: Page):
        self.page = page


class ProjectElements(CommonLocators, ProjectLocators):
    def __init__(self, page: Page):
        self.page = page


class ProjectMemberElements(CommonLocators, ProjectMemberLocators):
    def __init__(self, page: Page):
        self.page = page

class ApplicationPermissionElements(CommonLocators, ApplicationPermissionLocators):
    def __init__(self, page: Page):
        self.page = page

class ApplicationS2sElements(CommonLocators, ApplicationS2sLocators):
    def __init__(self, page: Page):
        self.page = page

class ApplicationSsoElements(CommonLocators, ApplicationSsoLocators):
    def __init__(self, page: Page):
        self.page = page

class OperationElements(CommonLocators, OperationLocators):
    def __init__(self, page: Page):
        self.page = page


class AllElements(
    CommonLocators,
    LoginLocators,
    ProjectLocators,
    ProjectMemberLocators,
    ApplicationPermissionLocators,
    ApplicationS2sLocators,
    ApplicationSsoLocators,
    OperationLocators,
):
    def __init__(self, page: Page):
        self.page = page
