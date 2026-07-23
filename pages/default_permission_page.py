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

    @allure.step("新增預設權限 [{role_code}]")
    def create_default_permission(self, role_code: str, scope_code: str):
        self.open_create_default_permission_page()
        self.select_default_role_permission(role_code)
        self.select_default_scope_permission(scope_code)
        self.submit_and_verify_created(role_code)

# create

    @allure.step("開啟預設權限清單")
    def open_create_permission_list(self):
        self.base_page.click_expect(
            self.elements.tab_permission_default,
            self.elements.btn_create_default_permission,
        )

    @allure.step("開啟新增預設權限頁面")
    def open_create_default_permission_page(self):
        self.base_page.click_expect(
            self.elements.tab_permission_default,
            self.elements.btn_create_default_permission,
        )
        self.base_page.click_expect(
            self.elements.btn_create_default_permission,
            self.elements.btn_submit,
        )
        self.base_page.wait_loading_disapper()

    @allure.step("選擇預設權限角色")
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

    @allure.step("選擇預設權限範圍")
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

    @allure.step("送出預設權限並驗證新增成功")
    def submit_and_verify_created(self, role_code: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.option_permissions.last,
        )

# read

    @allure.step("開啟預設權限清單")
    def open_permission_list(self):
        self.base_page.click_expect(
            self.elements.tab_permission_default,
            self.elements.btn_set_default_permission,
        )

    @allure.step("驗證預設權限清單顯示")
    def verify_default_permission_list_visible(self):
        self.base_page.click_expect(
            self.elements.tab_permission_default,
            self.elements.btn_set_default_permission,
        )
        expect(self.elements.option_permissions.first).to_be_visible()

    @allure.step("依角色搜尋預設權限")
    def search_default_permission_by_role(self, role_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.msg_search_noResult,
            should_exist=False
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("依範圍搜尋預設權限")
    def search_default_permission_by_scope(self, scope_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            scope_code,
            self.elements.msg_search_noResult,
            should_exist=False
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("搜尋不存在的預設權限並驗證無結果")
    def search_default_permission_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    #  update

    @allure.step("開啟編輯預設權限頁面")
    def open_update_default_permission_page(self):
        self.base_page.click_expect(
            self.elements.tab_permission_default,
            self.elements.btn_set_default_permission,
        )
        self.base_page.click_expect(
            self.elements.btn_create_default_permission,
            self.elements.list_default_role.last,
        )

    @allure.step("更換預設權限角色")
    def replace_default_role_permission(self, role_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_default_role.last,
            self.elements.option_dropdown_list_avail,
            role_code,
        )

    @allure.step("更換預設權限範圍")
    def replace_default_scope_permission(self, scope_code: str):
        self.operate_page.select_list_by_text(
            self.elements.list_default_scope.last,
            self.elements.option_dropdown_list_avail,
            scope_code,
        )

    @allure.step("送出預設權限並驗證更新成功")
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

    @allure.step("開啟刪除預設權限視窗")
    def open_default_permission_delete_dialog(self, role_code: str):
        self.base_page.click_expect(
            self.elements.tab_permission_default,
            self.elements.btn_set_default_permission,
        )
        self.elements.input_keyword_search.fill(role_code)
        self.base_page.wait_loading_disapper()
        row = self.get_default_permission_row(role_code)
        expect(row).to_be_visible()
        self.click_default_permission_delete(role_code)

    @allure.step("驗證預設權限刪除確認欄位")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("刪除預設權限 [{role_code}]")
    def delete_default_permission(self, role_code: str):
        self.open_default_permission_delete_dialog(role_code)
        self.verify_deleted_input()

    @allure.step("若預設權限存在則刪除 [{role_code}]")
    def delete_default_permission_if_exists(self, role_code: str) -> bool:
        self.base_page.click_expect(self.elements.tab_permission_default)
        self.elements.input_keyword_search.fill(role_code)
        self.base_page.wait_loading_disapper()
        row = self.get_default_permission_row(role_code)
        if row.count() == 0 or not row.is_visible():
            self.elements.input_keyword_search.fill("")
            return False
        self.click_default_permission_delete(role_code)
        self.verify_deleted_input()
        return True

    @allure.step("驗證預設權限已刪除 [{role_code}]")
    def verify_default_permission_deleted(self, role_code: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            role_code,
            self.elements.option_permissions,
            should_exist=False,
        )
