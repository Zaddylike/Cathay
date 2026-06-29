from playwright.sync_api import Page


class CommonLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def btn_login(self):
        # 首頁: 登入按鈕
        return self.page.get_by_role("button", name="登入", exact=True)
    
    @property
    def btn_login_nextStep(self):
        # 登入頁面: 下一步按鈕
        return self.page.locator("#idSIButton9")

    @property
    def btn_nextStep(self):
        # 登入頁面: 下一步按鈕
        return self.page.get_by_text(" 下一步")

    @property
    def input_member_search(self):
        # 共用篩選搜尋欄, project, project member, project member add
        return self.page.get_by_placeholder("請輸入關鍵字", exact=True)   

    @property
    def btn_clear_noResult(self):
        # 清除搜尋按鈕
        return self.page.locator('.btn--secondary', has_text=" 清除搜尋 ")

    @property
    def btn_clear_search(self):
        # 清除關鍵字按鈕
        return self.page.locator(".function-bar .relative p-inputicon.cursor-pointer img").first

    @property
    def btn_dialog_checked(self):
        # 異動通知確認按鈕, 確認
        return self.page.locator('[role="dialog"] app-prompt-dialog .prompt-dialog__footer')
    
    @property
    def btn_dialog_footer_filter_search(self):
        # 篩選框內搜尋按鈕
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns button', has=self.page.get_by_text(" 搜尋 ", exact=True))

    @property
    def btn_dialog_footer_filter_clear(self):
        # 篩選框內清除搜尋按鈕
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns button', has=self.page.get_by_text(" 清除搜尋 ", exact=True))

    @property
        # 篩選條件設定按鈕
    def btn_filter_search(self):
        return self.page.locator('p-iconfield p-inputicon.cursor-pointer')
    
    @property
    def btn_filter_status_all(self):
        # 篩選條件: 全部
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option div button', has=self.page.get_by_text("全部", exact=True))

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
    def btn_submit(self):
        return self.page.locator('div.footer').get_by_role("button", name="送出")

    @property
    def btn_tag(self):
        return self.page.locator('[tooltipposition="bottom"]>div>button')

    @property
    def btn_user_avatar(self):
        return self.page.locator(".header__feature p-splitbutton button.p-splitbutton-dropdown")
    

    @property
    def checkbox_add_member(self):
        return self.page.locator('[role="treeitem"] p-checkbox .p-checkbox-input').last

    @property
    def dialog_btn_confirm(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 確認 ")

    @property
    def dialog_page(self):
        # 任何_彈窗頁面
        return self.page.locator('[role="dialog"]')
    
    @property
    def btn_dialog_cancel(self):    
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 取消 ")
    
    @property
    def dialog_project_filter(self):
        return self.page.locator('[role="dialog"] .p-popover-content')

    @property
    def dialog_success(self):
        return self.page.locator('[role="dialog"] app-prompt-dialog')

    @property
    def img_planets(self):
        return self.page.locator(".planets-icon-box")
    
    @property
    def input_search_project(self):
        return self.page.locator(".function-bar .relative input")

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
    def list_project_members(self):
        return self.page.locator('[datakey="memberId"] tbody')

    @property
    def list_projects(self):
        return self.page.locator(".data-card").first

    @property
    def list_search_member(self):
        return self.page.locator('[role="listbox"] [role="option"] p-checkbox')

    @property
    def list_transform(self):
        return self.page.locator('.function-bar .btn').nth(0)

    @property
    def logo_google(self):
        return self.page.locator(".logo")
    

    @property
    def logo_omni(self):
        return self.page.locator(".header__logo")
    

    @property
    def msg_field_error(self):
        # 欄位錯誤訊息
        return self.page.locator('app-error-message.ng-star-inserted div span')

    @property
    def msg_search_noResult(self):
        return self.page.locator(".text-type--secondary-title")
