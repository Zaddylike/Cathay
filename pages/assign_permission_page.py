import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators.elements import AssignPermissionElements
from pages.operate_page import OperatePage


class AssignPermissionPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = AssignPermissionElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    @allure.step("Create assign permission [{role_code}]")
    def create_assign_permission(
        self,
        member_keyword: str,
        role_code: str,
        scope_code: str,
        description: str,
    ):
        self.open_create_assign_permission_page()
        self.select_assign_permission_member(member_keyword)
        self.select_assign_role_permission(role_code)
        self.select_assign_scope_permission(scope_code)
        self.elements.input_assign_permission_description.fill(description)
        self.submit_and_verify_created(role_code)

    @allure.step("Open assign permission list")
    def open_assign_permission_list(self):
        self.base_page.click_expect(
            self.elements.tab_permission_assign,
            self.elements.btn_create_assign_permission,
        )


    #  create

    @allure.step("Open create assign permission page")
    def open_create_assign_permission_page(self):
        self.open_assign_permission_list()
        self.base_page.click_expect(
            self.elements.btn_create_assign_permission,
            self.elements.btn_assign_create_more_assign,
        )

    @allure.step("Select assign permission member")
    def select_assign_permission_member(self, member_keyword: str):
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.first,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            member_keyword,
        )

    @allure.step("Select assign role permission")
    def select_assign_role_permission(self, role_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_assign_permission_role.first,
            self.elements.option_dropdown_list_avail,
            role_code,
        )

    @allure.step("Select assign scope permission")
    def select_assign_scope_permission(self, scope_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_assign_permission_scope.nth(1),
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

    @allure.step("Validate and fill assign permission description")
    def validate_and_fill_description(self, description: str):
        input_cases = [
            ("#" * 201, "輸入字數超過限制長度200"),
        ]
        self.operate_page.verify_input(
            self.elements.input_assign_permission_description,
            self.elements.msg_field_error,
            input_cases,
        )
        self.elements.input_assign_permission_description.fill(description)

    @allure.step("Create another assign permission")
    def create_another_assign_permission(
        self,
        member_keyword: str,
        role_code: str,
        scope_code: str,
        description: str,
    ):
        self.base_page.click_expect(self.elements.btn_assign_create_more_assign)
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.last,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            member_keyword,
        )

        self.operate_page.select_list_by_text(
            self.elements.list_assign_permission_role.nth(2),
            self.elements.option_dropdown_list_avail,
            role_code,
        )

        self.base_page.click_expect(self.elements.btn_more_permission.last)
        self.operate_page.select_list_by_text(
            self.elements.list_assign_permission_scope.nth(3),
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

        self.elements.input_assign_permission_description.last.fill(
            description
        )

    @allure.step("Submit assign permission and verify created")
    def submit_and_verify_created(self, assignment_key: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            assignment_key,
            self.elements.option_assign,
        )


    #  read

    @allure.step("Verify assign permission list visible")
    def verify_assign_permission_list_visible(self):
        self.open_assign_permission_list()
        expect(self.elements.btn_create_assign_permission).to_be_visible()

    @allure.step("Search assign permission by member")
    def search_assign_permission_by_member(self, member_keyword: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            member_keyword,
            self.elements.option_assign,
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("Search assign permission with no result")
    def search_assign_permission_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("Sort assign permissions by created time")
    def sort_assign_permissions_by_created_time(self):
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_date_reyoung.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_assign.first)

        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_date_grewup.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_assign.first)

        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_footer_clearfilter.click()


    #  update

    @allure.step("Open update assign permission page")
    def open_update_assign_permission_page(self, assignment_key: str):
        self.open_assign_permission_list()
        expect(self.elements.btn_create_assign_permission).to_be_visible()
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            assignment_key,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
        )

    @allure.step("Replace assign role permission")
    def replace_assign_role_permission(self, role_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_assign_edit_permission_role.first,
            self.elements.option_dropdown_list_avail,
            role_code,
        )

    @allure.step("Replace assign scope permission")
    def replace_assign_scope_permission(self, scope_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_assign_edit_permission_scope.last,
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

    @allure.step("Validate and update assign permission description")
    def validate_and_update_description(self, updated_description: str):
        input_cases = [
            ("#" * 201, "輸入字數超過限制長度200"),
        ]
        self.operate_page.verify_input(
            self.elements.input_assign_permission_description,
            self.elements.msg_field_error,
            input_cases,
        )
        self.elements.input_assign_permission_description.fill(updated_description)

    @allure.step("Submit assign permission and verify updated")
    def submit_and_verify_updated(self, assignment_key: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            assignment_key,
            self.elements.option_assign,
        )

    #  delete

    @allure.step("Open assign permission delete dialog")
    def open_assign_permission_delete_dialog(self, assignment_key: str):
        self.open_assign_permission_list()
        expect(self.elements.btn_create_assign_permission).to_be_visible()
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            assignment_key,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
        )

    @allure.step("Verify assign permission delete input")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("Delete assign permission [{assignment_key}]")
    def delete_assign_permission(self, assignment_key: str):
        self.open_assign_permission_delete_dialog(assignment_key)
        self.verify_deleted_input()

    @allure.step("Delete assign permission if it exists [{assignment_key}]")
    def delete_assign_permission_if_exists(self, assignment_key: str) -> bool:
        self.open_assign_permission_list()
        self.elements.input_keyword_search.fill(assignment_key)
        self.base_page.wait_loading_disapper()
        if self.elements.msg_search_noResult.is_visible():
            self.elements.input_keyword_search.fill("")
            return False
        self.delete_assign_permission(assignment_key)
        return True

    @allure.step("Verify deleted assign permission")
    def verify_assign_permission_deleted(self, assignment_key: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            assignment_key,
            self.elements.option_assign,
            should_exist=False,
        )
