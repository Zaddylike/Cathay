from playwright.sync_api import Page

class AssignPermissionLocators:
    def __init__(self, page: Page):
        self.page = page

    # Entry / Page

    @property
    # 身分驗證頁面_分頁_權限分配
    def tab_permission_assign(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper:nth-child(6)')

    @property
    # 權限分配頁面_新增權限分配按鈕
    def btn_create_assign_permission(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button')

    # Create Assignment

    @property
    # 權限分配頁面_新增權限分配頁面_新增按鈕
    def btn_add_assign_permission(self):
        return self.page.locator("app-permission-assignment button, app-assign-permission button").first

    @property
    # 權限分配頁面_新增權限分配頁面_成員搜尋按鈕
    def btn_assign_member_search(self):
        return self.page.locator('p-iconfield p-inputicon.cursor-pointer').first

    @property
    # 權限分配頁面_新增權限分配頁面_角色清單
    def list_assign_permission_role(self):
        return self.page.locator('[formcontrolname="id"]').first

    @property
    # 權限分配頁面_新增權限分配頁面_範圍清單
    def list_assign_permission_scope(self):
        return self.page.locator('[formcontrolname="id"]').last

    @property
    # 權限分配頁面_新增權限分配頁面_描述
    def input_assign_permission_description(self):
        return self.page.locator('[formcontrolname="remark"]')
