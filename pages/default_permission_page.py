import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators.elements import DefaultPermissionElements
from pages.operate_page import OperatePage


class DefaultPermissionPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = DefaultPermissionElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    @allure.step("Open default permission list")
    def open_default_permission_list(self):
        self.base_page.click_expect(
            self.elements.tab_permission_default,
            self.elements.btn_create_default_permission,
        )

    @allure.step("Open create default permission page")
    def open_create_default_permission_page(self):
        self.open_default_permission_list()
        self.base_page.click_expect(
            self.elements.btn_create_default_permission,
            self.elements.btn_add_default_role,
        )

    @allure.step("Select default role permission")
    def select_default_role_permission(self):
        self.base_page.click_expect(self.elements.btn_add_default_role)
        self.operate_page.select_list(
            self.elements.list_default_permission_role,
            self.elements.option_dropdown_list,
            0,
        )

    @allure.step("Select default scope permission")
    def select_default_scope_permission(self):
        self.base_page.click_expect(self.elements.btn_add_default_scope)
        self.operate_page.select_list(
            self.elements.list_default_permission_scope,
            self.elements.option_dropdown_list,
            0,
        )

    @allure.step("Submit default permission and verify created")
    def submit_and_verify_created(self):
        self.operate_page.submit_and_confirm()
        expect(self.elements.option_cards.first).to_be_visible()

    @allure.step("Verify default permission list visible")
    def verify_default_permission_list_visible(self):
        self.open_default_permission_list()
        expect(self.elements.option_cards.first).to_be_visible()

    @allure.step("Search default permission by role")
    def search_default_permission_by_role(self):
        self.operate_page.search_keyword(self.elements.input_keyword_search, "role")
        self.elements.input_keyword_search.fill("")

    @allure.step("Search default permission by scope")
    def search_default_permission_by_scope(self):
        self.operate_page.search_keyword(self.elements.input_keyword_search, "scope")
        self.elements.input_keyword_search.fill("")

    @allure.step("Search default permission with no result")
    def search_default_permission_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("Open update default permission page")
    def open_update_default_permission_page(self):
        self.open_default_permission_list()
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            "role",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
        )

    @allure.step("Replace default role permission")
    def replace_default_role_permission(self):
        self.operate_page.select_list(
            self.elements.list_default_permission_role,
            self.elements.option_dropdown_list,
            1,
        )

    @allure.step("Replace default scope permission")
    def replace_default_scope_permission(self):
        self.operate_page.select_list(
            self.elements.list_default_permission_scope,
            self.elements.option_dropdown_list,
            1,
        )

    @allure.step("Submit default permission and verify updated")
    def submit_and_verify_updated(self):
        self.operate_page.submit_and_confirm()
        expect(self.elements.option_cards.first).to_be_visible()

    @allure.step("Open default permission delete dialog")
    def open_default_permission_delete_dialog(self):
        self.open_default_permission_list()
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            "role",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
        )

    @allure.step("Verify default permission delete input")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("Verify deleted default permission")
    def verify_default_permission_deleted(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "role",
            self.elements.option_cards,
            should_exist=False,
        )
