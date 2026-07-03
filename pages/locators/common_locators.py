from playwright.sync_api import Page

class CommonLocators:
    def __init__(self, page: Page):
        self.page = page


    # 未登入頁面、登入頁、Omni Logo

    @property
    # 登入按鈕, 撈重複多再篩內部有符合的抓
    def btn_login(self):
        return self.page.locator('.header__feature-item', has=self.page.get_by_role("button", name="登入", exact=True))
    
    @property
    # 登入頁: 登入按鈕, 先抓指定區域再從中有符合的抓
    def btn_login_welcome(self):
        return self.page.locator('[method="post"]').get_by_role("button", name="登入", exact=True)
    
    @property
    # Entra登入頁面: 下一步按鈕
    # Entra登入頁面: 下一步按鈕
    def btn_login_nextStep(self):
        return self.page.locator("#idSIButton9")
    
    @property
    # 登入後頁面_使用者頭像
    def btn_user_avatar(self):
        return self.page.locator(".header__feature p-splitbutton button.p-splitbutton-dropdown")
    

    # Common Actions

    @property
    # 下一步按鈕
    def btn_next_step(self):
        return self.page.get_by_role("button", name="下一步", exact=True)


    # 常用欄位、按鈕

    @property
    #All_送出字樣按鈕
    def btn_submit(self):
        return self.page.get_by_role("button", name="送出")

    @property
    #All_展開新增頁面箭頭
    def arrow_extend_page(self):
        return self.page.locator('.border-circle')

    @property
    # 
    def list_transform(self):
        return self.page.locator('.function-bar .btn').nth(0)

    # Search / Filter

    @property
    # 篩選面板_共用[請輸入關鍵字]的搜尋欄
    def input_keyword_search(self):
        return self.page.get_by_placeholder("請輸入關鍵字", exact=True)   

    @property
    # 篩選面板_篩選條件設定按鈕
    def btn_filter_condition_page(self):
        return self.page.locator('p-iconfield p-inputicon.cursor-pointer')

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
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="啟用", exact=True)

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
    # 對話視窗_異動通知的確認按鈕
    def btn_dialog_checked(self):
        return self.page.locator('[role="dialog"] app-prompt-dialog .prompt-dialog__footer')

    @property
    # 刪除對話視窗_確認按鈕
    def btn_dialog_delete_confirm(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 確認 ")

    @property
    # 刪除對話視窗_確認按鈕
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
    

    # Shared Lists / Options

    @property
    # All_下拉選單內的選項
    def option_unit(self):
        return self.page.locator('[role="option"]')

    @property
    # 
    def list_transform(self):
        return self.page.locator('.function-bar .btn').nth(0)

    @property
    def list_projects(self):
        return self.page.locator(".data-card").first

    @property
    def list_project_members(self):
        return self.page.locator('[datakey="memberId"] tbody')

    @property
    def list_project_member_add_levellist(self):
        return self.page.locator('.p-select-list-container .p-select-list')

    @property
    def list_project_member_add_owner(self):
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="OWNER"]')

    @property
    def list_project_member_add_viewer(self):
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="VIEWER"]')

    @property
    def list_search_member(self):
        return self.page.locator('[role="listbox"] [role="option"] p-checkbox')

    # Member Common

    @property
    def checkbox_add_member(self):
        return self.page.locator('[role="treeitem"] p-checkbox .p-checkbox-input').last

    @property
    def btn_memberadd_add_member_cancel(self):
        return self.page.locator('[role="dialog"] .justify-content-center').get_by_text(" 取消 ")

    @property
    def btn_memberadd_filter_add_search_confirm(self):
        return self.page.locator('[role="dialog"] .justify-content-center').get_by_text(" 確認 ")

    @property
    def btn_memberadd_add_member_levellist(self):
        return self.page.locator('.flex-column app-select p-select [role="button"]').first

    @property
    # _篩選成員彈窗_篩選欄位
    def input_member_advanced_search(self):
        return self.page.get_by_placeholder("請輸入部門/姓名", exact=True)    
    

    # Permission Common

    @property
    # 身分驗證頁面_分頁_權限設定
    def tab_permission(self):
        return self.page.locator('[role="tablist"] p-tab', has_text=" 權限設定 ")
    

    @property
    # 身分驗證頁面_logo
    def page_permission(self):
        return self.page.locator(".text-type--content-title")
    

    @property
    # 身分驗證頁面_分頁_權限設定_範圍卡片
    def card_permission_scope(self):
        return self.page.locator("app-permission-card")
    

    @property
    #
    def threepoint_menu(self):
        return self.page.locator('app-permission-card  .p-splitbutton-dropdown')
    

    @property
    #
    def page_threepoint_menu(self):
        return self.page.locator('[role="menu"]')

    @property
    #
    def btn_menu_update(self):
        return self.page.locator('[role="menu"] [role="menuitem"]').get_by_text('編輯', exact=True)

    @property
    #
    def btn_menu_copy(self):
        return self.page.locator('[role="menu"] [role="menuitem"]').get_by_text('複製', exact=True)
    

    @property
    #
    def btn_menu_delete(self):
        return self.page.locator('[role="menu"] [role="menuitem"]').get_by_text('刪除', exact=True)

    # Status Controls

    @property
    # 新增專案頁面_狀態_停用
    def radio_status_disable(self):
        return self.page.get_by_text("停用")

    @property
    # 新增專案頁面_狀態_啟用
    def radio_status_enable(self):
        return self.page.get_by_text("啟用")
    
        

    # Messages / Visuals

    @property
    def img_planets(self):
        return self.page.locator(".planets-icon-box")
    

    @property
    # 欄位錯誤訊息
    def msg_field_error(self):
        return self.page.locator('app-error-message.ng-star-inserted div span')

    @property
    def msg_search_noResult(self):
        return self.page.locator(".text-type--secondary-title")
