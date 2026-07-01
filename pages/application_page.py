from playwright.sync_api import Page, expect
from pages.locators.elements import ApplicationPermissionElements, ApplicationSsoElements, ApplicationS2sElements
from pages.base_page import BasePage
from pages.operation_page import OperationPage
import allure

class ApplicationSingleSignOnPage:
    def __init__(self, page: Page):
            self.page = page
            self.elements = ApplicationSsoElements(page)
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
    
    @allure.step("進入單一登入新增頁面")
    def open_to_create_sso_page(self):
        self.base_page.click_expect(self.elements.tab_signon, self.elements.btn_permission_add_sso)
        self.base_page.click_expect(self.elements.btn_permission_add_sso, self.elements.btn_nextStep)

    @allure.step("點擊下一步")    
    def click_to_next_step(self):
        self.elements.btn_nextStep.click()
    
    @allure.step("新增Microsoft Entra Id")
    def create_provider_entraId(self):
        self.base_page.click_expect(self.elements.list_providers.last, self.elements.opt_providers_entraId)
        self.base_page.click_expect(self.elements.opt_providers_entraId, self.page.get_by_text("設定 Microsoft Entra ID SSO"))
    
    @allure.step("驗證輸入用戶端ID新增資料")
    def input_entraId_clientId(self):
        self.input_client_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 101, "輸入字數超過限制長度100"),
        ]
        element_input = self.elements.input_entra_clientId
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_client_cases)
        self.elements.input_entra_clientId.fill("e2e-testing-clientId")

    @allure.step("驗證輸入密鑰新增資料")
    def input_entraId_secret(self):
        self.input_secret_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_entra_client_secret
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_secret_cases)
        self.elements.input_entra_client_secret.fill("e2e-testing-secret")

    @allure.step("驗證輸入租戶ID新增資料")
    def input_entraId_tenant(self):
        self.input_tenant_cases = [
            ("8" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_entra_tenant_id
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_tenant_cases)
        self.elements.input_entra_tenant_id.fill("e2e-testing-tenant")

    @allure.step("點擊設定進階設定")
    def verify_advanced(self):
        self.base_page.click_expect(self.elements.btn_entra_advanced_setting)
        expect(self.elements.input_entra_authorization_uri).to_be_visible()

        self.operate_page.verify_input_text(self.elements.input_entra_authorization_uri, "e2e-testing-tenant")
        self.operate_page.verify_input_text(self.elements.input_entra_token_uri, "e2e-testing-tenant")
        self.operate_page.verify_input_text(self.elements.input_entra_jwk_set_uri, "e2e-testing-tenant")
        self.elements.input_entra_user_name_attribute_name.fill("e2e-tseting-entra-attr")

    @allure.step("點擊已新增供應商")
    def verify_dup_create(self):
        self.elements.btn_sso_create_more_provider.click()
        self.base_page.click_expect(self.elements.list_providers.last, self.elements.opt_providers_entraId)
        expect(self.elements.opt_providers_entraId).to_contain_class("p-disabled")


    @allure.step("新增Google供應商")
    def create_provider_google(self):
        self.base_page.click_expect(self.elements.opt_providers_google, self.page.get_by_text("設定 GOOGLE SSO"))
        self.page.mouse.wheel(0, 500)
    
    @allure.step("驗證google輸入用戶端ID")
    def input_google_clientId(self):
        self.input_client_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 101, "輸入字數超過限制長度100"),
        ]
        element_input = self.elements.input_google_clientId
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_client_cases)
        self.elements.input_google_clientId.fill("e2e-google-clientId")

    @allure.step("驗證google輸入密鑰")
    def input_google_secret(self):
        self.input_secret_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_google_client_secret
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_secret_cases)
        self.elements.input_google_client_secret.fill("e2e-google-secret")

    @allure.step("驗證google設定白名單")
    def switch_whitelist_active(self):
        self.elements.switch_google_whitelist_active.click()
        
    @allure.step("驗證google輸入識別欄位")
    def input_identify_field(self):
        expect(self.elements.input_google_identify_field).to_be_visible()
        self.elements.input_google_identify_field.fill("e2e-google-testing")

    @allure.step("新增OIDC供應商")
    def create_provider_oidc(self):
        self.elements.btn_sso_create_more_provider.click()
        self.base_page.click_expect(self.elements.list_providers.last, self.elements.opt_providers_google)
        expect(self.elements.opt_providers_google).to_contain_class("p-disabled")
        self.base_page.click_expect(self.elements.opt_providers_oidc, self.page.get_by_text("自訂設定"))
        self.page.mouse.wheel(0, 500)
    
    @allure.step("驗證 OIDC 欄位輸入")
    def input_oidc_setting(self):
        try:
            oidc_value = "e2e-oidc-name"
            self.elements.switch_google_whitelist_active.click()
            expect(self.elements.switch_google_whitelist_active).to_contain_class('p-radiobutton-checked')

            oidc_inputs = [
                self.elements.input_oidc_buttonName,
                self.elements.input_oidc_clientId,
                self.elements.input_oidc_clientSecret,
                self.elements.input_oidc_name,
                self.elements.input_oidc_authorizationUri,
                self.elements.input_oidc_tokenUri,
                self.elements.input_oidc_userInfoUri,
                self.elements.input_oidc_jwkSetUri,
                self.elements.input_oidc_userNameAttributeName,
            ]

            for input_element in oidc_inputs:
                input_element.fill(oidc_value)
                expect(input_element).to_have_value(oidc_value)
            
        except Exception as e:
            raise AssertionError(f"Failed to input oidc field: {e}")
        
    @allure.step("填寫應用端資訊-用戶端名稱")
    def input_application_name(self):
        self.input_name_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 41, "輸入字數超過限制長度40"),
        ]
        element_input = self.elements.input_application_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_application_name.fill("e2e-application-name")

    @allure.step("選擇租戶")
    def select_tenant(self):
        self.operate_page.select_list(self.elements.list_tenants, self.elements.opt_tenant, 0)

    @allure.step("填寫應用端資訊-重新導向網址")
    def input_application_redirectUrl(self):
        self.input_redirectUrl_cases = [
            ("https:/e2e/testing/omni", "網址格式錯誤，請重新輸入"),
        ]
        element_input = self.elements.input_application_redirectUrl
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_redirectUrl_cases)
        self.elements.input_application_redirectUrl.fill("https://e2e/testing/omni")

    @allure.step("填寫應用端資訊-登出網址")
    def input_application_logoutUrl(self):
        self.input_logoutUrl_cases = [
            ("https:/e2e/testing/omni", "網址格式錯誤，請重新輸入"),
        ]
        element_input = self.elements.input_application_logoutUrl
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_logoutUrl_cases)
        self.elements.input_application_logoutUrl.fill("https://e2e/testing/omni")

    @allure.step("設定生效日/到期日")
    def setting_date(self):
        self.base_page.click_expect(self.elements.date_picker_endDate, self.elements.dete_picker_arrow_previous)
        self.base_page.click_expect(self.elements.dete_picker_arrow_previous, self.elements.date_picker_day.nth(12))
        self.base_page.click_expect(self.elements.date_picker_day.nth(12))

    @allure.step("驗證確認送出")
    def submit_sso_and_verify_success(self):
        expect(self.elements.btn_submit).to_be_enabled()
        self.base_page.click_expect(self.elements.btn_submit, self.elements.dialog_page)
        self.base_page.click_expect(self.elements.btn_dialog_permission_confirm)


