from pages.locators.elements_base import ElementsBase


class ApplicationS2sLocators(ElementsBase):

# Entry / Page

    @property
    # 身分驗證頁面_分頁_權限設定
    def tab_permission(self):
        return self.page.locator("div.p-tablist-content p-tab", has=self.page.get_by_text("權限設定"))

    @property
    # 身分驗證頁面_分頁_伺服器串接
    def tab_s2s(self):
        return self.page.locator("div.p-tablist-content p-tab", has=self.page.get_by_text("伺服器串接"))
    

# Create Application

    @property
    # 身分驗證_伺服器串接分頁_新增應用端按鈕
    def btn_permission_add_s2s(self):
        return self.page.locator('[data-p-active="true"] button', has_text=" 新增應用端 ")

    @property
    # 身分驗證_新增伺服器串接分頁_姓名欄位
    def input_s2s_application_name(self):
        return self.page.locator('[formcontrolname="name"]')
    
    @property
    # 身分驗證_新增伺服器串接分頁_描述欄位
    def input_s2s_application_description(self):
        return self.page.locator('[formcontrolname="description"]')
    

    # Scope

    @property
    # 身分驗證_新增伺服器串接分頁_心曾範圍按鈕
    def btn_s2s_add_scope(self):
        return self.page.get_by_text(" 新增範圍")
    

    @property
    # 身分驗證_新增伺服器串接分頁_新增範圍下拉清單
    def list_s2s_scope(self):
        return self.page.locator('[formcontrolname="code"] p-select')

    @property
    # 身分驗證_新增伺服器串接分頁_新增範圍描述
    def input_s2s_scope_description(self):
        return self.page.locator('[formcontrolname="description"]').last
