from playwright.sync_api import Page


class GroupLocators:
    def __init__(self, page: Page):
        self.page = page

# Basic

    @property
    # 權限設定頁面_群組
    def tab_permission_group(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) div div.tab--wrapper div', has=self.page.get_by_text("群組"))

    @property
    # 權限設定_群組頁面_群組新增按鈕
    def btn_create_group(self):
        return self.page.locator('[role="tabpanel"]:nth-child(3) .function-bar .function-bar__item:nth-child(3) button', has=self.page.get_by_text("新增群組"))

    @property
    # 權限設定_新增/編輯群組頁面_群組名稱欄位
    def input_group_name(self):
        return self.page.locator('[formcontrolname="name"]')

    @property
    # 權限設定_新增/編輯群組頁面_描述欄位
    def input_group_description(self):
        return self.page.locator('[formcontrolname="description"]')

# Create 

    @property
    # 權限設定_新增群組頁面_新增群組按鈕
    def btn_create_more_group(self):
        return self.page.locator('app-permission-group button.btn', has=self.page.get_by_text("新增群組"))
    
    @property
    # 權限設定_新增群組頁面_搜尋成員_新增成員按鈕
    def btn_group_add_member(self):
        return self.page.locator('app-permission-group app-custom-form-field button').get_by_text("新增成員")