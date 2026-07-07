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

    @allure.step("Open assign permission list")
    def open_assign_permission_list(self):
        self.base_page.click_expect(
            self.elements.tab_permission_assign,
            self.elements.btn_create_assign_permission,
        )

    @allure.step("Open create assign permission page")
    def open_create_assign_permission_page(self):
        self.open_assign_permission_list()
        self.base_page.click_expect(
            self.elements.btn_create_assign_permission,
            self.elements.btn_add_assign_permission,
        )

    @allure.step("Select assign permission member")
    def select_assign_permission_member(self):
        self.base_page.click_expect(self.elements.btn_add_assign_permission)
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_assign_member_search,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            "testuser01",
        )

    @allure.step("Select assign role permission")
    def select_assign_role_permission(self):
        self.operate_page.select_list(
            self.elements.list_assign_permission_role,
            self.elements.option_dropdown_list,
            0,
        )

    @allure.step("Select assign scope permission")
    def select_assign_scope_permission(self):
        self.operate_page.select_list(
            self.elements.list_assign_permission_scope,
            self.elements.option_dropdown_list,
            0,
        )

    @allure.step("Validate and fill assign permission description")
    def validate_and_fill_description(self):
        input_cases = [
            ("#" * 201, "頛詨摮頞???瑕漲200"),
        ]
        self.operate_page.verify_input(
            self.elements.input_assign_permission_description,
            self.elements.msg_field_error,
            input_cases,
        )
        self.elements.input_assign_permission_description.fill("e2e-testing-permission-assign-description")

    @allure.step("Create another assign permission")
    def create_another_assign_permission(self):
        self.base_page.click_expect(self.elements.btn_create_more)
        self.elements.input_assign_permission_description.last.fill(
            "e2e-testing-permission-assign-description2"
        )

    @allure.step("Submit assign permission and verify created")
    def submit_and_verify_created(self):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(self.elements.input_keyword_search, "testuser01")

    @allure.step("Verify assign permission list visible")
    def verify_assign_permission_list_visible(self):
        self.open_assign_permission_list()
        expect(self.elements.option_cards.first).to_be_visible()

    @allure.step("Search assign permission by member")
    def search_assign_permission_by_member(self):
        self.operate_page.search_keyword(self.elements.input_keyword_search, "testuser01")
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
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_filter_date_reyoung.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_filter_date_grewup.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("Open update assign permission page")
    def open_update_assign_permission_page(self):
        self.open_assign_permission_list()
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            "testuser01",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
        )

    @allure.step("Replace assign permission member")
    def replace_assign_permission_member(self):
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_assign_member_search,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            "testuser02",
        )

    @allure.step("Replace assign role permission")
    def replace_assign_role_permission(self):
        self.operate_page.select_list(
            self.elements.list_assign_permission_role,
            self.elements.option_dropdown_list,
            1,
        )

    @allure.step("Replace assign scope permission")
    def replace_assign_scope_permission(self):
        self.operate_page.select_list(
            self.elements.list_assign_permission_scope,
            self.elements.option_dropdown_list,
            1,
        )

    @allure.step("Validate and update assign permission description")
    def validate_and_update_description(self):
        input_cases = [
            ("#" * 201, "頛詨摮頞???瑕漲200"),
        ]
        self.operate_page.verify_input(
            self.elements.input_assign_permission_description,
            self.elements.msg_field_error,
            input_cases,
        )
        self.elements.input_assign_permission_description.fill("e2e-testing-permission-assign-edit-description")

    @allure.step("Submit assign permission and verify updated")
    def submit_and_verify_updated(self):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(self.elements.input_keyword_search, "testuser02")

    @allure.step("Open assign permission delete dialog")
    def open_assign_permission_delete_dialog(self):
        self.open_assign_permission_list()
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            "testuser02",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
        )

    @allure.step("Verify assign permission delete input")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("Verify deleted assign permission")
    def verify_assign_permission_deleted(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "testuser02",
            self.elements.option_cards,
            should_exist=False,
        )
