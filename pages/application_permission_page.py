import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators.elements import ApplicationPermissionElements
from pages.operate_page import OperatePage

from data.schema.permission_cases import (
    PERMISSION_CODE_CASES,
    PERMISSION_CREATE_NAME_CASES,
    PERMISSION_DESCRIPTION_CASES,
    PERMISSION_EDIT_NAME_CASES,
    duplicate_permission_code_cases,
)

class ApplicationPermissionPage:
    def __init__(
        self,
        page: Page,
        base_page: BasePage | None = None,
        operate_page: OperatePage | None = None,
    ):
        self.page = page
        self.elements = ApplicationPermissionElements(page)
        self.base_page = base_page or BasePage(page)
        self.operate_page = operate_page or OperatePage(page, self.base_page)

    @allure.step("進入專案身分驗證頁面")
    def open_to_permission_page(self, project_abbreviation: str):
        self.operate_page.go_to_permission_page(project_abbreviation)
        expect(self.elements.page_permission).to_contain_text("身份驗證")
    
    @allure.step("確認權限是否初始化")
    def permission_initialization_available(self) -> bool:
        self.elements.tab_permission.click()
        expect(self.elements.tab_permission).to_have_attribute("aria-selected", "true")
        self.base_page.wait_loading_disapper()
        return self.elements.btn_permission_add_permission.is_visible()

    @allure.step("開啟權限初始化頁面")
    def open_to_create_permission_page(self):
        self.base_page.click_expect(self.elements.tab_permission, self.elements.btn_permission_add_permission)
        self.base_page.click_expect(self.elements.btn_permission_add_permission, self.elements.btn_permission_add_scope)


    # Scope

    @allure.step("驗證輸入範圍代碼新增資料")
    def validate_and_fill_scope_code(self, scope_code: str):
        element_input = self.elements.input_permission_init_scope_code
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, PERMISSION_CODE_CASES)
        self.elements.input_permission_init_scope_code.fill(scope_code)

    @allure.step("驗證輸入範圍名稱新增資料")
    def validate_and_fill_scope_name(self, scope_name: str):
        element_input = self.elements.input_permission_init_scope_name
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, PERMISSION_CREATE_NAME_CASES)
        self.elements.input_permission_init_scope_name.fill(scope_name)

    @allure.step("驗證輸入範圍名稱新增資料")
    def validate_and_fill_scope_description(self, description: str):
        element_input = self.elements.input_permission_init_scope_description
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, PERMISSION_DESCRIPTION_CASES)
        self.elements.input_permission_init_scope_description.fill(description)

    @allure.step("驗證重複code")
    def validate_duplicate_scope(self, scope_code: str):
        self.base_page.click_expect(self.elements.btn_permission_add_scope)
        expect(self.elements.input_permission_init_scope_code).to_have_count(2)

        self.input_scope_cases = duplicate_permission_code_cases(scope_code)
        element_input = self.elements.input_permission_init_scope_code.last
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, self.input_scope_cases)
        self.base_page.click_expect(self.elements.btn_perms_remove_create.last)

    @allure.step("新增第二筆範圍資料")
    def create_another_scope(self, scope_code: str, scope_name: str, description: str):
        self.base_page.click_expect(self.elements.btn_permission_add_scope)
        expect(self.elements.input_permission_init_scope_code).to_have_count(2)

        self.elements.input_permission_init_scope_code.last.fill(scope_code)
        if ( self.elements.input_permission_init_scope_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()
        
        self.elements.input_permission_init_scope_name.last.fill(scope_name)
        self.elements.input_permission_init_scope_description.last.fill(description)

    @allure.step("點擊下一步到角色新增頁面")
    def click_to_role_next_step(self):
        self.base_page.click_expect(self.elements.btn_next_step, self.elements.btn_permission_add_role)
    

    # Role

    @allure.step("展開角色新增頁面")
    def click_to_extend_role_page(self):
        self.base_page.click_expect(self.elements.btn_permission_add_role)

    @allure.step("驗證輸入並填寫角色代碼")
    def validate_and_fill_role_code(self, role_code: str):
        element_input = self.elements.input_permission_init_role_code
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, PERMISSION_CODE_CASES)
        self.elements.input_permission_init_role_code.fill(role_code)

    @allure.step("驗證輸入並填寫角色名稱")
    def validate_and_fill_role_name(self, role_name: str):
        element_input = self.elements.input_permission_init_role_name
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, PERMISSION_CREATE_NAME_CASES)
        self.elements.input_permission_init_role_name.fill(role_name)

    @allure.step("驗證輸入並填寫角色")
    def validate_and_fill_role_description(self, description: str):
        element_input = self.elements.input_permission_init_role_description
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, PERMISSION_DESCRIPTION_CASES)
        self.elements.input_permission_init_role_description.fill(description)

    @allure.step("選擇第一筆新增的範圍資料")
    def select_created_scope(self, scope_code: str):
        # self.base_page.click_expect(self.elements.btn_permission_scope_list, self.elements.opt_permission_scope_list.first)
        # self.elements.opt_permission_scope_list.first.click()

        self.operate_page.select_list_by_text(
            self.elements.btn_permission_scope_list,
            self.elements.opt_permission_scope_list,
            scope_code,
        )

    @allure.step("驗證重複code")
    def validate_duplicate_role(self, role_code: str):
        self.base_page.click_expect(self.elements.btn_permission_add_role)
        expect(self.elements.input_permission_init_role_code).to_have_count(2)

        self.input_role_cases = duplicate_permission_code_cases(role_code)
        element_input = self.elements.input_permission_init_role_code.last
        element_error = self.elements.msg_field_error

        self.operate_page.verify_input(element_input, element_error, self.input_role_cases)
        self.base_page.click_expect(self.elements.btn_perms_remove_create.last)

    @allure.step("新增第二筆角色資料")
    def create_another_role(self, role_code: str, role_name: str, description: str):
        self.base_page.click_expect(self.elements.btn_permission_add_role)
        expect(self.elements.input_permission_init_role_code).to_have_count(2)

        self.elements.input_permission_init_role_code.last.fill(role_code)
        if ( self.elements.input_permission_init_role_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()

        self.elements.input_permission_init_role_name.last.fill(role_name)
        self.elements.input_permission_init_role_description.last.fill(description)

    @allure.step("新增第三筆範圍資料")
    def create_scope_in_role_page(
        self,
        second_scope_code: str,
        second_scope_name: str,
        third_scope_code: str,
        third_scope_name: str,
    ):
        
        self.operate_page.select_list_by_text(
            self.elements.btn_permission_scope_list.last,
            self.elements.opt_permission_scope_list,
            second_scope_code,
        )

        self.base_page.click_expect(self.elements.btn_permission_role_more_scope.last)
        self.base_page.click_expect(self.elements.btn_permission_scope_list.last, self.elements.opt_permission_scope_list.first)
        option = self.elements.opt_permission_scope_list.filter(
            has_text=f" {second_scope_code} {second_scope_name} "
        )
        expect(option).to_have_attribute("data-p-disabled", "true")

        self.elements.input_perms_role_scope_create_code.fill(third_scope_code)
        self.elements.input_perms_role_scope_create_name.fill(third_scope_name)
        self.base_page.click_expect(self.elements.btn_perms_role_scope_create)

        expect(self.elements.opt_permission_scope_list.first).to_have_text(
            f" {third_scope_code} {third_scope_name} "
        )
        self.elements.opt_permission_scope_list.get_by_text(third_scope_code).click()

    @allure.step("點擊下一步到新增群組頁面")
    def click_to_group_next_step(self):
        self.base_page.click_expect(self.elements.btn_next_step, self.elements.btn_permission_add_group)


# Group

    @allure.step("展開群組新增頁面")
    def click_to_extend_group_page(self):
        self.base_page.click_expect(self.elements.btn_permission_add_group)

    @allure.step("驗證輸入群駔名稱新增資料")
    def validate_and_fill_group_name(self, group_name: str):
        self.input_group_cases = [
            ("8" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位")
        ]
        element_input = self.elements.input_permission_init_group_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_group_cases)
        self.elements.input_permission_init_group_name.fill(group_name)

    @allure.step("驗證輸入群駔描述新增資料")
    def validate_and_fill_group_description(self, description: str):
        self.input_group_cases = [
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_permission_init_group_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_group_cases)
        self.elements.input_permission_init_group_description.fill(description)
    
    @allure.step("邀請團隊成員")
    def invite_team_member(self, member_keyword: str, description: str):
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.first,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            member_keyword,
        )
        self.elements.btn_group_add_member.click()        
        self.elements.input_permission_init_group_description.last.fill(description)

    @allure.step("點擊下一步到新增指定權限頁面")
    def click_to_permission_next_step(self):
        self.base_page.click_expect(self.elements.btn_next_step, self.elements.btn_permission_add_assign)
        
