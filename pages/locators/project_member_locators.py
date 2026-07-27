from pages.locators.elements_base import ElementsBase


class ProjectMemberLocators(ElementsBase):

#   Member Page Navigation

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

#   Add Member

    @property
    # 專案成員新增頁面_新增成員按鈕
    def btn_memberadd_add_member(self):
        return self.page.locator('div.main-container--wrapper app-share-project-edit div button.btn', has=self.page.get_by_text(" 新增成員 ", exact=True))

    @property
    # 專案成員新增頁面_篩選成員欄位
    def input_search_member_field(self):
        return self.page.locator(".w-full .w-full p-multiselect .p-multiselect-label-container .p-multiselect-label").first

#   Member Level

    @property
    # 專案成員新增頁面_新增篩選欄位_權限清單_編輯者
    def option_cards_member_as_editor(self):
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="EDITOR"]')

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

#   Existing Member

    @property
    # 專案成員新增頁面_成員名單_測試資料
    def list_editmember_tester3(self):
        return self.page.locator('[datakey="memberId"] tbody tr', has_text = " 測試人員3 ")
