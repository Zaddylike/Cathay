import re
import allure
from playwright.sync_api import Page, expect

from data.schema.permission_cases import (
    PERMISSION_CODE_CASES,
    PERMISSION_CREATE_NAME_CASES,
    PERMISSION_DESCRIPTION_CASES,
    PERMISSION_EDIT_NAME_CASES,
    duplicate_permission_code_cases,
)

from pages.locators.elements import ScopeElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage

class ScopePage:
    def __init__(
        self,
        page: Page,
        base_page: BasePage | None = None,
        operate_page: OperatePage | None = None,
    ):
        self.page = page
        self.elements = ScopeElements(page)
        self.base_page = base_page or BasePage(page)
        self.operate_page = operate_page or OperatePage(page, self.base_page)

    def scope_card(self, scope_code: str):
        return self.elements.option_cards.filter(
            has=self.page.get_by_text(scope_code, exact=True)
        )

    def search_scope_card(self, scope_code: str):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.elements.input_keyword_search.clear()
        self.base_page.wait_loading_disapper()
        self.elements.input_keyword_search.fill(scope_code)
        self.base_page.wait_loading_disapper()
        return self.scope_card(scope_code)

    """以完整 Scope code 搜尋並確認是否存在唯一資料。"""
    def scope_exists(self, scope_code: str) -> bool:
        scope_card = self.search_scope_card(scope_code)
        exists = scope_card.count() == 1
        self.elements.input_keyword_search.clear()
        self.base_page.wait_loading_disapper()
        return exists



    @allure.step("新增範圍 [{scope_code}]")
    def create_scope(self, scope_code: str, scope_name: str, scope_description: str):
        self.click_to_create_scope_page()
        self.elements.input_scope_code.fill(scope_code)
        self.elements.input_scope_name.fill(scope_name)
        self.elements.input_scope_description.fill(scope_description)
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.search_scope_by_code(scope_code)

    #  create

    @allure.step("開啟新增範圍視窗")
    def click_to_create_scope_page(self):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.base_page.click_expect(self.elements.btn_create_scope)
        expect(self.elements.input_scope_code).to_be_visible()

    @allure.step("驗證並填寫範圍代碼")
    def validate_and_fill_scope_code(self, scope_code: str):
        self.input_code_cases = PERMISSION_CODE_CASES
        element_input = self.elements.input_scope_code
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, self.input_code_cases)
        self.elements.input_scope_code.fill(scope_code)

    @allure.step("驗證並填寫範圍名稱")
    def validate_and_fill_scope_name(self, scope_name: str):
        self.input_name_cases = PERMISSION_CREATE_NAME_CASES
        element_input = self.elements.input_scope_name
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_scope_name.fill(scope_name)

    @allure.step("驗證並填寫範圍描述")
    def validate_and_fill_scope_description(self, scope_description: str):
        self.input_description_cases = PERMISSION_DESCRIPTION_CASES
        element_input = self.elements.input_scope_description
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_scope_description.fill(scope_description)

    @allure.step("驗證範圍代碼不可重複")
    def validate_duplicate_scope(self, scope_code: str):
        self.base_page.click_expect(self.elements.btn_scope_add_scope)
        expect(self.elements.input_scope_code).to_have_count(2)
        
        self.input_scope_cases = duplicate_permission_code_cases(scope_code)
        element_input = self.elements.input_scope_code.last
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, self.input_scope_cases)
        self.base_page.click_expect(self.elements.btn_scope_remove_create.last)

    @allure.step("新增另一筆範圍")
    def create_another_scope(
        self,
        scope_code: str,
        scope_name: str,
        scope_description: str,
    ):
        self.elements.input_scope_code.last.fill(scope_code)
        if ( self.elements.input_scope_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()
        self.elements.input_scope_name.last.fill(scope_name)
        self.elements.input_scope_description.last.fill(scope_description)
    
    @allure.step("送出範圍並驗證新增成功")
    def submit_and_verify_created(self, scope_code: str):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            scope_code,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.base_page.take_screenshot("Scope_Create_Success")

    #  copy

    @allure.step("開啟複製範圍視窗")
    def click_to_copy_scope_page(self, source_scope_code: str):
        scope_card = self.search_scope_card(source_scope_code)
        expect(scope_card).to_have_count(1)
        menu_button = scope_card.locator(".p-splitbutton-dropdown")
        expect(menu_button).to_have_count(1)
        self.base_page.click_expect(
            menu_button,
            self.elements.page_card_threepoint_menu,
        )
        self.base_page.click_expect(
            self.elements.btn_card_menu_copy,
        )

    @allure.step("驗證並填寫複製後的範圍代碼")
    def validate_copy_and_fill_code(self, copied_scope_code: str):
        self.operate_page.verify_input_text(self.elements.input_scope_code, "copy-")
        
        self.input_code_cases = PERMISSION_CODE_CASES
        element_input = self.elements.input_scope_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_code_cases)
        self.elements.input_scope_code.fill(copied_scope_code)

    @allure.step("驗證並填寫複製後的範圍名稱")
    def validate_copy_and_fill_name(self, copied_scope_name: str):
        expect(self.elements.input_scope_name).to_have_value(re.compile("copy-"),timeout=5000)

        self.input_name_cases = PERMISSION_EDIT_NAME_CASES
        element_input = self.elements.input_scope_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_scope_name.fill(copied_scope_name)

    @allure.step("驗證並填寫複製後的範圍描述")
    def validate_and_copy_scope_description(self, copied_scope_description: str):
        self.input_description_cases = PERMISSION_DESCRIPTION_CASES
        element_input = self.elements.input_scope_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_scope_description.fill(copied_scope_description)

    @allure.step("啟用複製後的範圍狀態")
    def enable_scope_status(self):
        self.elements.radio_status_enable.click()

    @allure.step("送出範圍並驗證複製成功")
    def submit_and_verify_copied(self, copied_scope_code: str):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")

        scope_card = self.search_scope_card(copied_scope_code)
        expect(scope_card).to_have_count(1)
        menu_button = scope_card.locator(".p-splitbutton-dropdown")
        expect(menu_button).to_have_count(1)
        self.base_page.click_expect(
            menu_button,
            self.elements.page_card_threepoint_menu,
        )
        self.base_page.click_expect(
            self.elements.btn_card_menu_update,
            reclick=True,
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
    def search_scope_by_code(self, scope_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            scope_code,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.clear()

    @allure.step("搜尋框搜尋姓名已存在範圍")
    def search_scope_by_name(self, scope_name: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            scope_name,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.clear()

    @allure.step("進階篩選面板篩選狀態")
    def filter_projects_by_status(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.base_page.click_expect(self.elements.btn_filter_status_enable)
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.base_page.click_expect(self.elements.btn_filter_status_disable)
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

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

    @allure.step("開啟編輯範圍視窗")
    def click_to_update_scope_page(self, scope_code: str):
        self.base_page.click_expect(self.elements.tab_permission_scope)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            scope_code,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
            action_reclick=True,
        )

    @allure.step("驗證並更新範圍名稱")
    def validate_and_update_scope_name(self, updated_scope_name: str):
        self.input_name_cases = PERMISSION_EDIT_NAME_CASES
        element_input = self.elements.input_scope_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_scope_name.fill(updated_scope_name)

    @allure.step("驗證並更新範圍描述")
    def validate_and_update_scope_description(self, updated_scope_description: str):
        self.input_description_cases = PERMISSION_DESCRIPTION_CASES
        element_input = self.elements.input_scope_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_scope_description.fill(updated_scope_description)

    @allure.step("停用範圍狀態")
    def disable_scope_status(self):
        self.elements.radio_status_disable.click()

    @allure.step("送出範圍並驗證更新成功")
    def submit_and_verify_updated(self, updated_scope_name: str):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            updated_scope_name,
            self.elements.option_cards.last,
            True
        )

    #  delete

    @allure.step("刪除範圍 [{scope_code}]")
    def delete_scope(self, scope_code: str):
        scope_card = self.search_scope_card(scope_code)
        expect(scope_card).to_have_count(1)
        menu_button = scope_card.locator(".p-splitbutton-dropdown")
        expect(menu_button).to_have_count(1)
        self.base_page.click_expect(
            menu_button,
            self.elements.page_card_threepoint_menu,
        )
        self.base_page.click_expect(
            self.elements.btn_card_menu_delete,
            reclick=True,
        )
        self.operate_page.verify_delete()
        self.base_page.wait_loading_disapper()
        expect(scope_card).to_have_count(0)
        self.elements.input_keyword_search.clear()
        self.base_page.wait_loading_disapper()

    @allure.step("若範圍存在則刪除 [{scope_code}]")
    def delete_scope_if_exists(self, scope_code: str) -> bool:
        scope_card = self.search_scope_card(scope_code)

        if scope_card.count() == 0:
            expect(self.elements.msg_search_noResult).to_be_visible()
            self.elements.input_keyword_search.clear()
            self.base_page.wait_loading_disapper()
            return False

        expect(scope_card).to_have_count(1)
        self.delete_scope(scope_code)
        return True

    def click_to_delete_scope_page(self, scope_code: str):
        self.delete_scope(scope_code)

    @allure.step("驗證範圍已刪除 [{scope_code}]")
    def verify_scope_deleted(self, scope_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            scope_code,
            self.elements.btn_filter_clear_noResult,
            should_exist=True,
        )
