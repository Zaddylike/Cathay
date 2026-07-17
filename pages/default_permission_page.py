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

    @allure.step("Create default permission [{role_code}]")
    def create_default_permission(self, role_code: str, scope_code: str):
        self.open_create_default_permission_page()
        self.select_default_role_permission(role_code)
        self.select_default_scope_permission(scope_code)
        self.submit_and_verify_created(role_code)

    #  create

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
            self.elements.btn_submit,
        )
        self.base_page.wait_loading_disapper()

    @allure.step("Select default role permission")
    def select_default_role_permission(self, role_code: str):
        if self.elements.btn_add_default_role.is_visible():
            self.base_page.click_expect(self.elements.btn_add_default_role, self.elements.list_default_role.last)
        else:
            self.base_page.click_expect(self.elements.btn_more_default_role, self.elements.list_default_role.last)

        self.operate_page.select_list_by_text(
            self.elements.list_default_role.last,
            self.elements.option_dropdown_list_avail,
            role_code,
        )

    @allure.step("Select default scope permission")
    def select_default_scope_permission(self, scope_code: str):
        if self.elements.btn_add_default_scope.is_visible():
            self.base_page.click_expect(self.elements.btn_add_default_scope, self.elements.list_default_scope.last)
        else:
            self.base_page.click_expect(self.elements.btn_more_default_scope, self.elements.list_default_scope.last)

        self.operate_page.select_list_by_text(
            self.elements.list_default_scope.last,
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

    @allure.step("Submit default permission and verify created")
    def submit_and_verify_created(self, role_code: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.option_permissions.last,
        )

    #  read

    @allure.step("Verify default permission list visible")
    def verify_default_permission_list_visible(self):
        self.open_default_permission_list()
        expect(self.elements.option_permissions.first).to_be_visible()

    @allure.step("Search default permission by role")
    def search_default_permission_by_role(self, role_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.msg_search_noResult,
            should_exist=False
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("Search default permission by scope")
    def search_default_permission_by_scope(self, scope_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            scope_code,
            self.elements.msg_search_noResult,
            should_exist=False
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("Search default permission with no result")
    def search_default_permission_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    #  update

    @allure.step("Open update default permission page")
    def open_update_default_permission_page(self):
        self.open_default_permission_list()
        self.base_page.click_expect(
            self.elements.btn_create_default_permission,
            self.elements.list_default_role.last,
        )

    @allure.step("Replace default role permission")
    def replace_default_role_permission(self, role_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_default_role.last,
            self.elements.option_dropdown_list_avail,
            role_code,
        )

    @allure.step("Replace default scope permission")
    def replace_default_scope_permission(self, scope_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_default_scope.last,
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

    @allure.step("Submit default permission and verify updated")
    def submit_and_verify_updated(self, role_code: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.option_permissions.last,
        )

    #  delete

    def get_default_permission_row(self, role_code: str):
        return self.elements.option_permissions.filter(has_text=role_code)

    def click_default_permission_delete(self, role_code: str):
        row = self.get_default_permission_row(role_code)
        self.base_page.click_expect(
            row.locator('app-icon[class="cursor-pointer"]')
        )

    @allure.step("Open default permission delete dialog")
    def open_default_permission_delete_dialog(self, role_code: str):
        self.open_default_permission_list()
        self.elements.input_keyword_search.fill(role_code)
        self.base_page.wait_loading_disapper()
        row = self.get_default_permission_row(role_code)
        expect(row).to_be_visible()
        self.click_default_permission_delete(role_code)

    @allure.step("Verify default permission delete input")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("Delete default permission [{role_code}]")
    def delete_default_permission(self, role_code: str):
        self.open_default_permission_delete_dialog(role_code)
        self.verify_deleted_input()

    @allure.step("Delete default permission if it exists [{role_code}]")
    def delete_default_permission_if_exists(self, role_code: str) -> bool:
        self.open_default_permission_list()
        self.elements.input_keyword_search.fill(role_code)
        self.base_page.wait_loading_disapper()
        row = self.get_default_permission_row(role_code)
        if row.count() == 0 or not row.is_visible():
            self.elements.input_keyword_search.fill("")
            return False
        self.click_default_permission_delete(role_code)
        self.verify_deleted_input()
        return True

    @allure.step("Verify deleted default permission")
    def verify_default_permission_deleted(self, role_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.option_permissions,
            should_exist=False,
        )
