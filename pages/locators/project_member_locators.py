from playwright.sync_api import Page


class ProjectMemberLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def btn_project_edit_member(self):
        # 專案頁面_編輯成員按鈕
        return self.page.get_by_text("編輯成員").first

    @property
    def btn_member_edit_member(self):
        # 專案成員頁面_編輯成員按鈕
        return self.page.locator("div.main-container--wrapper.ng-star-inserted > app-share-project > div > button")

    @property
    def btn_memberadd_add_member(self):
        # 專案成員新增頁面_新增成員按鈕
        return self.page.locator('div.main-container--wrapper app-share-project-edit div button.btn', has=self.page.get_by_text(" 新增成員 ", exact=True))

    @property
    def list_project_member_as_editor(self):
        # 專案成員新增頁面_新增篩選欄位_權限清單_編輯者
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="EDITOR"]')

    @property
    def btn_memberadd_filter_level_editor(self):
        # 專案成員新增頁面_成員名單_篩選清單_編輯者
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text(" 編輯者 ",exact=True))

    @property
    def btn_memberadd_filter_level_owner(self):
        # 專案成員新增頁面_成員名單_篩選清單_擁有者
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text(" 擁有者 ",exact=True))

    @property
    def btn_memberadd_filter_level_viewer(self):
        # 專案成員新增頁面_成員名單_篩選清單_檢視者
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text(" 檢視者 ",exact=True))

    @property
    def list_editmember_tester3(self):
        # 專案成員新增頁面_成員名單_測試資料
        return self.page.locator('[datakey="memberId"] tbody tr', has_text = " 測試人員3 ")
    
    @property
    def btn_memberadd_filter_add_search(self):
        # 專案成員新增頁面_新增篩選欄位_篩選條件按鈕
        return self.page.locator('p-iconfield p-inputicon.cursor-pointer').first

    @property
    def input_memberadd_member_search(self):
        # 專案成員新增頁面_篩選成員彈窗_篩選欄位
        return self.page.get_by_placeholder("請輸入部門/姓名", exact=True)    
    
    @property
    def input_search_member_field(self):
        # 專案成員新增頁面_篩選成員欄位
        return self.page.locator(".w-full .w-full p-multiselect .p-multiselect-label-container .p-multiselect-label").first