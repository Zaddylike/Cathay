from playwright.sync_api import Page


class CommonLocators:
    def __init__(self, page: Page):
        self.page = page


    @property
    def btn_clear_noResult(self):
        return self.page.locator('.btn--secondary')

    @property
    def btn_clear_search(self):
        return self.page.locator(".function-bar .relative p-inputicon.cursor-pointer img").first

    @property
    def btn_delete_project(self):
        return self.page.get_by_text("刪除專案")    

    @property
    def btn_dialog_checked(self):
        return self.page.locator('[role="dialog"] app-prompt-dialog .prompt-dialog__footer')

    @property
    def btn_dialog_project_filter_search(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns').get_by_role("button", name=" 搜尋 ", exact=True)

    @property
    def btn_editmember_edit_project_member(self):
        return self.page.locator('div.main-container--wrapper app-share-project div button.btn').first

    @property
    def btn_filter_clean_filter(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__btns').get_by_role("button", name=" 清除搜尋 ", exact=True)

    @property
    def btn_filter_level_editor(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="編輯者", exact=True)

    @property
    def btn_filter_level_owner(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="擁有者", exact=True)

    @property
    def btn_filter_level_viewer(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="檢視者", exact=True)

    @property
    def btn_filter_search(self):
        return self.page.locator('.function-bar .relative p-inputicon.cursor-pointer img[tooltipstyleclass="custom-form-field-tooltip"]')

    @property
    def btn_filter_status_all(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="全部", exact=True)

    @property
    def btn_login(self):
        return self.page.get_by_role("button", name="登入", exact=True)
    

    @property
    def btn_login_nextStep(self):
        self.page.get_by_role
        return self.page.locator("#idSIButton9")
    

    @property
    def btn_project_edit_member(self):
        return self.page.get_by_text("編輯成員")

    @property
    def btn_project_member_add(self):
        return self.page.locator('div.main-container--wrapper app-share-project-edit div button.btn').first

    @property
    def btn_project_member_add_cancel(self):
        return self.page.locator('[role="dialog"] .justify-content-center').get_by_text(" 取消 ")

    @property
    def btn_project_member_add_filter(self):
        return self.page.locator('.w-full .relative p-inputicon.cursor-pointer img[tooltipstyleclass="custom-form-field-tooltip"]')

    @property
    def btn_project_member_add_filter_confirm(self):
        return self.page.locator('[role="dialog"] .justify-content-center').get_by_text(" 確認 ")

    @property
    def btn_project_member_add_levellist(self):
        return self.page.locator('.flex-column app-select p-select [role="button"]').first

    @property
    def btn_project_member_edit(self):
        return self.page.get_by_text("編輯成員")

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
        return self.page.locator('[role="dialog"]')

    @property
    def dialog_page_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog')

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
    def input_add_member_search(self):
        return self.page.get_by_placeholder("請輸入部門/姓名", exact=True)    

    @property
    def input_project_abbr(self):
        return self.page.locator('input[formcontrolname="nameAbbr"]')

    @property
    def input_project_description(self):
        return self.page.locator('textarea[formcontrolname="description"]')

    @property
    def input_project_nameEn(self):
        return self.page.locator('input[formcontrolname="nameEn"]')

    @property
    def input_project_nameZh(self):
        return self.page.locator('input[formcontrolname="nameCn"]')

    @property
    def input_project_tag(self):
        return self.page.locator('input[formcontrolname="tag"]')

    @property
    def input_search_member_field(self):
        return self.page.locator(".w-full .w-full p-multiselect .p-multiselect-label-container .p-multiselect-label").first

    @property
    def input_search_project(self):
        return self.page.locator(".function-bar .relative input")

    @property
    def list_editmember_tester3(self):
        return self.page.locator('[datakey="memberId"] tbody tr').filter(has_text = " 測試人員3 ")

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
        return self.page.locator('app-error-message.ng-star-inserted div span')

    @property
    def msg_search_noResult(self):
        return self.page.locator(".text-type--secondary-title")
