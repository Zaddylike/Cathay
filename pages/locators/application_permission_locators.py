from pages.locators.elements_base import ElementsBase


class ApplicationPermissionLocators(ElementsBase):



# Entry / Page

    @property
    # 身分驗證頁面_分頁_權限設定
    def tab_permission(self):
        return self.page.locator('[role="tablist"] p-tab', has=self.page.get_by_text("權限設定"))
    
    @property
    # 身分驗證頁面_權限設定頁面
    def btn_permission_add_permission(self):
        return self.page.locator("app-applications p-tabs p-tabpanel:nth-child(3)").get_by_text("新增權限")



    # Scope

    @property
    # 身分驗證_範圍_新增頁面
    def page_perms_scope_create(self):
        return self.page.locator("app-permission-scope")

    @property
    # 身分驗證_範圍_新增頁面_新增範圍按鈕
    def btn_permission_add_scope(self):
        return self.page.locator("app-permission-scope button").get_by_text("新增範圍")

    @property
    # 身分驗證_範圍_新增頁面_代碼
    def input_permission_init_scope_code(self):
        return self.page.locator('app-permission-scope [formcontrolname="code"]')

    @property
    # 身分驗證_範圍_新增頁面_名稱
    def input_permission_init_scope_name(self):
        return self.page.locator('app-permission-scope [formcontrolname="name"]')

    @property
    # 身分驗證_範圍_新增頁面_描述
    def input_permission_init_scope_description(self):
        return self.page.locator('app-permission-scope [formcontrolname="description"]')

    @property
    # 身分驗證_範圍_新增頁面_箭頭
    def arrow_extend_page(self):
        return self.page.locator('app-permission-scope .border-circle')

    @property
    # 身分驗證_範圍_垃圾桶_按鈕
    def btn_perms_remove_create(self):
        return self.page.locator('p-accordion-header app-custom-form-field  [tooltipposition="bottom"] app-icon')


    # Role

    @property
    # 身分驗證_角色_新增頁面
    def page_perms_role_create(self):
        return self.page.locator("app-permission-role")

    @property
    # 身分驗證_角色_新增頁面_新增角色按鈕
    def btn_permission_add_role(self):
        return self.page.locator('app-permission-role button').get_by_text("新增角色")

    @property
    # 身分驗證_角色_新增頁面_代碼
    def input_permission_init_role_code(self):
        return self.page.locator('app-permission-role [formcontrolname="code"]')

    @property
    # 身分驗證_角色_新增頁面_名稱
    def input_permission_init_role_name(self):
        return self.page.locator('app-permission-role [formcontrolname="name"]')

    @property
    # 身分驗證_角色_新增頁面_描述
    def input_permission_init_role_description(self):
        return self.page.locator('app-permission-role [formcontrolname="description"]')

    @property
    # 身分驗證_角色_新增頁面_箭頭
    def arrow_extend_role_page(self):
        return self.page.locator('app-permission-role .border-circle')

    @property
    # 身分驗證_角色_新增頁面_範圍清單_展開
    def btn_permission_scope_list(self):
        return self.page.locator('app-permission-role [role="combobox"]')

    @property
    # 身分驗證_角色_新增頁面_範圍清單
    def opt_permission_scope_list(self):
        return self.page.locator('[role="option"]')

    @property
    # 身分驗證_角色_新增頁面_新增設定範圍筆數的按鈕
    def btn_permission_role_more_scope(self):
        return self.page.locator('app-permission-role [tooltipposition="bottom"] p', has=self.page.get_by_text("新增"))

    @property
    # 身分驗證_角色_新增頁面_選擇範圍_清單_新增代碼欄位
    def input_perms_role_scope_create_code(self):
        return self.page.locator('.p-select--footer app-custom-form-field input[formcontrolname="code"]')

    @property
    # 身分驗證_角色_新增頁面_選擇範圍_清單_新增代碼欄位
    def input_perms_role_scope_create_name(self):
        return self.page.locator('.p-select--footer app-custom-form-field input[formcontrolname="name"]')

    @property
    # 身分驗證_角色_新增頁面_選擇範圍_清單_新增代碼欄位
    def btn_perms_role_scope_create(self):
        return self.page.locator('.p-select--footer button')


    # Group

    @property
    # 身分驗證_群組_新增頁面
    def page_perms_group_create(self):
        return self.page.locator("app-permission-group p-accordion-panel")

    @property
    # 身分驗證_群組_新增頁面_新增群組按鈕
    def btn_permission_add_group(self):
        return self.page.locator("app-permission-group button").get_by_text("新增群組")

    @property
    # 身分驗證_群組_新增頁面_名稱
    def input_permission_init_group_name(self):
        return self.page.locator('app-permission-group [formcontrolname="name"]')

    @property
    # 身分驗證_群組_新增頁面_描述
    def input_permission_init_group_description(self):
        return self.page.locator('app-permission-group [formcontrolname="description"]')

    @property
    # 身分驗證_群組_新增頁面_新增成員按鈕
    def btn_group_add_member(self):
        return self.page.locator('app-permission-group [tooltipposition="bottom"] button').get_by_text("新增成員")



    # Assign

    @property
    # 身分驗證_指定_新增頁面
    def page_perms_assign_create(self):
        return self.page.locator("app-application-permission app-permission-assign")

    @property
    # 身分驗證頁面_權限設定頁面
    def btn_permission_add_assign(self):
        return self.page.locator("app-application-permission app-permission-assign", has=self.page.get_by_text("新增權限"))

    @property
    # 
    def list_permission_role(self):
        return self.page.locator('app-application-permission app-permission-assign p-accordion-content app-custom-form-field app-select')

    # Default  

    @property
    # 身分驗證_預設_新增頁面
    def page_perms_default_create(self):
        return self.page.locator("app-application-permission app-permission-default")

    @property
    # 
    def btn_perms_default_scope_list(self):
        return self.page.locator('app-application-permission app-permission-default [formarrayname="scopes"] button')

    @property
    # 
    def btn_perms_default_role_list(self):
        return self.page.locator('app-application-permission app-permission-default [formarrayname="roles"] button')

    @property
    # 
    def list_perms_default_scope_list(self):
        return self.page.locator('app-application-permission app-permission-default [formarrayname="scopes"] app-select')

    @property
    # 
    def list_perms_default_role_list(self):
        return self.page.locator('app-application-permission app-permission-default [formarrayname="roles"] app-select')




    @property
    # 身分驗證頁面_分頁_新增頁面_預設權限_
    def input_permission_remark(self):
        return self.page.locator('app-application-permission app-permission-assign [formcontrolname="remark"]')


