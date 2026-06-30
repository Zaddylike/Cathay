from playwright.sync_api import Page, expect
from pages.locators.elements import ApplicationPermissionElements
from pages.base_page import BasePage
from pages.operation_page import OperationPage
import allure

class ApplicationPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ApplicationPermissionElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperationPage(page)

    @allure.step("進入專案身分驗證頁面")
    def open_to_permission_page(self):
        expect(self.elements.list_projects).to_be_visible()
        self.elements.input_search_project.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
        self.elements.list_projects.click()
        self.base_page.click_expect(self.elements.btn_project_info_permission, self.elements.page_permission)
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
    
    @allure.step("進入權限新增頁面")
    def open_to_create_permission_page(self):
        self.base_page.click_expect(self.elements.tab_permission, self.elements.btn_permission_add_permission)
        self.base_page.click_expect(self.elements.btn_permission_add_permission, self.elements.btn_permission_add_scope)

    #scope
    @allure.step("驗證輸入範圍代碼新增資料")
    def validate_and_fill_scope_code(self):
        self.input_scope_cases = [
            ("中文", "只允許半形之英數字及符號：_-."),
            ("", "必填欄位"),
            ("$$$", "只允許半形之英數字及符號：_-."),
            ("ＡＢＣ", "只允許半形之英數字及符號：_-."),
            ("  ", "只允許半形之英數字及符號：_-."),
            ("8" * 21, "輸入字數超過限制長度20"),
        ]
        element_input = self.elements.input_permission_init_scope_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_scope_cases)
        self.elements.input_permission_init_scope_code.fill("e2e-scope-code")

    @allure.step("驗證輸入範圍名稱新增資料")
    def validate_and_fill_scope_name(self):
        self.input_scope_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 41, "輸入字數超過限制長度40"),
        ]
        element_input = self.elements.input_permission_init_scope_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_scope_cases)
        self.elements.input_permission_init_scope_name.fill("e2e-scope-name")

    @allure.step("驗證輸入範圍名稱新增資料")
    def validate_and_fill_scope_description(self):
        self.input_scope_cases = [
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_permission_init_scope_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_scope_cases)
        self.elements.input_permission_init_scope_description.fill("e2e-scope-description")


    @allure.step("驗證重複code")
    def validate_duplicate_scope(self):
        self.elements.btn_permission_add_scope.click()
        self.input_scope_cases = [
            ("e2e-scope-code", " 代碼不可重複 "),
        ]
        element_input = self.elements.input_permission_init_scope_code.last
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_scope_cases)

    @allure.step("新增第二筆範圍資料")
    def create_another_scope(self):
        self.elements.input_permission_init_scope_code.last.fill("e2e-scope-code-2")
        if ( self.elements.input_permission_init_scope_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()
        self.elements.input_permission_init_scope_name.last.fill("e2e-scope-name-2")
        self.elements.input_permission_init_scope_description.last.fill("e2e-scope-description-2")

    @allure.step("點擊下一步到角色新增頁面")
    def click_to_role_next_step(self):
        self.base_page.click_expect(self.elements.btn_nextStep, self.elements.btn_permission_add_role)
    

    # role
    @allure.step("展開角色新增頁面")
    def click_to_extend_role_page(self):
        self.base_page.click_expect(self.elements.btn_permission_add_role)

    @allure.step("驗證輸入角色名稱新增代碼")
    def validate_and_fill_role_code(self):
        self.input_role_cases = [
            ("中文", "只允許半形之英數字及符號：_-."),
            ("", "必填欄位"),
            ("$$$", "只允許半形之英數字及符號：_-."),
            ("ＡＢＣ", "只允許半形之英數字及符號：_-."),
            ("  ", "只允許半形之英數字及符號：_-."),
            ("8" * 21, "輸入字數超過限制長度20"),
        ]
        element_input = self.elements.input_permission_init_role_code
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_role_cases)
        self.elements.input_permission_init_role_code.fill("e2e-role-code")

    @allure.step("驗證輸入角色名稱新增資料")
    def validate_and_fill_role_name(self):
        self.input_role_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 41, "輸入字數超過限制長度40"),
        ]
        element_input = self.elements.input_permission_init_role_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_role_cases)
        self.elements.input_permission_init_role_name.fill("e2e-role-name")

    @allure.step("驗證輸入角色描述新增資料")
    def validate_and_fill_role_description(self):
        self.input_role_cases = [
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_permission_init_role_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_role_cases)
        self.elements.input_permission_init_role_description.fill("e2e-role-description")

    @allure.step("驗證選擇已被新增的範圍資料")
    def select_created_scope(self):
        self.base_page.click_expect(self.elements.btn_permission_scope_list, self.elements.opt_permission_scope_list.first)
        self.elements.opt_permission_scope_list.first.click()

    @allure.step("驗證重複code")
    def validate_duplicate_role(self):
        self.elements.btn_permission_add_role.click()
        self.input_role_cases = [
            ("e2e-role-code", " 代碼不可重複 "),
        ]
        element_input = self.elements.input_permission_init_role_code.last
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_role_cases)

    @allure.step("新增第二筆角色資料")
    def create_another_role(self):
        self.elements.input_permission_init_role_code.last.fill("e2e-role-code-2")
        if ( self.elements.input_permission_init_role_name.last.is_hidden() ): 
            self.elements.arrow_extend_page.last.click()
        self.elements.input_permission_init_role_name.last.fill("e2e-role-name-2")
        self.elements.input_permission_init_role_description.last.fill("e2e-role-description-2")

    @allure.step("新增第三筆範圍資料")
    def create_scope_in_role_page(self):
        self.base_page.click_expect(self.elements.btn_permission_scope_list.last, self.elements.opt_permission_scope_list.first)
        self.base_page.click_expect(self.elements.opt_permission_scope_list.first)

        self.base_page.click_expect(self.elements.btn_permission_role_more_scope.last)
        self.base_page.click_expect(self.elements.btn_permission_scope_list.last, self.elements.opt_permission_scope_list.first)
        option = self.elements.opt_permission_scope_list.filter(has_text=" e2e-scope-code-2 e2e-scope-name-2 ")
        expect(option).to_contain_class("p-disabled")

        self.elements.input_permission_init_scope_code.last.fill("e2e-scope-code-3")
        self.elements.input_permission_init_scope_name.last.fill("e2e-scope-name-3")
        self.elements.btn_dialog_permission_add_scope.click()
        expect(self.elements.opt_permission_scope_list.first).to_have_text(" e2e-scope-code-3 e2e-scope-name-3 ")
        self.elements.opt_permission_scope_list.first.click()

    @allure.step("點擊下一步到新增群組頁面")
    def click_to_group_next_step(self):
        self.base_page.click_expect(self.elements.btn_nextStep, self.elements.btn_permission_add_group)

    #group
    @allure.step("展開群組新增頁面")
    def click_to_extend_group_page(self):
        self.base_page.click_expect(self.elements.btn_permission_add_group)

    @allure.step("驗證輸入群駔名稱新增資料")
    def validate_and_fill_group_name(self):
        self.input_group_cases = [
            ("8" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位")
        ]
        element_input = self.elements.input_permission_init_group_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_group_cases)
        self.elements.input_permission_init_group_name.fill("e2e-group-name")

    @allure.step("驗證輸入群駔描述新增資料")
    def validate_and_fill_group_description(self):
        self.input_group_cases = [
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_permission_init_group_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_group_cases)
        self.elements.input_permission_init_group_description.fill("e2e-group-description")

    # @allure.step("")
    # def (self):
    #     @allure.step("")
    # def (self):
    # @allure.step("")
    # def (self):