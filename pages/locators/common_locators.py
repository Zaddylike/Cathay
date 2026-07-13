from playwright.sync_api import Page

class CommonLocators:
    def __init__(self, page: Page):
        self.page = page

    # Login / Logo

    @property
    # 登入按鈕, 撈重複多再篩內部有符合的抓
    def btn_login(self):
        return self.page.locator('.header__feature-item', has=self.page.get_by_role("button", name="登入", exact=True))

    @property
    # 登入頁_登入按鈕, 先抓指定區域再從中有符合的抓
    def btn_login_welcome(self):
        return self.page.locator('[method="post"]').get_by_role("button", name="登入", exact=True)

    @property
    # Entra登入頁面_下一步按鈕
    def btn_login_nextStep(self):
        return self.page.locator("#idSIButton9")

    @property
    # 登入後頁面_使用者頭像
    def btn_user_avatar(self):
        return self.page.locator(".header__feature p-splitbutton button.p-splitbutton-dropdown")
<<<<<<< HEAD
=======

#   極常出現

    @property
    #  loading icon
    def icon_loading(self):
        return self.page.locator('.loading__main')

>>>>>>> origin/temp

    # Common Fields / Buttons

    @property
    # 下一步按鈕
    def btn_next_step(self):
        return self.page.get_by_role("button", name="下一步", exact=True)

    @property
    # All_送出字樣按鈕
    def btn_submit(self):
        return self.page.get_by_role("button", name="送出")

    @property
    # All_展開新增頁面箭頭
    def arrow_extend_page(self):
        return self.page.locator('.border-circle')

    @property
    # 專案總覽_卡片、清單按鈕的儀表板
    def dashboard_type_projects(self):
        return self.page.locator('.function-bar .btn').nth(0)

    @property
    # 專案總覽_列表模式
    def btn_projet_type_list(self):
        return self.page.locator('.function-bar .btn div').nth(1)

    @property
    # 專案總覽_卡片模式
    def btn_projet_type_card(self):
        return self.page.locator('.function-bar .btn div').nth(0)

    @property
    # 行星圖像
    def img_planets(self):
        return self.page.locator(".planets-icon-box")

    # Create Buttons

    @property
    # 新增設定筆數的按鈕
    def btn_create_more(self):
        return self.page.locator('[tooltipposition="bottom"] p', has=self.page.get_by_text(" 新增 ", exact=True))

    # Search / Filter

    @property
    # 篩選面板_共用[請輸入關鍵字]的搜尋欄
    def input_keyword_search(self):
        return self.page.get_by_placeholder("請輸入關鍵字", exact=True)

    @property
    # 篩選面板_篩選條件設定按鈕
    def btn_filter_condition_page(self):
        return self.page.locator('p-iconfield p-inputicon.cursor-pointer [tooltipstyleclass="custom-form-field-tooltip"]')

    @property
    # 篩選面板_設定篩選條件頁面
    def page_filter_condition(self):
        return self.page.locator('[role="dialog"] .p-popover-content')

    @property
    # 篩選面板_狀態_全部
    def btn_filter_status_All(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text("全部", exact=True))

    @property
    # 篩選面板_狀態_停用
    def btn_filter_status_disable(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="停用", exact=True)

    @property
    # 篩選面板_狀態_啟用
    def btn_filter_status_enable(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option .flex', has=self.page.get_by_role("button", name="啟用", exact=True))
        # return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="啟用", exact=True)

    @property
    # 篩選面板_日期排序_由新至舊
    def btn_filter_date_grewup(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由新至舊 ", exact=True)

    @property
    # 篩選面板_日期排序_由舊至新
    def btn_filter_date_reyoung(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由舊至新 ", exact=True)

    @property
    # 篩選面板_底部_搜尋按鈕
    def btn_filter_footer_search(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns button', has=self.page.get_by_text(" 搜尋 ", exact=True))

    @property
    # 篩選面板_底部_清除搜尋按鈕
    def btn_filter_footer_clearfilter(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns button', has=self.page.get_by_text(" 清除搜尋 ", exact=True))

    @property
    # 篩選面板_查無資料時的清除搜尋按鈕
    def btn_filter_clear_noResult(self):
        return self.page.locator('.btn--secondary', has_text=" 清除搜尋 ")

    @property
    # 篩選面板_清除關鍵字按鈕
    def btn_filter_clear_search(self):
        return self.page.locator(".function-bar .relative p-inputicon.cursor-pointer img").first

    # Dialog / Confirm

    @property
    # 對話視窗_彈窗頁面
    def page_dialog(self):
        return self.page.locator('[role="dialog"]')

    @property
    # 對話視窗_確認按鈕
    def btn_dialog_checked(self):
        return self.page.locator('[role="dialog"] app-prompt-dialog .prompt-dialog__footer')

    @property
    # 刪除對話視窗_確認按鈕
    def btn_dialog_delete_confirm(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 確認 ")

    @property
    # 刪除對話視窗_取消按鈕
    def btn_dialog_delete_cancel(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 取消 ")

    @property
    # S2S, SSO 新增視窗的權限設定按鈕
    def btn_dialog_permission_confirm(self):
        return self.page.locator('[role="dialog"] .prompt-dialog__footer', has=self.page.get_by_role("button", name=" 權限設定 ", exact=True))

    # Date Picker

    @property
    # 日期選擇視窗面板
    def date_picker_panel(self):
        return self.page.locator('.p-datepicker-panel [data-pc-section="calendarcontainer"]')

    @property
    # 生效日期選擇欄位
    def date_picker_startDate(self):
        return self.page.locator('p-datepicker[formcontrolname="startDate"]')

    @property
    # 到期日期選擇欄位
    def date_picker_endDate(self):
        return self.page.locator('p-datepicker[formcontrolname="endDate"]')

    @property
    # 日期選擇視窗面板_上一個月箭頭
    def dete_picker_arrow_previous(self):
        return self.page.locator('.p-datepicker-panel [data-pc-section="calendarcontainer"] .p-datepicker-header [severity="secondary"]').nth(0)

    @property
    # 日期選擇視窗面板_下一個月箭頭
    def dete_picker_arrow_next(self):
        return self.page.locator('.p-datepicker-panel [data-pc-section="calendarcontainer"] .p-datepicker-header [severity="secondary"]').nth(1)

    @property
    # 日期選擇視窗面板_日期按鈕
    def date_picker_day(self):
        return self.page.locator(f'.p-datepicker-panel [data-pc-section="calendarcontainer"] .p-datepicker-calendar [data-pc-section="tablebody"] [data-pc-section="tablebodyrow"] .p-datepicker-day-cell')

    # Cards / Options

    @property
    # All_清單
    def list_dropdown(self):
        return self.page.locator('[role="combobox"]')

    @property
    # All_下拉選單內的選項
    def option_dropdown_list(self):
        return self.page.locator('[role="option"]')

    @property
    # All_下拉選單內的選項
    def option_dropdown_list_checked(self):
        return self.page.locator('[role="option"][data-p-disabled="true"]')
    
    @property
    # All_下拉選單內的選項
    def option_dropdown_list_avail(self):
        return self.page.locator('[role="option"][data-p-disabled="false"]')

    @property
    # 專案, 權限設定內的項目
    def option_cards(self):
        return self.page.locator(".data-card")
    @property
    # 權限設定_預設權限的項目
    def option_assign(self):
        return self.page.locator('.data-card--permission')
    @property
    # 權限設定_預設權限的項目
    def option_permissions(self):
        return self.page.locator('[role="rowgroup"][data-pc-section="tbody"] tr')

    # Member Common

    @property
    # 專案成員頁面內的項目
    def option_cards_members(self):
        return self.page.locator('[datakey="memberId"] tbody')

    @property
    # 新增專案成員頁面內的權限清單按鈕
    def btn_memberadd_add_member_levellist(self):
        return self.page.locator('.flex-column app-select p-select [role="button"]').first

    @property
    # 新增專案成員頁面內的權限清單
    def page_members_level_list_select(self):
        return self.page.locator('.p-select-list-container .p-select-list')

    @property
    # 新增專案成員頁面內的權限清單的選項 - owner
    def option_members_level_list_owner(self):
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="OWNER"]')

    @property
    # 新增專案成員頁面內的權限清單的選項 - editor
    def option_members_level_list_editor(self):
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="EDITOR"]')

    @property
    # 新增專案成員頁面內的權限清單的選項 - viewer
    def option_members_level_list_viewer(self):
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="VIEWER"]')

    @property
    # 成員搜尋頁面_篩選成員彈窗_篩選欄位
    def input_memberadd_advanced_search(self):
        return self.page.get_by_placeholder("請輸入部門/姓名", exact=True)

    @property
    # 成員搜尋頁面_checkbox最後一個
    def checkbox_add_member(self):
        return self.page.locator('[role="treeitem"] p-checkbox .p-checkbox-input').last
