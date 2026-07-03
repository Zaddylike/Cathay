from playwright.sync_api import Page

class ApplicationPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    # Entry / Page

    @property
    # 專案資訊頁面_身分認證按鈕
    def btn_project_info_permission(self):
        return self.page.locator(".sidebar__list", has=self.page.get_by_text(" 身份認證 ", exact=True))
    

    @property
    # 身分驗證頁面_logo
    def page_permission(self):
        return self.page.locator(".text-type--content-title")

    # @property
    # def tab_permission(self):
    #     # 身分驗證頁面_分頁_權限設定
    #     return self.page.locator('[role="tablist"] p-tab', has_text=" 權限設定 ")

    @property
    # 身分驗證頁面_分頁_權限設定
    def btn_permission_add_permission(self):
        return self.page.get_by_text(" 新增權限 ")
    

    # Scope

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍
    def btn_permission_add_scope(self):
        return self.page.get_by_text(" 新增範圍")
    

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍_代碼
    def input_permission_init_scope_code(self):
        return self.page.locator('[formcontrolname="code"]')
    

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍_名稱
    def input_permission_init_scope_name(self):
        return self.page.locator('[formcontrolname="name"]')
    

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍_描述
    def input_permission_init_scope_description(self):
        return self.page.locator('[formcontrolname="description"]')
    

    @property
    #展開範圍新增頁面箭頭
    def arrow_extend_page(self):
        return self.page.locator('.border-circle')
    

    # Role

    @property
    # 身分驗證頁面_分頁_新增頁面_角色
    def btn_permission_add_role(self):
        return self.page.get_by_text(" 新增角色 ")

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍_代碼
    def input_permission_init_role_code(self):
        return self.page.locator('[formcontrolname="code"]')
    

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍_名稱
    def input_permission_init_role_name(self):
        return self.page.locator('[formcontrolname="name"]')
    

    @property
    # 身分驗證頁面_分頁_新增頁面_範圍_描述
    def input_permission_init_role_description(self):
        return self.page.locator('[formcontrolname="description"]')
    

    @property
    # 展開範圍新增頁面箭頭
    def arrow_extend_role_page(self):
        return self.page.locator('.border-circle')
    

    @property
    # 角色新增頁面_範圍清單_展開
    def btn_permission_scope_list(self):
        return self.page.locator('[role="combobox"]')

    @property
    # 角色新增頁面_範圍清單
    def opt_permission_scope_list(self):
        return self.page.locator('[role="option"]')
    

    @property
    # 角色新增頁面_新增設定範圍筆數的按鈕
    def btn_permission_role_more_scope(self):
        return self.page.locator('[tooltipposition="bottom"] p', has=self.page.get_by_text(" 新增 ", exact=True))
    

    @property
    # 角色新增頁面_範圍選擇清單_新增範圍按鈕
    def btn_dialog_permission_add_scope(self):
        return self.page.get_by_text(" 新增範圍 ")
    

    # Group

    @property
    # 身分驗證頁面_分頁_新增頁面_群組
    def btn_permission_add_group(self):
        return self.page.locator("app-permission-group button")
    

    @property
    # 身分驗證頁面_分頁_新增頁面_群組_名稱
    def input_permission_init_group_name(self):
        return self.page.locator('[formcontrolname="name"]')
    

    @property
    # 身分驗證頁面_分頁_新增頁面_群組_描述
    def input_permission_init_group_description(self):
        return self.page.locator('[formcontrolname="description"]')
    

    @property
    # 身分驗證頁面_分頁_新增頁面_群組_新增成員按鈕
    def btn_group_add_member(self):
        return self.page.locator('[formarrayname="members"] button', has=self.page.get_by_text(" 新增成員 ", exact=True))

    # Permission Assignment

    @property
    # 身分驗證頁面_分頁_新增頁面_預設權限_成員清單
    def list_permission_role(self):
        return self.page.locator('[formcontrolname="id"]')

    @property
    # 身分驗證頁面_分頁_新增頁面_預設權限_
    def input_permission_remark(self):
        return self.page.locator('[formcontrolname="remark"]')
