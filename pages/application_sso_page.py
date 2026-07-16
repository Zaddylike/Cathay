import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators.elements import ApplicationSsoElements
from pages.operate_page import OperatePage


class ApplicationSingleSignOnPage:
    def __init__(self, page: Page):
            self.page = page
            self.elements = ApplicationSsoElements(page)
            self.base_page = BasePage(page)
            self.operate_page = OperatePage(page)

    @allure.step("進入專案身分驗證頁面")
    def open_to_permission_page(self, project_abbreviation: str):
        self.operate_page.go_to_permission_page(project_abbreviation)
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
    
    @allure.step("進入單一登入新增頁面")
    def application_exists(self, application_name: str) -> bool:
        """切換到 SSO 頁籤，使用完整 Application 名稱確認 baseline。"""
        self.elements.tab_signon.click()
        expect(self.elements.tab_signon).to_have_attribute("aria-selected", "true")
        self.base_page.wait_loading_disapper()
        return self.page.get_by_text(application_name, exact=True).is_visible()

    @allure.step("Delete SSO application [{application_name}] if it exists")
    def delete_application_if_exists(self, application_name: str) -> bool:
        if not self.application_exists(application_name):
            return False
        return self.operate_page.delete_application_card_if_exists(application_name)

    @allure.step("Open SSO creation page")
    def open_to_create_sso_page(self):
        self.base_page.click_expect(self.elements.tab_signon, self.elements.btn_permission_add_sso)
        self.base_page.click_expect(self.elements.btn_permission_add_sso, self.elements.btn_next_step)
    
    @allure.step("新增Microsoft Entra Id")
    def create_provider_entraId(self):
        self.base_page.click_expect(self.elements.list_providers.last, self.elements.opt_providers_entraId)
        self.base_page.click_expect(self.elements.opt_providers_entraId, self.page.get_by_text("設定 Microsoft Entra ID SSO"))

    @allure.step("驗證輸入用戶端ID新增資料")
    def input_entraId_clientId(self, client_id: str):
        self.input_clientId_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 101, "輸入字數超過限制長度100"),
        ]
        element_input = self.elements.input_entra_clientId
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_clientId_cases)
        self.elements.input_entra_clientId.fill(client_id)

    @allure.step("驗證輸入密鑰新增資料")
    def input_entraId_secret(self, secret: str):
        self.input_secret_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_entra_client_secret
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_secret_cases)
        self.elements.input_entra_client_secret.fill(secret)

    @allure.step("驗證輸入租戶ID新增資料")
    def input_entraId_tenant(self, tenant: str):
        self.input_tenant_cases = [
            ("8" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
        ]
        element_input = self.elements.input_entra_tenant_id
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_tenant_cases)
        self.elements.input_entra_tenant_id.fill(tenant)

    @allure.step("點擊設定進階設定")
    def verify_advanced(self, tenant: str, attribute: str):
        self.base_page.click_expect(self.elements.btn_entra_advanced_setting, self.elements.input_entra_authorization_uri)
        self.operate_page.verify_input_text(self.elements.input_entra_authorization_uri, tenant)
        self.operate_page.verify_input_text(self.elements.input_entra_token_uri, tenant)
        self.operate_page.verify_input_text(self.elements.input_entra_jwk_set_uri, tenant)
        self.base_page.wait_fill(self.elements.input_entra_user_name_attribute_name, attribute)

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
    def input_google_clientId(self, client_id: str):
        self.input_client_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 101, "輸入字數超過限制長度100"),
        ]
        element_input = self.elements.input_google_clientId
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_client_cases)
        self.elements.input_google_clientId.fill(client_id)

    @allure.step("驗證google輸入密鑰")
    def input_google_secret(self, secret: str):
        self.input_secret_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_google_client_secret
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_secret_cases)
        self.elements.input_google_client_secret.fill(secret)

    @allure.step("驗證google設定白名單")
    def switch_whitelist_active(self):
        self.elements.switch_google_whitelist_active.click()
        
    @allure.step("驗證google輸入識別欄位")
    def input_identify_field(self, identify_field: str):
        expect(self.elements.input_google_identify_field).to_be_visible()
        self.elements.input_google_identify_field.fill(identify_field)

    @allure.step("新增OIDC供應商")
    def create_provider_oidc(self):
        self.elements.btn_sso_create_more_provider.click()
        self.base_page.click_expect(self.elements.list_providers.last, self.elements.opt_providers_google)
        expect(self.elements.opt_providers_google).to_contain_class("p-disabled")
        self.base_page.click_expect(self.elements.opt_providers_oidc, self.page.get_by_text("自訂設定"))
        self.page.mouse.wheel(0, 500)
    
    @allure.step("驗證 OIDC 欄位輸入")
    def input_oidc_setting(self, oidc_value: str):
        try:
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
    def input_application_name(self, application_name: str):
        self.input_name_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 41, "輸入字數超過限制長度40"),
        ]
        element_input = self.elements.input_application_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_name_cases)
        self.elements.input_application_name.fill(application_name)

    @allure.step("選擇租戶")
    def select_tenant(self):
        self.operate_page.select_list(self.elements.list_tenants, self.elements.opt_tenant, 0)

    @allure.step("填寫應用端資訊-重新導向網址")
    def input_application_redirectUrl(self, redirect_url: str):
        self.input_redirectUrl_cases = [
            ("https:/e2e/testing/omni", "網址格式錯誤，請重新輸入"),
        ]
        element_input = self.elements.input_application_redirectUrl
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_redirectUrl_cases)
        self.elements.input_application_redirectUrl.fill(redirect_url)

    @allure.step("填寫應用端資訊-登出網址")
    def input_application_logoutUrl(self, logout_url: str):
        self.input_logoutUrl_cases = [
            ("https:/e2e/testing/omni", "網址格式錯誤，請重新輸入"),
        ]
        element_input = self.elements.input_application_logoutUrl
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_logoutUrl_cases)
        self.elements.input_application_logoutUrl.fill(logout_url)

    @allure.step("設定生效日/到期日")
    def setting_date(self):
        self.base_page.click_expect(self.elements.date_picker_endDate, self.elements.dete_picker_arrow_previous)
        self.base_page.click_expect(self.elements.dete_picker_arrow_previous, self.elements.date_picker_day.nth(12))
        self.base_page.click_expect(self.elements.date_picker_day.nth(12))

    @allure.step("驗證確認送出")
    def submit_sso_and_verify_success(self):
        self.operate_page.submit_and_confirm(
            confirm_button=self.elements.btn_dialog_permission_confirm,
        )
