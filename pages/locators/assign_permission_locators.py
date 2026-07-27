from pages.locators.elements_base import ElementsBase


class AssignPermissionLocators(ElementsBase):

# Basic

    @property
    # 權限設定_指定權限分頁
    def tab_permission_assign(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper div', has=self.page.get_by_text("指定權限"))

    @property
    # 權限設定_指定權限分頁_新增預設權限按鈕
    def btn_create_assign_permission(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div.function-bar div.function-bar__item button', has=self.page.get_by_text('新增指定權限'))

    @property
    # 權限設定_指定權限分頁_新增/編輯指定權限頁面_描述欄位
    def input_assign_permission_description(self):
        return self.page.locator('[formcontrolname="remark"]')

# Create

    @property
    # 權限設定_指定權限分頁_新增指定權限頁面_新增權限按鈕
    def btn_assign_create_more_assign(self):
        return self.page.locator('app-permission-assign button.btn')

    @property
    # 權限設定_指定權限分頁_新增指定權限頁面_角色及範圍的新增按鈕
    def btn_more_permission(self):
        return self.page.locator('[formarrayname="assigns"] app-custom-form-field .cursor-pointer app-icon')

    @property
    # 權限設定_指定權限分頁_新增指定權限頁面_角色新增下拉清單
    def list_assign_permission_role(self):
        return self.page.locator('[formarrayname="assigns"] [formcontrolname="id"]')

    @property
    # 權限設定_指定權限分頁_新增指定權限頁面_範圍新增下拉清單    
    def list_assign_permission_scope(self):
        return self.page.locator('[formarrayname="assigns"] [formcontrolname="id"]')

# Update

    @property
    # 權限設定_指定權限分頁_編輯指定權限頁面_範圍下拉清單    
    def list_assign_edit_permission_role(self):
        return self.page.locator('app-permission-assign-edit [formcontrolname="id"]')
    
    # 權限設定_指定權限分頁_編輯指定權限頁面_範圍下拉清單    
    @property
    def list_assign_edit_permission_scope(self):
        return self.page.locator('app-permission-assign-edit [formcontrolname="id"]')
