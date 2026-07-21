from playwright.sync_api import Page

class ApplicationSsoLocators:
    def __init__(self, page: Page):
        self.page = page

# Entry / Page

    @property
    # 身分驗證頁面_分頁_單一登入
    def tab_signon(self):
        return self.page.locator('[role="tablist"] p-tab', has=self.page.get_by_text("單一登入"))

    @property
    # 身分驗證頁面_單一登入分頁_新增應用端按鈕
    def btn_permission_add_sso(self):
        return self.page.locator('[data-p-active="true"] button', has_text="新增應用端")
    

# Provider Selection

    @property
    # 單一登入新增頁面_step.2_供應商清單
    def list_providers(self):
        return self.page.locator('[formcontrolname="providerId"] p-select')
    

    @property
    # 單一登入新增頁面_step.2_供應商清單選項
    def opt_providers_entraId(self):
        return self.page.locator('[role="listbox"] p-selectitem [aria-label="Microsoft Entra ID"]')
    

    @property
    # 單一登入新增頁面_step.2_供應商清單選項
    def opt_providers_google(self):
        return self.page.locator('[role="listbox"] p-selectitem [aria-label="GOOGLE"]')

    @property
    # 單一登入新增頁面_step.2_供應商清單選項
    def opt_providers_oidc(self):
        return self.page.locator('[role="listbox"] p-selectitem [aria-label="OIDC"]')

    # Entra Provider

    @property
    # 單一登入新增頁面_step.2_用戶端ID
    def input_entra_clientId(self):
        # return self.page.locator('[formcontrolname="clientId"]')
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('entra')).locator('[formcontrolname="clientId"]')
    
    @property
    # 單一登入新增頁面_step.2_用戶端密鑰
    def input_entra_client_secret(self):
        # return self.page.locator('[formcontrolname="clientSecret"]')
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('entra')).locator('[formcontrolname="clientSecret"]')


    @property
    # 單一登入新增頁面_step.2_租用戶ID
    def input_entra_tenant_id(self):
        # return self.page.locator('[formcontrolname="tenantId"]')
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('entra')).locator('[formcontrolname="tenantId"]')

    @property
    # 單一登入新增頁面_step.2_進階設定
    def btn_entra_advanced_setting(self):
        return self.page.get_by_text("進階設定")

    @property
    # 單一登入新增頁面_step.2_Authorization URI
    def input_entra_authorization_uri(self):
        return self.page.locator('[formcontrolname="authorizationUri"]')

    @property
    # 單一登入新增頁面_step.2_Token URI
    def input_entra_token_uri(self):
        return self.page.locator('[formcontrolname="tokenUri"]')

    @property
    # 單一登入新增頁面_step.2_User Info URI
    def input_entra_user_info_uri(self):
        return self.page.locator('[formcontrolname="userInfoUri"]')

    @property
    # 單一登入新增頁面_step.2_JWK Set URI
    def input_entra_jwk_set_uri(self):
        return self.page.locator('[formcontrolname="jwkSetUri"]')

    @property
    # 單一登入新增頁面_step.2_User Name Attribute Name
    def input_entra_user_name_attribute_name(self):
        return self.page.locator('[formcontrolname="userNameAttributeName"]')

    # Google Provider

    @property
    # 新增第三方應用程式按鈕
    def btn_sso_create_more_provider(self):
        return self.page.get_by_role("button", name=" 新增第三方應用程式 ", exact=True)
    
    @property
    # 單一登入新增頁面_step.2_用戶端ID
    def input_google_clientId(self):
        # return self.page.locator('[formcontrolname="clientId"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('google')).locator('[formcontrolname="clientId"]')

    @property
    # 單一登入新增頁面_step.2_用戶端密鑰
    def input_google_client_secret(self):
        # return self.page.locator('[formcontrolname="clientSecret"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('google')).locator('[formcontrolname="clientSecret"]')
    
    @property
    #
    def switch_google_whitelist_active(self):
        # return self.page.locator('[formcontrolname="whitelistEnabled"]').nth(2)
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('google')).locator('[formcontrolname="whitelistEnabled"]').nth(0)


    @property
    #
    def input_google_identify_field(self):
        # return self.page.locator('[formcontrolname="whitelistKey"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('google')).locator('[formcontrolname="whitelistKey"]')

    

# OIDC Provider

    @property
    #
    def input_oidc_buttonName(self):
        return self.page.locator('[formcontrolname="buttonName"]').last

    @property
    #
    def input_oidc_clientId(self):
        # return self.page.locator('[formcontrolname="clientId"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="clientId"]')

    @property
    #
    def input_oidc_clientSecret(self):
        # return self.page.locator('[formcontrolname="clientSecret"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="clientSecret"]')

    @property
    #
    def input_oidc_whitelistKey(self):
        # return self.page.locator('[formcontrolname="whitelistKey"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="whitelistKey"]')
    
    @property
    #
    def input_oidc_authorizationGrantTypes(self):
        # return self.page.locator('[formcontrolname="authorizationGrantTypes"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="authorizationGrantTypes"]')

    @property
    #
    def input_oidc_name(self):
        # return self.page.locator('[formcontrolname="name"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="name"]')

    @property
    #
    def input_oidc_authorizationUri(self):
        # return self.page.locator('[formcontrolname="authorizationUri"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="authorizationUri"]')

    @property
    #
    def input_oidc_tokenUri(self):
        # return self.page.locator('[formcontrolname="tokenUri"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="tokenUri"]')
    

    @property
    #
    def input_oidc_userInfoUri(self):
        # return self.page.locator('[formcontrolname="userInfoUri"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="userInfoUri"]')
    

    @property
    #
    def input_oidc_jwkSetUri(self):
        # return self.page.locator('[formcontrolname="jwkSetUri"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="jwkSetUri"]')

    @property
    #
    def input_oidc_userNameAttributeName(self):
        # return self.page.locator('[formcontrolname="userNameAttributeName"]').last
        return self.page.locator('app-application-single-sign-on p-accordion-panel app-oauth2-registration', has=self.page.get_by_text('自訂設定')).locator('[formcontrolname="userNameAttributeName"]')
    

    # Application Setting

    @property
    #
    def input_application_name(self):
        return self.page.locator('[formcontrolname="name"]').last
    

    @property
    #
    def list_tenants(self):
        return self.page.locator('[formcontrolname="tenantId"]').last

    @property
    #
    def opt_tenant(self):
        return self.page.locator('[role="option"]')

    @property
    #
    def input_application_redirectUrl(self):
        return self.page.locator('[formcontrolname="redirectUri"]').last
    

    @property
    #
    def input_application_logoutUrl(self):
        return self.page.locator('[formcontrolname="logoutRedirectUri"]').last
    

    @property
    #
    def input_application_description(self):
        return self.page.locator('[formcontrolname="description"]').last


    @property
    #
    def dialog_sso_success(self):
        return self.page.locator('[role="dialog"] prompt-dialog__body')