from playwright.sync_api import Page, expect
from pages.locators.elements import ScopeElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage
import allure, re
from config.settings import SCOPE_CODE

class ScopePage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ScopeElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    #  create

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
        self.elements.input_scope_code.fill(SCOPE_CODE)

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
        self.elements.input_scope_code.last.fill(f"${SCOPE_CODE}2")
        if ( self.elements.input_permission_init_scope_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()
        self.elements.input_scope_name.last.fill("e2e-scope-name2")
        self.elements.input_scope_description.last.fill("e2e-scope-description2")
    
    @allure.step("Submit scope and verify created")
    def submit_and_verify_created(self):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-scope-code",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.base_page.take_screenshot("Scope_Create_Success")

    #  copy

    @allure.step("Open copy scope dialog")
    def click_to_copy_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            SCOPE_CODE,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_copy,
        )

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
        self.elements.input_scope_code.fill(f"copy-{SCOPE_CODE}")

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
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")

        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            f"copy-{SCOPE_CODE}",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
            action_reclick=True,
        )
        self.elements.radio_status_disable.click()
        self.operate_page.submit_and_confirm()

    #  read

    @allure.step("進入範圍頁面")
    def verify_scope_list_visible(self):
        self.base_page.click_expect(self.elements.tab_permission_scope, self.elements.btn_create_scope)

    @allure.step("搜尋框搜尋不存在範圍")
    def search_scope_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("搜尋框搜尋代碼已存在範圍")
    def search_scope_by_code(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            SCOPE_CODE,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("搜尋框搜尋姓名已存在範圍")
    def search_scope_by_name(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "name",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("進階篩選面板篩選狀態")
    def filter_projects_by_status(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.base_page.click_expect(self.elements.btn_filter_status_enable)
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.base_page.click_expect(self.elements.btn_filter_status_disable)
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("進階篩選面板排序日期")
    def sort_projects_by_created_time(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.base_page.click_expect(self.elements.btn_filter_date_reyoung)
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.base_page.click_expect(self.elements.btn_filter_date_grewup)
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()


    #  update

    @allure.step("Open update scope dialog")
    def click_to_update_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            f"{SCOPE_CODE}2",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
            action_reclick=True,
        )

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
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-scope-name2-edit",
            self.elements.option_cards.last,
            True
        )

    #  delete

    @allure.step("Open delete scope dialog")
    def click_to_delete_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            f"copy-{SCOPE_CODE}",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
            action_reclick=True,
        )
        self.operate_page.verify_delete()
        self.base_page.wait_loading_disapper()

        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            "e2e-scope-name2-edit",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
            action_reclick=True,
        )
        
        self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__body input').fill("DELETE")
        self.elements.btn_dialog_delete_confirm.click()
        self.elements.btn_dialog_checked.click()

    @allure.step("Verify deleted scope if exist")
    def verify_scope_deleted(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "copy-e2e-scope-code",
            self.elements.btn_filter_clear_noResult,
            should_exist=True,
        )
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-scope-name2-edit",
            self.elements.btn_filter_clear_noResult,
            should_exist=True,
        )