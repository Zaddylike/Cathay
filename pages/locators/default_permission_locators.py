from playwright.sync_api import Page


class DefaultPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def tab_permission_default(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(1)')

    @property
    def btn_create_default_permission(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    @property
    def btn_default_add_role(self):
        return self.page.locator('[formarrayname="roles"] button')

    @property
    def list_default_role(self):
        return self.page.locator('[formarrayname="roles"] app-custom-form-field app-select')

    @property
    def btn_default_more_role(self):
        return self.page.locator('[formarrayname="roles"] .cursor-pointer')

    @property
    def btn_add_default_scope(self):
        return self.page.locator('[formarrayname="scopes"] button')
    
    @property
    def list_default_permission_scope(self):
        return self.page.locator('[formarrayname="scopes"] app-custom-form-field app-select')

    @property
    def btn_more_default_scope(self):
        return self.page.locator('[formarrayname="scopes"] .cursor-pointer')

    @property
    def bin_default_permission(self):
        return self.page.locator('app-icon[class="cursor-pointer"]')