class ApplicationServerToServerPage:
    def __init__(self, page: Page):
            self.page = page
            self.elements = ApplicationS2sElements(page)
            self.base_page = BasePage(page)
            self.operate_page = OperationPage(page)
    
    @allure.step("點擊下一步")    
    def click_to_next_step(self):
        self.elements.btn_nextStep.click()

    @allure.step("進入專案身分驗證頁面")
    def open_to_permission_page(self):
        expect(self.elements.list_projects).to_be_visible()
        self.elements.input_search_project.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
        self.elements.list_projects.click()
        self.base_page.click_expect(self.elements.btn_project_info_permission, self.elements.page_permission)
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
    
    @allure.step("進入伺服器串接新增頁面")
    def open_to_create_s2s_page(self):
        self.base_page.click_expect(self.elements.tab_s2s, self.elements.btn_permission_add_s2s)
        self.base_page.click_expect(self.elements.btn_permission_add_s2s, self.elements.btn_nextStep)

    @allure.step("驗證輸入應用端名稱新增資料")
    def input_s2s_application_name(self):
        self.input_s2s_application_name_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 101, "輸入字數超過限制長度100"),
        ]
        element_input = self.elements.input_s2s_application_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_s2s_application_name_cases)
        self.elements.input_s2s_application_name.fill("e2e-testing-application-name")

    @allure.step("設定生效日/到期日")
    def setting_date(self):
        self.base_page.click_expect(self.elements.date_picker_endDate, self.elements.date_picker_panel)
        self.base_page.click_expect(self.elements.dete_picker_arrow_previous, self.elements.date_picker_day.nth(12))
        self.base_page.click_expect(self.elements.date_picker_day.nth(12))
    
    @allure.step("輸入驗證描述欄位")
    def input_application_description(self):
        self.input_s2s_description_name_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_s2s_application_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_s2s_description_name_cases)
        self.elements.input_s2s_application_description.fill("e2e-testing-application-description")

    @allure.step("新增範圍")
    def create_scope(self):
        self.elements.btn_s2s_add_scope.click()
        self.operate_page.select_list(self.elements.list_s2s_scope, self.elements.opt_item, 0)

    @allure.step("驗證輸入描述")
    def input_scope_description(self):
        self.elements.input_s2s_application_description.fill("e2e-testing-application-description")

    @allure.step("新增送出")
    def submit_s2s_and_verify_success(self):
        expect(self.elements.btn_submit).to_be_enabled()
        self.base_page.click_expect(self.elements.btn_submit, self.elements.dialog_page)
        self.base_page.click_expect(self.elements.btn_dialog_permission_confirm)


