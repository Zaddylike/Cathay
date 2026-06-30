from playwright.sync_api import Page


class ApplicationPermissionLocators:
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
    def btn_permission_add_permission(self):
        # 身分驗證頁面_分頁_權限設定
        return self.page.get_by_text(" 新增權限 ")
    
    @property
    def btn_permission_add_scope(self):
        # 身分驗證頁面_分頁_新增頁面_範圍
        return self.page.get_by_text(" 新增範圍")
    
    @property
    def input_permission_init_scope_code(self):
        # 身分驗證頁面_分頁_新增頁面_範圍_代碼
        return self.page.locator('[formcontrolname="code"]')
    
    @property
    def input_permission_init_scope_name(self):
        # 身分驗證頁面_分頁_新增頁面_範圍_名稱
        return self.page.locator('[formcontrolname="name"]')
    
    @property
    def input_permission_init_scope_description(self):
        # 身分驗證頁面_分頁_新增頁面_範圍_描述
        return self.page.locator('[formcontrolname="description"]')
    
    @property
    def arrow_extend_page(self):
        #展開範圍新增頁面箭頭
        return self.page.locator('.border-circle')
    
    @property
    def btn_permission_add_role(self):
        # 身分驗證頁面_分頁_新增頁面_角色
        return self.page.get_by_text(" 新增角色 ")
    @property
    def input_permission_init_role_code(self):
        # 身分驗證頁面_分頁_新增頁面_範圍_代碼
        return self.page.locator('[formcontrolname="code"]')
    
    @property
    def input_permission_init_role_name(self):
        # 身分驗證頁面_分頁_新增頁面_範圍_名稱
        return self.page.locator('[formcontrolname="name"]')
    
    @property
    def input_permission_init_role_description(self):
        # 身分驗證頁面_分頁_新增頁面_範圍_描述
        return self.page.locator('[formcontrolname="description"]')
    
    @property
    def arrow_extend_role_page(self):
        # 展開範圍新增頁面箭頭
        return self.page.locator('.border-circle')
    
    @property
    def btn_permission_scope_list(self):
        # 角色新增頁面_範圍清單_展開
        return self.page.locator('[role="combobox"]')

    @property
    def opt_permission_scope_list(self):
        # 角色新增頁面_範圍清單
        return self.page.locator('[role="option"]')
    
    @property
    def btn_permission_role_more_scope(self):
        #
        return self.page.locator('[tooltipposition="bottom"] p', has=self.page.get_by_text(" 新增 ", exact=True))
    @property
    def btn_dialog_permission_add_scope(self):
        #
        return self.page.get_by_text(" 新增範圍 ")
    
    @property
    def btn_permission_add_group(self):
        # 身分驗證頁面_分頁_新增頁面_群組
        return self.page.locator("app-permission-group button")
    
    @property
    def input_permission_init_group_name(self):
        # 身分驗證頁面_分頁_新增頁面_群組_名稱
        return self.page.locator('[formcontrolname="name"]')
    
    @property
    def input_permission_init_group_description(self):
        # 身分驗證頁面_分頁_新增頁面_群組_描述
        return self.page.locator('[formcontrolname="description"]')