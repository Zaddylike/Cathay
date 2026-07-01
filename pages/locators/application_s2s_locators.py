from playwright.sync_api import Page


class ApplicationS2sLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def btn_project_info_permission(self):
        # 專案資訊頁面_身分認證按鈕
        return self.page.locator(".sidebar__list", has=self.page.get_by_text(" 身份認證 ", exact=True))

    @property
    def page_permission(self):
        # 身分驗證頁面_logo
        return self.page.locator(".text-type--content-title")

    @property
    def tab_permission(self):
        # 身分驗證頁面_分頁_權限設定
        return self.page.locator('[role="tablist"] p-tab', has_text=" 權限設定 ")

    @property
    def tab_s2s(self):
        # 身分驗證頁面_分頁_伺服器串接
        return self.page.locator('[role="tablist"] p-tab', has_text=" 伺服器串接 ")
    
    @property
    def btn_permission_add_s2s(self):
        # 身分驗證頁面_伺服器串接分頁_新增應用端按鈕
        return self.page.locator('[data-p-active="true"] button', has_text=" 新增應用端 ")

    @property
    def input_s2s_application_name(self):
        #
        return self.page.locator('[formcontrolname="name"]')
    
    @property
    def input_s2s_application_description(self):
        #
        return self.page.locator('[formcontrolname="description"]')
    
    @property
    def btn_s2s_add_scope(self):
        # 
        return self.page.get_by_text(" 新增範圍")
    
    @property
    def list_s2s_scope(self):
        #
        return self.page.locator('[formcontrolname="scopes"]')