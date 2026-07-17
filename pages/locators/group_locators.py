from playwright.sync_api import Page


class GroupLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def tab_permission_group(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(5)')

    @property
    def btn_create_group(self):
        return (
            self.page.locator('[role="tabpanel"]:visible')
            .get_by_role("button", name="新增群組", exact=True)
            .first
        )
    
    @property
    def btn_create_more_group(self):
        return self.page.locator('app-permission-group button.btn').get_by_text("新增群組")
    
    @property
    def btn_group_header_add_member(self):
        return self.page.locator('app-permission-group app-custom-form-field button').get_by_text("新增成員")

    @property
    def input_group_name(self):
        return self.page.locator('[formcontrolname="name"]')

    @property
    def input_group_description(self):
        return self.page.locator('[formcontrolname="description"]')

    @property
    def btn_group_add_member(self):
        return self.page.locator('[formarrayname="members"] button').last

    @property
    def btn_group_add_more_group(self):
        return self.page.locator("app-permission-group button").last
