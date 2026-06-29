from playwright.sync_api import Page


class ProjectLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def btn_create_project(self):
        # 專案總覽_新增專案按鈕
        return self.page.locator(".function-bar").get_by_role("button", name="新增專案", exact=True)
    
    @property
    def input_project_abbr(self):
        # 新增專案頁面_專案縮寫欄位
        return self.page.locator('input[formcontrolname="nameAbbr"]')
    
    @property
    def input_project_description(self):
        # 新增專案頁面_專案描述
        return self.page.locator('textarea[formcontrolname="description"]')

    @property
    def input_project_nameEn(self):
        # 新增專案頁面_專案英文
        return self.page.locator('input[formcontrolname="nameEn"]')

    @property
    def input_project_nameZh(self):
        # 新增專案頁面_專案中文
        return self.page.locator('input[formcontrolname="nameCn"]')

    @property
    def input_project_tag(self):
        # 新增專案頁面_專案標籤
        return self.page.locator('input[formcontrolname="tag"]')
    
    @property
    def radio_status_disable(self):
        # 新增專案頁面_狀態_停用
        return self.page.get_by_text("停用")

    @property
    def radio_status_enable(self):
        # 新增專案頁面_狀態_啟用
        return self.page.get_by_text("啟用")

    @property
    def btn_project_edit_member(self):
        # 專案頁面_編輯成員按鈕
        return self.page.get_by_text("編輯成員").first

    @property
    def btn_member_edit_member(self):
        # 專案成員頁面_編輯成員按鈕
        return self.page.locator("div.main-container--wrapper.ng-star-inserted > app-share-project > div > button")

    @property
    def arrow_go_back(self):
        # 專案資訊頁面_返回箭頭
        return self.page.locator('[class="go-back-btn__icon"]')
    
    @property
    def btn_back_to_overview(self):
        # 專案資訊頁面_返回專案總覽
        return self.page.get_by_text(" 返回專案總覽 ")

    @property
    def btn_back_to_imformation(self):
        # 專案資訊頁面_返回專案總覽
        return self.page.get_by_text(" 返回專案資訊 ")
    
    @property
    def btn_card_transtfer_list(self):
        # 專案總覽_列表模式
        return self.page.locator('.function-bar .btn div').nth(1)
    
    @property
    def btn_list_transtfer_card(self):
        # 專案總覽_卡片模式
        return self.page.locator('.function-bar .btn div').nth(0)
    
    @property
    def btn_dialog_project_filter_status_disable(self):
        # 專案總覽_篩選面板_狀態_停用
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="停用", exact=True)

    @property
    def btn_dialog_project_filter_status_enable(self):
        # 專案總覽_篩選面板_狀態_啟用
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="啟用", exact=True)

    @property
    def btn_dialog_project_filter_newtoold(self):
        # 專案總覽_篩選面板_日期排序_由新至舊
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由新至舊 ", exact=True)

    @property
    def btn_dialog_project_filter_oldtonew(self):
        # 專案總覽_篩選面板_日期排序_由舊至新
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由舊至新 ", exact=True)

    @property
    def btn_edit_project(self):
        # 專案資訊頁面_編輯專案按鈕
        return self.page.get_by_text("編輯專案")
    
    @property
    def btn_delete_project(self):
        # 專案資訊頁面_刪除專案按鈕
        return self.page.get_by_text("刪除專案")    
    
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
