from playwright.sync_api import Page

class AssignPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    # Entry / Page

    @property
    # 身分驗證頁面_分頁_權限分配
    def tab_permission_assign(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(2)')

    @property
    # 權限分配頁面_新增權限分配按鈕
    def btn_create_assign_permission(self):
<<<<<<< HEAD
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    # Create Assignment

    @property
    # 權限分配頁面_新增權限分配頁面_新增按鈕
    def btn_add_assign_permission(self):
        return self.page.locator("app-permission-assignment button, app-assign-permission button").first
=======
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button', has=self.page.get_by_text(' 新增指定權限 '))
>>>>>>> origin/temp

    @property
    # 權限分配頁面_新增權限分配頁面_成員搜尋按鈕
    def btn_assign_member_search(self):
        return self.page.locator('[formarrayname="assigns"] .cursor-pointer')

    @property
    def btn_more_permission(self):
        return self.page.locator('[formarrayname="assigns"] app-custom-form-field .cursor-pointer app-icon')

    @property
    # 權限分配頁面_新增權限分配頁面_角色清單
    def list_assign_permission_role(self):
        return self.page.locator('[formarrayname="assigns"] [formcontrolname="id"]')

    @property
    # 權限分配頁面_新增權限分配頁面_範圍清單
    def list_assign_permission_scope(self):
        return self.page.locator('[formarrayname="assigns"] [formcontrolname="id"]')

    @property
    def list_assign_edit_permission_role(self):
        return self.page.locator('app-permission-assign [formcontrolname="id"]')

    @property
    def list_assign_edit_permission_scope(self):
        return self.page.locator('app-permission-assign [formcontrolname="id"]')



    @property
    # 權限分配頁面_新增權限分配頁面_描述
    def input_assign_permission_description(self):
        return self.page.locator('[formcontrolname="remark"]')

    @property
    #
    def btn_assign_create_more_assign(self):
        return self.page.locator('app-permission-assign button')