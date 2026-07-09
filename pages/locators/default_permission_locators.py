from playwright.sync_api import Page

class DefaultPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    # Entry / Page

    @property
    # 身分驗證頁面_分頁_預設權限
    def tab_permission_default(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(7)')

    @property
    # 預設權限頁面_新增預設權限按鈕
    def btn_create_default_permission(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    # Create Default Permission

    @property
    # 預設權限頁面_新增預設角色按鈕
    def btn_add_default_role(self):
        return self.page.locator("app-permission-default button, app-default-permission button").first

    @property
    # 預設權限頁面_新增預設範圍按鈕
    def btn_add_default_scope(self):
        return self.page.locator("app-permission-default button, app-default-permission button").last

    @property
    # 預設權限頁面_角色清單
    def list_default_permission_role(self):
        return self.page.locator('[formcontrolname="id"]').first

    @property
    # 預設權限頁面_範圍清單
    def list_default_permission_scope(self):
        return self.page.locator('[formcontrolname="id"]').last
