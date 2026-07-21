from playwright.sync_api import Page

class RoleLocators:
    def __init__(self, page: Page):
        self.page = page
    
# Basic

    @property
    # 權限設定頁面_角色
    def tab_permission_role(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper div', has=self.page.get_by_text("角色"))

    @property
    # 權限設定_角色頁面_角色新增按鈕
    def btn_create_role(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button', has=self.page.get_by_text("新增角色"))

    @property
    # 權限設定_角色_新增/編輯角色頁面_名稱欄位
    def input_role_name(self):
        return self.page.locator('[formcontrolname="name"]')

    @property
    # 權限設定_角色_新增/編輯角色頁面_描述欄位
    def input_role_description(self):
        return self.page.locator('[formcontrolname="description"]')

# Create

    @property
    # 權限設定_範圍_新增範圍頁面_代碼欄位
    def input_role_code(self):
        return self.page.locator('[formcontrolname="code"]')

    @property
    # 權限設定_角色_新增角色頁面_新增角色按鈕
    def btn_role_add_more_role(self):
        return self.page.locator("app-permission-role-edit app-permission-role").get_by_text("新增角色")