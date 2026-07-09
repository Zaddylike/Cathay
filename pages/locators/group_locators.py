from playwright.sync_api import Page

class GroupLocators:
    def __init__(self, page: Page):
        self.page = page

    # Entry / Page

    @property
    # 身分驗證頁面_分頁_群組
    def tab_permission_group(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(5)')

    @property
    # 群組頁面_新增群組按鈕
    def btn_create_group(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    # Create Group

    @property
    # 群組頁面_新增群組頁面_新增群組按鈕
    def btn_create_more_group(self):
        return self.page.locator('app-permission-group button.btn').get_by_text("新增群組")

    @property
    # 群組頁面_新增群組頁面_新增成員按鈕
    def btn_group_header_add_member(self):
        return self.page.locator('app-permission-group app-custom-form-field button').get_by_text("新增成員")

    @property
    # 群組頁面_新增群組頁面_名稱
    def input_group_name(self):
        return self.page.locator('[formcontrolname="name"]')

    @property
    # 群組頁面_新增群組頁面_描述
    def input_group_description(self):
        return self.page.locator('[formcontrolname="description"]')

    @property
    # 群組頁面_新增群組頁面_新增成員按鈕
    def btn_group_add_member(self):
        return self.page.locator('[formarrayname="members"] button').last

    @property
    # 群組頁面_新增群組頁面_新增更多群組按鈕
    def btn_group_add_more_group(self):
        return self.page.locator("app-permission-group button").last