class ApplicationPermissionPage:
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
    
    @allure.step("邀請團隊成員")
    def invite_team_member(self):
        self.elements.btn_filter_to_search.click()
        self.elements.input_member_advanced_search.fill("測試人員3")
        self.elements.checkbox_add_member.click()
        self.elements.btn_memberadd_filter_add_search_confirm.click()
        self.elements.btn_group_add_member.click()        
        self.elements.input_permission_init_group_description.last.fill("e2e-group-description-member")

    @allure.step("點擊下一步到新增指定權限頁面")
    def click_to_permission_next_step(self):
        self.base_page.click_expect(self.elements.btn_nextStep, self.elements.btn_permission_add_group)

    @allure.step("新增指定權限成員")
    def create_permission_setting(self):
        self.elements.btn_permission_add_permission.click()
        self.elements.btn_filter_to_search.click()
        self.elements.input_member_advanced_search.fill("測試人員3")
        self.elements.checkbox_add_member.click()
        self.elements.btn_memberadd_filter_add_search_confirm.click()

    @allure.step("新增指定權限角色")
    def create_permission_role(self):
        self.operate_page.select_list(self.elements.list_permission_role.first, self.elements.opt_item.last, 0)
        
    @allure.step("新增指定權限範圍")
    def create_permission_scope(self):
        self.operate_page.select_list(self.elements.list_permission_role.last, self.elements.opt_item.last, 0)

    @allure.step("新增指定權限描述")
    def create_permission_description(self):
        self.input_description_cases = [
            ("8" * 201, "輸入字數超過限制長度200")
        ]
        element_input = self.elements.input_permission_remark
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_description_cases)
        self.elements.input_permission_remark.fill("e2e-permission-description")

    @allure.step("展開指定權限新增頁面")
    def click_to_extend_permission_page(self):
        self.base_page.click_expect(self.elements.btn_permission_add_group)

    @allure.step("新增預設權限成員角色")
    def create_role_for_member(self):
        self.elements.btn_permission_add_role.click()
        self.operate_page.select_list(self.elements.list_permission_role.first, self.elements.opt_item.last, 0)

    @allure.step("新增預設權限成員範圍")
    def create_scope_for_member(self):
        self.elements.btn_permission_add_scope.click()
        self.operate_page.select_list(self.elements.list_permission_role.last, self.elements.opt_item.last, 0)

    @allure.step("確認送出並驗證成功")
    def verify_permission_creation(self):
        expect(self.elements.btn_submit).to_be_enabled()
        self.base_page.click_expect(self.elements.btn_submit, self.elements.dialog_page)
        self.base_page.click_expect(self.elements.btn_dialog_checked)