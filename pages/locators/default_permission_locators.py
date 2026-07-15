from playwright.sync_api import Page


class DefaultPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    #  權限設定_預設權限分頁
    def tab_permission_default(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(1)')

    @property
    #  權限設定_預設權限分頁_新增預設權限
    def btn_create_default_permission(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    @property
    #  權限設定_預設權限分頁_新增預設權限頁面_新增角色按鈕
    def btn_add_default_role(self):
        return self.page.locator('[formarrayname="roles"] button')

    @property
    #  權限設定_預設權限分頁_新增預設權限頁面_新增範圍按鈕
    def btn_add_default_scope(self):
        return self.page.locator('[formarrayname="scopes"] button')

    @property
    #  權限設定_預設權限分頁_新增預設權限頁面_角色區塊_新增按鈕
    def btn_more_default_role(self):
        return self.page.locator('[formarrayname="roles"] .cursor-pointer')

    @property
    #  權限設定_預設權限分頁_新增預設權限頁面_範圍區塊_新增按鈕
    def btn_more_default_scope(self):
        return self.page.locator('[formarrayname="scopes"] .cursor-pointer')
    
    @property
    #  權限設定_預設權限分頁_新增預設權限頁面_新增角色清單
    def list_default_role(self):
        return self.page.locator('[formarrayname="roles"] app-custom-form-field app-select')

    @property
    #  權限設定_預設權限分頁_新增預設權限頁面_新增範圍清單
    def list_default_scope(self):
        return self.page.locator('[formarrayname="scopes"] app-custom-form-field app-select')

    @property
    #  權限設定_預設權限分頁_垃圾桶
    def bin_default_permission(self):
        return self.page.locator('app-icon[class="cursor-pointer"]')