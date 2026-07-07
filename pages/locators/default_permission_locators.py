from playwright.sync_api import Page


class DefaultPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def tab_permission_default(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(7)')

    @property
    def btn_create_default_permission(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    @property
    def btn_add_default_role(self):
        return self.page.locator("app-permission-default button, app-default-permission button").first

    @property
    def btn_add_default_scope(self):
        return self.page.locator("app-permission-default button, app-default-permission button").last

    @property
    def list_default_permission_role(self):
        return self.page.locator('[formcontrolname="id"]').first

    @property
    def list_default_permission_scope(self):
        return self.page.locator('[formcontrolname="id"]').last