# Assign permission

    @allure.step("新增指定權限成員")
    def create_permission_setting(self, member_keyword: str):
        self.elements.btn_permission_add_assign.click()
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.first,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            member_keyword,
        )

    @allure.step("新增指定權限角色")
    def create_permission_role(self):
        self.operate_page.select_list(self.elements.list_permission_role.first, self.elements.option_dropdown_list.last, 0)
        
    @allure.step("新增指定權限範圍")
    def create_permission_scope(self):
        self.operate_page.select_list(self.elements.list_permission_role.last, self.elements.option_dropdown_list.last, 0)

    @allure.step("新增指定權限描述")
    def create_permission_description(self, description: str):
        self.input_description_cases = [
            ("8" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_permission_remark
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_permission_remark.fill(description)

    @allure.step("點擊下一步到預設權限新增頁面")
    def click_to_default_permission_next_step(self):
        self.base_page.click_expect(self.elements.btn_next_step, self.elements.btn_submit)

    # default permission

    @allure.step("新增預設權限成員角色")
    def create_role_for_member(self):
        self.base_page.click_expect(self.elements.btn_perms_default_role_list)
        self.operate_page.select_list(self.elements.list_perms_default_role_list, self.elements.option_dropdown_list.last, 0)

    @allure.step("新增預設權限成員範圍")
    def create_scope_for_member(self):
        self.base_page.click_expect(self.elements.btn_perms_default_scope_list)
        self.operate_page.select_list(self.elements.list_perms_default_scope_list, self.elements.option_dropdown_list.last, 0)

    @allure.step("確認送出並驗證成功")
    def verify_permission_creation(self):
        self.operate_page.submit_and_confirm()
