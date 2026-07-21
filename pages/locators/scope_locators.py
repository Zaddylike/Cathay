from playwright.sync_api import Page

class ScopeLocators:
    def __init__(self, page: Page):
        self.page = page

# Basic

    @property
    # 權限設定_範圍
    def tab_permission_scope(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper div', has=self.page.get_by_text("範圍"))

    @property
    # 權限設定_範圍_新增範圍按鈕
    def btn_create_scope(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div.function-bar div.function-bar__item button', has=self.page.get_by_text("新增範圍"))

    @property
    # 權限設定_範圍_新增/編輯範圍頁面_代碼欄位
    def input_scope_code(self):
        return self.page.locator('[formcontrolname="code"]')

    @property
    # 權限設定_範圍_新增/編輯範圍頁面_名稱欄位
    def input_scope_name(self):
        return self.page.locator('[formcontrolname="name"]')

    @property
    # 權限設定_範圍_新增/編輯範圍頁面_描述欄位
    def input_scope_description(self):
        return self.page.locator('[formcontrolname="description"]')

# Create

    @property
    # 權限設定_範圍_新增範圍頁面_新增範圍按鈕
    def btn_scope_add_more_scope(self):
        return self.page.locator("app-permission-scope-edit app-permission-scope").get_by_text("新增範圍")
