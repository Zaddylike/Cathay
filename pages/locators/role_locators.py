from playwright.sync_api import Page

class RoleLocators:
    def __init__(self, page: Page):
        self.page = page

    # Entry / Page

    @property
    # 權限設定頁面_分頁_角色
    def tab_permission_role(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(4)')

    @property
    # 權限設定頁面_角色新增按鈕
    def btn_create_role(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button', has=self.page.get_by_text(" 新增角色 ", exact=True))

    # Role Form

    @property
    # 角色新增頁面_角色代碼
    def input_role_code(self):
        return self.page.locator('[formcontrolname="code"]')

    @property
    # 角色新增頁面_角色名稱
    def input_role_name(self):
        return self.page.locator('[formcontrolname="name"]')

    @property
    # 角色新增頁面_角色描述
    def input_role_description(self):
        return self.page.locator('[formcontrolname="description"]')

    @property
    # 身分驗證頁面_分頁_新增頁面_角色_名稱
    def input_permission_init_role_name(self):
        return self.page.locator('[formcontrolname="name"]')

    # Role Actions

    @property
    # 身分驗證頁面_分頁_新增頁面_新增更多角色按鈕
    def btn_role_add_more_role(self):
        return self.page.locator("app-permission-role").get_by_text(" 新增角色")
