from playwright.sync_api import Page, expect

class Elements:
    def __init__(self, page: Page):
        self.page = page

    @property
    def btn_login(self):
        return self.page.get_by_role("button", name="登入", exact=True)
    
    @property
    def btn_login_google(self):
        return self.page.locator(".welcome-box__password-login .welcome-box__oauth2-login--only-microsoft .google-login button")
    
    @property
    def btn_login_entra(self):
        return self.page.locator(".welcome-box__password-login .welcome-box__oauth2-login--only-microsoft button").first
    
    @property
    def input_account_entra(self):
        return self.page.get_by_placeholder("someone@example.com")
    
    @property
    def input_account_google(self):
        return self.page.locator("#identifierId")
    
    @property
    def input_password_entra(self):
        return self.page.get_by_placeholder("密碼")
    
    @property
    def input_password_google(self):
        return self.page.locator('input[name="Passwd"]')
    
    @property
    def btn_login_nextStep(self):
        self.page.get_by_role
        return self.page.locator("#idSIButton9")
    
    @property
    def logo_google(self):
        return self.page.locator(".logo")
    
    @property
    def logo_entra(self):
        return self.page.locator(".logo")
    
    @property
    def input_account(self):
        return self.page.get_by_placeholder("請輸入帳號")
    
    @property
    def input_password(self):
        return self.page.get_by_placeholder("請輸入密碼")
    
    @property
    def btn_user_avatar(self):
        return self.page.locator(".header__feature p-splitbutton button.p-splitbutton-dropdown")
    
    @property
    def btn_logout(self):
        return self.page.locator(".account-action").get_by_text("登出", exact=True)
    
    @property
    def logo_omni(self):
        return self.page.locator(".header__logo")
    
    @property
    def language_arrow(self):
        return self.page.locator(".header .language")
    
    @property
    def language_list(self):
        return self.page.locator(".language .language__dropdown")
    
    @property
    def language_option_en(self):
        return self.page.locator(".language .language__dropdown-item").get_by_text("EN", exact=True)
    
    @property
    def language_option_zh(self):
        return self.page.locator(".language .language__dropdown-item").get_by_text("繁中", exact=True)
    
    #project
    @property
    def btn_create_project(self):
        return self.page.locator(".function-bar").get_by_role("button", name="新增專案", exact=True)
    @property
    def input_nameAbbr(self):
        return self.page.locator('input[formcontrolname="nameAbbr"]')
    @property
    def input_nameZh(self):
        return self.page.locator('input[formcontrolname="nameCn"]')
    @property
    def input_nameEn(self):
        return self.page.locator('input[formcontrolname="nameEn"]')
    @property
    def input_tag(self):
        return self.page.locator('input[formcontrolname="tag"]')
    @property
    def btn_tag(self):
        return self.page.locator('[tooltipposition="bottom"]>div>button')
    @property
    def input_description(self):
        return self.page.locator('textarea[formcontrolname="description"]')
    @property
    def msg_error(self):
        return self.page.locator('app-error-message.ng-star-inserted div span')
    @property
    def btn_submit(self):
        return self.page.locator('div.footer').get_by_role("button", name="送出")
    @property
    def dialog_page(self):
        return self.page.locator('[role="dialog"]')
    @property
    def dialog_page_filter(self):
        return self.page.locator('[role="dialog"] .p-popover-content')
    @property
    def dialog_page_success(self):
        return self.page.locator('[role="dialog"] app-prompt-dialog')
    @property
    def dialog_btn_checked(self):
        return self.page.locator('[role="dialog"] app-prompt-dialog .prompt-dialog__footer')
    @property
    def dialog_page_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog')
    @property
    def dialog_input_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__body input')
    @property
    def dialog_btn_confirm(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 確認 ")
    @property
    def dialog_btn_cancel(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 取消 ")
    @property
    def input_search_field(self):
        return self.page.locator(".function-bar .relative input")
    @property
    def list_project_member(self):
        return self.page.locator('[datakey="memberId"] tbody')
    @property
    def msg_search_nodata(self):
        return self.page.locator(".text-type--secondary-title")
    @property
    def btn_clean_search(self):
        return self.page.locator(".function-bar .relative p-inputicon.cursor-pointer img").first
    @property
    def btn_filter_page(self):
        return self.page.locator('.function-bar .relative p-inputicon.cursor-pointer img[tooltipstyleclass="custom-form-field-tooltip"]')
    @property
    def btn_clean_nodata(self):
        return self.page.locator('.btn--secondary')
    @property
    def cards_project(self):
        return self.page.locator(".data-card")
    @property
    def btn_edit(self):
        return self.page.get_by_text("編輯專案")
    @property
    def btn_delete(self):
        return self.page.get_by_text("刪除專案")    
    @property
    def btn_member(self):
        return self.page.get_by_text("編輯成員")
    @property
    def btn_back_to_overview(self):
        return self.page.get_by_text(" 返回專案總覽 ")
    @property
    def btn_status_disable(self):
        return self.page.get_by_text("停用")
    @property
    def btn_status_enable(self):
        return self.page.get_by_text("啟用")
    @property
    def btn_filter_status_all(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="全部", exact=True)
    @property
    def btn_filter_status_disable(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="停用", exact=True)
    @property
    def btn_filter_status_enable(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="啟用", exact=True)
    @property
    def btn_filter_level_owner(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="擁有者", exact=True)
    @property
    def btn_filter_level_editor(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="編輯者", exact=True)
    @property
    def btn_filter_level_viwer(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="檢視者", exact=True)
    @property
    def btn_filter_index_oldtonew(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由舊至新 ", exact=True)
    @property
    def btn_filter_index_newtoold(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由新至舊 ", exact=True)
    @property
    def btn_filter_clean_filter(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns').get_by_role("button", name=" 清除搜尋 ", exact=True)
    @property
    def btn_filter_search(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns').get_by_role("button", name=" 搜尋 ", exact=True)
    @property
    def logo_planets(self):
        return self.page.locator(".planets-icon-box")
    @property
    def dialog_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog')
    @property
    def list_transform(self):
        return self.page.locator('.function-bar .btn').nth(0)
    @property
    def btn_transform_list(self):
        return self.page.locator('.function-bar .btn div').nth(1)
    @property
    def btn_transform_card(self):
        return self.page.locator('.function-bar .btn div').nth(0)
    @property
    def arrow_go_back(self):
        return self.page.locator('[class="go-back-btn__icon"]')