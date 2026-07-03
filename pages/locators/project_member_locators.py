from playwright.sync_api import Page

class ProjectMemberLocators:
    def __init__(self, page: Page):
        self.page = page

    # Member Page Navigation

    @property
    # 專案頁面_編輯成員按鈕
    def btn_project_edit_member(self):
        return self.page.get_by_text("編輯成員").first

    @property
    # 專案成員頁面_編輯成員按鈕
    def btn_member_edit_member(self):
        return self.page.locator("div.main-container--wrapper.ng-star-inserted > app-share-project > div > button")

    # Add Member

    @property
    # 專案成員新增頁面_新增成員按鈕
    def btn_memberadd_add_member(self):
        return self.page.locator('div.main-container--wrapper app-share-project-edit div button.btn', has=self.page.get_by_text(" 新增成員 ", exact=True))

    @property
    # 專案成員新增頁面_新增篩選欄位_篩選條件按鈕
    def btn_memberadd_filter_add_search(self):
        return self.page.locator('p-iconfield p-inputicon.cursor-pointer').first

    @property
    # 專案成員新增頁面_篩選成員彈窗_篩選欄位
    def input_memberadd_member_search(self):
        return self.page.get_by_placeholder("請輸入部門/姓名", exact=True)    
    

    @property
    # 專案成員新增頁面_篩選成員欄位
    def input_search_member_field(self):
        return self.page.locator(".w-full .w-full p-multiselect .p-multiselect-label-container .p-multiselect-label").first

    # Member Level

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

    # Existing Member

    @property
    # 專案成員新增頁面_成員名單_測試資料
    def list_editmember_tester3(self):
        return self.page.locator('[datakey="memberId"] tbody tr', has_text = " 測試人員3 ")
