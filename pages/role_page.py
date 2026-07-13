from playwright.sync_api import Page, expect
from pages.locators.elements import RoleElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage
import allure, re
from config.settings import ROLE_CODE

class RolePage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = RoleElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    #  create

    @allure.step("Open create role page")
    def click_to_create_role_page(self):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.base_page.click_expect(self.elements.btn_create_role)
        expect(self.elements.input_role_code).to_be_visible()

    @allure.step("Validate and fill role code")
    def validate_and_fill_role_code(self):
        self.input_code_cases = [
            ("中文", "只允許半形之英數字及符號：_-."),
            ("", "必填欄位"),
            ("$$$", "只允許半形之英數字及符號：_-."),
            ("ＡＢＣ", "只允許半形之英數字及符號：_-."),
            ("  ", "只允許半形之英數字及符號：_-."),
            ("#" * 21, "輸入字數超過限制長度20"),
        ]
        element_input = self.elements.input_role_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_code_cases)
        self.elements.input_role_code.fill(ROLE_CODE)

    @allure.step("Validate and fill role name")
    def validate_and_fill_role_name(self):
        self.input_name_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("  ", "必填欄位"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_role_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_role_name.fill("e2e-role-name")

    @allure.step("Validate and fill role description")
    def validate_and_fill_role_description(self):
        self.input_description_cases = [
            ("#" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_role_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_role_description.fill("e2e-role-description")

    @allure.step("Select scope in roles")
    def select_role_scopes(self):
        self.base_page.click_expect(self.elements.list_dropdown.last, self.elements.option_dropdown_list.first)
        self.elements.option_dropdown_list.first.click()

    @allure.step("確認送出並驗證成功")
    def submit_and_verify_created(self):
        self.operate_page.submit_and_confirm()

    #  copy
    
    @allure.step("Open copy role page")
    def click_to_copy_role_page(self):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            ROLE_CODE,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_copy,
        )

    @allure.step("Validate and fill copied role code")
    def validate_copy_and_fill_code(self):
        expect(self.elements.input_role_code).to_have_value(re.compile("copy-"),timeout=5000)

        self.input_code_cases = [
            ("中文", "只允許半形之英數字及符號：_-."),
            ("", "必填欄位"),
            ("$$$", "只允許半形之英數字及符號：_-."),
            ("ＡＢＣ", "只允許半形之英數字及符號：_-."),
            ("  ", "只允許半形之英數字及符號：_-."),
            ("#" * 21, "輸入字數超過限制長度20"),
        ]
        element_input = self.elements.input_role_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_code_cases)
        self.elements.input_role_code.fill("copy-e2e-role-code")

    @allure.step("Validate and fill copied role name")
    def validate_copy_and_fill_name(self):
        expect(self.elements.input_role_name).to_have_value(re.compile("copy-"),timeout=5000)

        self.input_name_cases = [
            ("  ", "必填欄位"),
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_role_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_role_name.fill("copy-e2e-role-name")

    @allure.step("Validate and fill copied role description")
    def validate_and_copy_role_description(self):
        self.input_description_cases = [
            ("#" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_role_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_role_description.fill("copy-e2e-role-description")

    @allure.step("Submit role and verify updated")
    def submit_and_verify_copied(self):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "copy-",
            self.elements.option_cards.last,
        )

    #  read

    @allure.step("Verify role list visible")
    def verify_role_list_visible(self):
        self.base_page.click_expect(self.elements.tab_permission_role, self.elements.btn_create_role)
    
    @allure.step("Search role with no result")
    def search_role_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("Search role by code")
    def search_role_by_code(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "code",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("Search role by name")
    def search_role_by_name(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "name",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("Filter roles by status")
    def filter_roles_by_status(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_enable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_disable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("Sort roles by created time")
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

    @allure.step("Open update role page")
    def click_to_update_role_page(self):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            f"copy-{ROLE_CODE}",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
            action_reclick=True,
        )

    @allure.step("Validate and update role name")
    def validate_and_update_role_name(self):
        self.input_name_cases = [
            ("  ", "必填欄位"),
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_role_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_role_name.fill("e2e-role-name-edit")

    @allure.step("Validate and update role description")
    def validate_and_update_role_description(self):
        self.input_description_cases = [
            ("#" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_role_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_role_description.fill("e2e-role-description-edit")

    @allure.step("Update role roles")
    def update_role_scopes(self):
        self.elements.btn_create_more.click()
        self.base_page.click_expect(self.elements.list_dropdown.first, self.elements.option_dropdown_list.first)
        self.base_page.click_expect(self.elements.option_dropdown_list_avail.nth(2))

        self.base_page.click_expect(self.elements.list_dropdown.last, self.elements.option_dropdown_list.first)
        self.base_page.click_expect(self.elements.option_dropdown_list_avail.nth(0))

    @allure.step("Submit role and verify updated")
    def submit_and_verify_updated(self):
        self.operate_page.submit_and_confirm()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-role-name-edit",
            self.elements.option_cards.last
        )

    #  delete

    @allure.step("Open role delete dialog")
    def open_role_delete_dialog(self):
        self.base_page.click_expect(self.elements.tab_permission_role)
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            f"copy-{ROLE_CODE}",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
            action_reclick=True,
        )

    @allure.step("Verify delete confirm disabled by default")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("Verify deleted role if exist")
    def verify_role_deleted(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            f"copy-{ROLE_CODE}",
            self.elements.msg_search_noResult,
            should_exist=True,
        )


