from playwright.sync_api import Page, expect
from pages.locators.elements import ScopeElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage
import allure


class ScopePage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ScopeElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    # create
    @allure.step("Open create scope dialog")
    def click_to_create_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.base_page.click_expect(self.elements.btn_create_scope)
        expect(self.elements.input_scope_code).to_be_visible()

    @allure.step("Validate and fill scope code")
    def validate_and_fill_scope_code(self):
        self.input_code_cases = [
            ("中文", "只允許半形之英數字及符號：_-."),
            ("", "必填欄位"),
            ("$$$", "只允許半形之英數字及符號：_-."),
            ("ＡＢＣ", "只允許半形之英數字及符號：_-."),
            ("  ", "只允許半形之英數字及符號：_-."),
            ("#" * 21, "輸入字數超過限制長度20"),
        ]
        element_input = self.elements.input_scope_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_code_cases)
        self.elements.input_scope_code.fill("e2e-scope-code")

    @allure.step("Validate and fill scope name")
    def validate_and_fill_scope_name(self):
        self.input_name_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("  ", "必填欄位"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_scope_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_scope_name.fill("e2e-scope-name")

    @allure.step("Validate and fill scope description")
    def validate_and_fill_scope_description(self):
        self.input_description_cases = [
            ("#" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_scope_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_scope_description.fill("e2e-scope-description")

    @allure.step("Submit scope and verify created")
    def validate_duplicate_scope(self):
        self.elements.btn_scope_add_more_scope.click()

        self.input_scope_cases = [
            ("e2e-scope-code", " 代碼不可重複 "),
        ]
        self.operate_page.verify_input(self.elements.input_scope_code.last, self.elements.msg_field_error, self.input_scope_cases)

    @allure.step("Create another scope")
    def create_another_scope(self):
        self.elements.input_scope_code.last.fill("e2e-scope-code-2")
        if ( self.elements.input_permission_init_scope_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()
        self.elements.input_scope_name.last.fill("e2e-scope-name-2")
        self.elements.input_scope_description.last.fill("e2e-scope-description-2")
    
    @allure.step("Submit scope and verify created")
    def submit_and_verify_created(self):
        self.elements.btn_submit.click()
        expect(self.elements.dialog_page).to_be_visible()
        self.elements.btn_dialog_checked.click()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.elements.input_keyword_search.fill("e2e-scope-code")
        expect(self.elements.card_permission_scope.first).to_be_visible()

    # read


    # update
    @allure.step("Open create scope dialog")
    def click_to_update_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.elements.input_keyword_search.fill("e2e-scope-code")
        self.base_page.click_expect(self.elements.threepoint_menu.last)
        expect(self.elements.page_threepoint_menu).to_be_visible()
        self.base_page.click_expect(self.elements.btn_menu_update)

    @allure.step("Validate and update scope name")
    def validate_and_update_scope_name(self):
        self.input_name_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("  ", "必填欄位"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_scope_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_scope_name.fill("e2e-scope-name-edit")

    @allure.step("Validate and update scope description")
    def validate_and_update_scope_description(self):
        self.input_description_cases = [
            ("#" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_scope_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_scope_description.fill("e2e-scope-description-edit")

    @allure.step("update scope status")
    def disable_scope_status(self):
        self.elements.radio_status_disable.click()

    @allure.step("Submit scope and verify updated")
    def submit_and_verify_updated(self):
        self.elements.btn_submit.click()
        expect(self.elements.dialog_page).to_be_visible()
        self.elements.btn_dialog_checked.click()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.elements.input_keyword_search.fill("e2e-scope-code-edit")
        expect(self.elements.card_permission_scope.first).to_be_visible()

    # delete
    @allure.step("Open scope delete dialog")
    def open_scope_delete_dialog(self):
        pass

    @allure.step("Verify delete confirm disabled by default")
    def verify_delete_confirm_disabled_by_default(self):
        pass

    @allure.step("Cancel scope delete then reopen")
    def cancel_scope_delete_then_reopen(self):
        pass

    @allure.step("Confirm scope delete")
    def confirm_scope_delete(self):
        pass

    @allure.step("Verify scope deleted")
    def verify_scope_deleted(self):
        pass

    # copy
    @allure.step("Open scope copy dialog")
    def open_scope_copy_dialog(self):
        pass

    @allure.step("Validate and fill copied scope code")
    def validate_and_fill_copied_scope_code(self):
        pass

    @allure.step("Validate and fill copied scope name")
    def validate_and_fill_copied_scope_name(self):
        pass

    @allure.step("Submit scope copy and verify")
    def submit_scope_copy_and_verify(self):
        pass
