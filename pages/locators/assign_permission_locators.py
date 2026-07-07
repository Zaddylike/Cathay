from playwright.sync_api import Page


class AssignPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def tab_permission_assign(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(6)')

    @property
    def btn_create_assign_permission(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    @property
    def btn_add_assign_permission(self):
        return self.page.locator("app-permission-assignment button, app-assign-permission button").first

    @property
    def btn_assign_member_search(self):
        return self.page.locator('p-iconfield p-inputicon.cursor-pointer').first

    @property
    def list_assign_permission_role(self):
        return self.page.locator('[formcontrolname="id"]').first

    @property
    def list_assign_permission_scope(self):
        return self.page.locator('[formcontrolname="id"]').last

    @property
    def input_assign_permission_description(self):
        return self.page.locator('[formcontrolname="remark"]')
