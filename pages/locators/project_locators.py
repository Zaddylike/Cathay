from pages.locators.elements_base import ElementsBase


class ProjectLocators(ElementsBase):

#   Create Project

    @property
    # 專案總覽頁面_新增專案按鈕
    def btn_create_project(self):
        return self.page.locator(".function-bar").get_by_role("button", name="新增專案", exact=True)
    

    @property
    # 新增專案頁面_專案縮寫欄位
    def input_project_abbr(self):
        return self.page.locator('input[formcontrolname="nameAbbr"]')
    

    @property
    # 新增專案頁面_專案中文
    def input_project_nameZh(self):
        return self.page.locator('input[formcontrolname="nameCn"]')

    @property
    # 新增專案頁面_專案英文
    def input_project_nameEn(self):
        return self.page.locator('input[formcontrolname="nameEn"]')

    @property
    # 新增專案頁面_專案標籤
    def input_project_tag(self):
        return self.page.locator('input[formcontrolname="tag"]')

    @property
    # 新增專案頁面_專案標籤新增按鈕
    def btn_project_tag(self):
        return self.page.locator('[tooltipposition="bottom"]>div>button')
    
    @property
    # 新增專案頁面_專案描述
    def input_project_description(self):
        return self.page.locator('textarea[formcontrolname="description"]')

#   Project Detail

    @property
    # 專案資訊頁面_返回箭頭
    def arrow_go_back(self):
        return self.page.locator('[class="go-back-btn__icon"]')
    
    @property
    # 專案資訊頁面_返回專案總覽
    def btn_back_to_overview(self):
        return self.page.get_by_text(" 返回專案總覽 ")
    
    @property
    # 專案資訊頁面_編輯專案按鈕
    def btn_edit_project(self):
        return self.page.get_by_text("編輯專案")
    
    @property
    # 專案資訊頁面_刪除專案按鈕
    def btn_delete_project(self):
        return self.page.get_by_text("刪除專案")    
    
    @property
    # 專案頁面_編輯成員按鈕
    def btn_project_edit_member(self):
        return self.page.get_by_role("button", name="編輯成員", exact=True)

    @property
    # 專案成員頁面_編輯成員按鈕
    def btn_member_edit_member(self):
        return (
            self.page.locator("app-share-project")
            .get_by_role("button", name="編輯成員", exact=True)
            .first
        )

#   Member Page

    @property
    # 專案成員頁面_返回專案總覽
    def btn_back_to_imformation(self):
        return self.page.get_by_text(" 返回專案資訊 ")

    @property
    # 專案成員新增頁面_成員名單_篩選清單_編輯者
    def btn_memberadd_filter_level_editor(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text(" 編輯者 ",exact=True))

    @property
    # 專案成員新增頁面_成員名單_篩選清單_擁有者
    def btn_memberadd_filter_level_owner(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text(" 擁有者 ",exact=True))

    @property
    # 專案成員新增頁面_成員名單_篩選清單_檢視者
    def btn_memberadd_filter_level_viewer(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text(" 檢視者 ",exact=True))
