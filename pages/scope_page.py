from playwright.sync_api import Page, expect
from pages.locators.elements import ScopeElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage
import allure, re


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
        self.elements.input_scope_code.last.fill("e2e-scope-code2")
        if ( self.elements.input_permission_init_scope_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()
        self.elements.input_scope_name.last.fill("e2e-scope-name2")
        self.elements.input_scope_description.last.fill("e2e-scope-description2")
    
    @allure.step("Submit scope and verify created")
    def submit_and_verify_created(self):
        self.elements.btn_submit.click()
        expect(self.elements.page_dialog).to_be_visible()
        self.elements.btn_dialog_checked.click()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.elements.input_keyword_search.fill("e2e-scope-code")
        self.base_page.take_screenshot("Scope_Create_Success")

    # read

    @allure.step("搜尋框搜尋不存在範圍")
    def search_scope_with_no_result(self):
        self.elements.tab_permission_scope.click()

        self.elements.input_keyword_search.fill("xxxxxxxxxxxx")
        expect(self.elements.msg_search_noResult).to_be_visible()
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("搜尋框搜尋已存在範圍")
    def search_scope_by_code(self):
        self.elements.input_keyword_search.fill("e2e-scope-code")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
        self.elements.input_keyword_search.fill("")

    @allure.step("進階篩選面板篩選狀態")
    def filter_projects_by_status(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_enable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_disable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("進階篩選面板排序日期")
    def sort_projects_by_created_time(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_date_reyoung.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_date_grewup.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()


    # update
    @allure.step("Open update scope dialog")
    def click_to_update_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.elements.input_keyword_search.fill("e2e-scope-code2")
        self.page.mouse.wheel(0, 500)
        self.base_page.sleep(1)
        self.base_page.click_expect(self.elements.btn_card_threepoint_menu.last, self.elements.page_card_threepoint_menu)
        self.base_page.click_expect(self.elements.btn_card_menu_update, reclick=True)

    @allure.step("Validate and update scope name")
    def validate_and_update_scope_name(self):
        self.input_name_cases = [
            ("  ", "必填欄位"),
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_scope_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_scope_name.fill("e2e-scope-name2-edit")

    @allure.step("Validate and update scope description")
    def validate_and_update_scope_description(self):
        self.input_description_cases = [
            ("#" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_scope_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_scope_description.fill("e2e-scope-description2-edit")

    @allure.step("update scope status")
    def disable_scope_status(self):
        self.elements.radio_status_disable.click()

    @allure.step("Submit scope and verify updated")
    def submit_and_verify_updated(self):
        self.base_page.click_expect(self.elements.btn_submit, self.elements.page_dialog)
        self.elements.btn_dialog_checked.click()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.elements.input_keyword_search.fill("e2e-scope-name2-edit")
        expect(self.elements.option_cards.first).to_be_visible()

    # delete
    @allure.step("Open delete scope dialog")
    def click_to_delete_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.elements.input_keyword_search.fill("e2e-scope-code2")
        self.page.mouse.wheel(0, 500)
        self.base_page.sleep(1)
        self.base_page.click_expect(self.elements.btn_card_threepoint_menu.last, self.elements.page_card_threepoint_menu)
        self.base_page.click_expect(self.elements.btn_card_menu_delete, reclick=True)

    @allure.step("Verify delete confirm disabled by default")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("Verify deleted scope if exist")
    def verify_scope_deleted(self):
        self.elements.input_keyword_search.fill("e2e-scope-code2")
        expect(self.elements.option_cards).not_to_be_visible()

    # copy
    @allure.step("Open copy scope dialog")
    def click_to_copy_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.elements.input_keyword_search.fill("e2e-scope-code")
        self.page.mouse.wheel(0, 500)
        self.base_page.sleep(1)
        self.base_page.click_expect(self.elements.btn_card_threepoint_menu.last, self.elements.page_card_threepoint_menu)
        self.base_page.click_expect(self.elements.btn_card_menu_copy)

    @allure.step("Validate and fill scope code")
    def validate_copy_and_fill_code(self):
        self.operate_page.verify_input_text(self.elements.input_scope_code, "copy-")
        
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
        self.elements.input_scope_code.fill("copy-e2e-scope-code")

    @allure.step("Validate and update scope name")
    def validate_copy_and_fill_name(self):
        expect(self.elements.input_scope_name).to_have_value(re.compile("copy-"),timeout=5000)

        self.input_name_cases = [
            ("  ", "必填欄位"),
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_scope_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_scope_name.fill("copy-e2e-scope-name")

    @allure.step("Validate and update scope description")
    def validate_and_copy_scope_description(self):
        self.input_description_cases = [
            ("#" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_scope_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_scope_description.fill("copy-e2e-scope-description")

    @allure.step("update scope status")
    def enable_scope_status(self):
        self.elements.radio_status_enable.click()

    @allure.step("Submit scope and verify updated")
    def submit_and_verify_copied(self):
        self.elements.btn_submit.click()
        expect(self.elements.page_dialog).to_be_visible()
        self.elements.btn_dialog_checked.click()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.elements.input_keyword_search.fill("copy-")
        expect(self.elements.option_cards.first).to_be_visible()
