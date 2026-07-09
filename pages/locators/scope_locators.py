from playwright.sync_api import Page

class ScopeLocators:
    def __init__(self, page: Page):
        self.page = page

    # Entry / Page

    @property
    # 權限設定頁面_分頁_範圍
    def tab_permission_scope(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(3)')

    @property
    # 權限設定頁面_範圍新增按鈕
    def btn_create_scope(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button', has=self.page.get_by_text(" 新增範圍 ", exact=True))

    # Scope Form

    @property
    # 範圍新增頁面_範圍代碼
    def input_scope_code(self):
        return self.page.locator('[formcontrolname="code"]')

    @property
    # 範圍新增頁面_範圍名稱
    def input_scope_name(self):
        return self.page.locator('[formcontrolname="name"]')

    @property
    # 範圍新增頁面_範圍描述
    def input_scope_description(self):
        return self.page.locator('[formcontrolname="description"]')

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍_名稱
    def input_permission_init_scope_name(self):
        return self.page.locator('[formcontrolname="name"]')

    # Scope Actions

    @property
    # 身分驗證頁面_分頁_新增頁面_新增更多範圍按鈕
    def btn_scope_add_more_scope(self):
        return self.page.locator("app-permission-scope").get_by_text(" 新增範圍")
