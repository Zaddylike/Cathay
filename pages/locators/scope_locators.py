from playwright.sync_api import Page


class ScopeLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def tab_permission_scope(self):
        #
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(3)')

    @property
    def btn_create_scope(self):
        #
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button', has=self.page.get_by_text(" 新增範圍 ", exact=True))

    @property
    def input_scope_code(self):
        #
        return self.page.locator('[formcontrolname="code"]')

    @property
    def input_scope_name(self):
        #
        return self.page.locator('[formcontrolname="name"]')

    @property
    def input_scope_description(self):
        #
        return self.page.locator('[formcontrolname="description"]')

    @property
    def btn_scope_add_more_scope(self):
        # 身分驗證頁面_分頁_新增頁面_範圍
        return self.page.locator("app-permission-scope").get_by_text(" 新增範圍")
    
    @property
    def input_permission_init_scope_name(self):
        # 身分驗證頁面_分頁_新增頁面_範圍_名稱
        return self.page.locator('[formcontrolname="name"]')