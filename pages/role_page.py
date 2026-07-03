from playwright.sync_api import Page
from pages.locators.elements import RoleElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage
import allure


class RolePage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = RoleElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    # create
    @allure.step("Open create role page")
    def click_to_create_role_page(self):
        pass

    @allure.step("Validate and fill role code")
    def validate_and_fill_role_code(self):
        pass

    @allure.step("Validate and fill role name")
    def validate_and_fill_role_name(self):
        pass

    @allure.step("Validate and fill role description")
    def validate_and_fill_role_description(self):
        pass

    @allure.step("Select role scopes")
    def select_role_scopes(self):
        pass

    @allure.step("Validate duplicate role")
    def validate_duplicate_role(self):
        pass

    @allure.step("Create another role")
    def create_another_role(self):
        pass

    @allure.step("Submit role and verify created")
    def submit_and_verify_created(self):
        pass

    # read
    @allure.step("Verify role list visible")
    def verify_role_list_visible(self):
        pass

    @allure.step("Search role with no result")
    def search_role_with_no_result(self):
        pass

    @allure.step("Search role by code")
    def search_role_by_code(self):
        pass

    @allure.step("Search role by name")
    def search_role_by_name(self):
        pass

    @allure.step("Filter roles by status")
    def filter_roles_by_status(self):
        pass

    @allure.step("Sort roles by created time")
    def sort_roles_by_created_time(self):
        pass

    # update
    @allure.step("Open update role page")
    def click_to_update_role_page(self):
        pass

    @allure.step("Validate and update role name")
    def validate_and_update_role_name(self):
        pass

    @allure.step("Validate and update role description")
    def validate_and_update_role_description(self):
        pass

    @allure.step("Update role scopes")
    def update_role_scopes(self):
        pass

    @allure.step("Disable role status")
    def disable_role_status(self):
        pass

    @allure.step("Submit role and verify updated")
    def submit_and_verify_updated(self):
        pass

    # delete
    @allure.step("Open role delete dialog")
    def open_role_delete_dialog(self):
        pass

    @allure.step("Verify delete confirm disabled by default")
    def verify_delete_confirm_disabled_by_default(self):
        pass

    @allure.step("Cancel role delete then reopen")
    def cancel_role_delete_then_reopen(self):
        pass

    @allure.step("Confirm role delete")
    def confirm_role_delete(self):
        pass

    @allure.step("Verify role deleted")
    def verify_role_deleted(self):
        pass

    # copy
    @allure.step("Open copy role page")
    def click_to_copy_role_page(self):
        pass

    @allure.step("Validate and fill copied role code")
    def validate_copy_and_fill_code(self):
        pass

    @allure.step("Validate and fill copied role name")
    def validate_copy_and_fill_name(self):
        pass

    @allure.step("Validate and fill copied role description")
    def validate_and_copy_role_description(self):
        pass

    @allure.step("Enable copied role status")
    def enable_role_status(self):
        pass

    @allure.step("Submit role and verify copied")
    def submit_and_verify_copied(self):
        pass
