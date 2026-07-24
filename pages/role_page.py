import re

import allure
from playwright.sync_api import Page, expect

from data.schema.permission_cases import (
    PERMISSION_CODE_CASES,
    PERMISSION_CREATE_NAME_CASES,
    PERMISSION_DESCRIPTION_CASES,
    PERMISSION_EDIT_NAME_CASES,
)
from pages.locators.elements import RoleElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage

class RolePage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = RoleElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    @allure.step("新增角色 [{role_code}]")
    def create_role(
        self,
        role_code: str,
        role_name: str,
        role_description: str,
        scope_code: str,
    ):
        self.click_to_create_role_page()
        self.elements.input_role_code.fill(role_code)
        self.elements.input_role_name.fill(role_name)
        self.elements.input_role_description.fill(role_description)
        self.select_role_scopes(scope_code)
        self.operate_page.submit_and_confirm()
        self.search_role_by_code(role_code)

    #  create

    @allure.step("開啟新增角色頁面")
    def click_to_create_role_page(self):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.base_page.click_expect(self.elements.btn_create_role)
        expect(self.elements.input_role_code).to_be_visible()

    @allure.step("驗證並填寫角色代碼")
    def validate_and_fill_role_code(self, role_code: str):
        self.input_code_cases = PERMISSION_CODE_CASES
        element_input = self.elements.input_role_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_code_cases)
        self.elements.input_role_code.fill(role_code)

    @allure.step("驗證並填寫角色名稱")
    def validate_and_fill_role_name(self, role_name: str):
        self.input_name_cases = PERMISSION_CREATE_NAME_CASES
        element_input = self.elements.input_role_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_role_name.fill(role_name)

    @allure.step("驗證並填寫角色描述")
    def validate_and_fill_role_description(self, role_description: str):
        self.input_description_cases = PERMISSION_DESCRIPTION_CASES
        element_input = self.elements.input_role_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_role_description.fill(role_description)

    @allure.step("選擇角色適用範圍")
    def select_role_scopes(self, scope_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_dropdown.last,
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

    @allure.step("確認送出並驗證成功")
    def submit_and_verify_created(self, role_code: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.option_cards.last,
        )

    #  copy
    
    @allure.step("開啟複製角色頁面")
    def click_to_copy_role_page(self, source_role_code: str):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            source_role_code,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_copy,
        )

    @allure.step("驗證並填寫複製後的角色代碼")
    def validate_copy_and_fill_code(self, copied_role_code: str):
        expect(self.elements.input_role_code).to_have_value(re.compile("copy-"),timeout=5000)

        self.input_code_cases = PERMISSION_CODE_CASES
        element_input = self.elements.input_role_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_code_cases)
        self.elements.input_role_code.fill(copied_role_code)

    @allure.step("驗證並填寫複製後的角色名稱")
    def validate_copy_and_fill_name(self, copied_role_name: str):
        expect(self.elements.input_role_name).to_have_value(re.compile("copy-"),timeout=5000)

        self.input_name_cases = PERMISSION_EDIT_NAME_CASES
        element_input = self.elements.input_role_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_role_name.fill(copied_role_name)

    @allure.step("驗證並填寫複製後的角色描述")
    def validate_and_copy_role_description(self, copied_role_description: str):
        self.input_description_cases = PERMISSION_DESCRIPTION_CASES
        element_input = self.elements.input_role_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_role_description.fill(copied_role_description)

    @allure.step("送出角色並驗證複製成功")
    def submit_and_verify_copied(self, copied_role_code: str):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            copied_role_code,
            self.elements.option_cards.last,
        )

    #  read

    @allure.step("開啟角色清單並驗證顯示")
    def verify_role_list_visible(self):
        self.base_page.click_expect(self.elements.tab_permission_role, self.elements.btn_create_role)
    
    @allure.step("搜尋不存在的角色並驗證無結果")
    def search_role_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("依角色代碼搜尋")
    def search_role_by_code(self, role_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("依角色名稱搜尋")
    def search_role_by_name(self, role_name: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_name,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("依狀態篩選角色")
    def filter_roles_by_status(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_enable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_disable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("依建立時間排序角色")
    def sort_roles_by_created_time(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_date_reyoung.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_date_grewup.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()

    #  update

    @allure.step("開啟編輯角色頁面")
    def click_to_update_role_page(self, role_code: str):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            role_code,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
            action_reclick=True,
        )

    @allure.step("驗證並更新角色名稱")
    def validate_and_update_role_name(self, updated_role_name: str):
        self.input_name_cases = PERMISSION_EDIT_NAME_CASES
        element_input = self.elements.input_role_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_role_name.fill(updated_role_name)

    @allure.step("驗證並更新角色描述")
    def validate_and_update_role_description(self, updated_role_description: str):
        self.input_description_cases = PERMISSION_DESCRIPTION_CASES
        element_input = self.elements.input_role_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_role_description.fill(updated_role_description)

    @allure.step("更新角色適用範圍")
    def add_role_scope(self, scope_code: str):
        self.elements.btn_create_more.click()
        self.operate_page.select_list_by_text(
            self.elements.list_dropdown.last,
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

    @allure.step("送出角色並驗證更新成功")
    def submit_and_verify_updated(self, updated_role_name: str):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            updated_role_name,
            self.elements.option_cards.last
        )

    #  delete

    @allure.step("開啟刪除角色視窗")
    def open_role_delete_dialog(self, role_code: str):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            role_code,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
            action_reclick=True,
        )

    @allure.step("驗證未輸入確認文字時不可刪除")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("刪除角色 [{role_code}]")
    def delete_role(self, role_code: str):
        self.open_role_delete_dialog(role_code)
        self.verify_deleted_input()

    @allure.step("若角色存在則刪除 [{role_code}]")
    def delete_role_if_exists(self, role_code: str) -> bool:
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.elements.input_keyword_search.fill(role_code)
        self.base_page.wait_loading_disapper()
        
        if self.elements.msg_search_noResult.is_visible():
            self.elements.input_keyword_search.fill("")
            return False
        self.delete_role(role_code)
        return True

    @allure.step("驗證角色已刪除 [{role_code}]")
    def verify_role_deleted(self, role_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.msg_search_noResult,
            should_exist=True,
        )


