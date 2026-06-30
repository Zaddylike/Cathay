from playwright.sync_api import Page


class ApplicationSsoLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def btn_project_info_permission(self):
        # 專案資訊頁面_身分認證按鈕
        return self.page.locator(".sidebar__list", has=self.page.get_by_text(" 身份認證 ", exact=True))

    @property
    def page_permission(self):
        # 身分驗證頁面_logo
        return self.page.locator(".text-type--content-title")

    @property
    def tab_signon(self):
        # 身分驗證頁面_分頁_單一登入
        return self.page.locator('[role="tablist"] p-tab', has_text=" 單一登入 ")
    
    @property
    def btn_permission_add_sso(self):
        # 身分驗證頁面_單一登入分頁_新增應用端按鈕
        return self.page.locator('[data-p-active="true"] button', has_text=" 新增應用端 ")
    
    @property
    def list_providers(self):
        # 單一登入新增頁面_step.2_供應商清單
        return self.page.locator('[formcontrolname="providerId"] p-select')
    
    @property
    def opt_providers_entraId(self):
        # 單一登入新增頁面_step.2_供應商清單選項
        return self.page.locator('[role="listbox"] p-selectitem [aria-label="Microsoft Entra ID"]')
    
    @property
    def opt_providers_google(self):
        # 單一登入新增頁面_step.2_供應商清單選項
        return self.page.locator('[role="listbox"] p-selectitem [aria-label="GOOGLE"]')

    @property
    def opt_providers_oidc(self):
        # 單一登入新增頁面_step.2_供應商清單選項
        return self.page.locator('[role="listbox"] p-selectitem [aria-label="OIDC"]')

    @property
    def input_entra_clientId(self):
        # 單一登入新增頁面_step.2_用戶端ID
        return self.page.locator('[formcontrolname="clientId"]')

    @property
    def input_entra_client_secret(self):
        # 單一登入新增頁面_step.2_用戶端密鑰
        return self.page.locator('[formcontrolname="clientSecret"]')

    @property
    def input_entra_tenant_id(self):
        # 單一登入新增頁面_step.2_租用戶ID
        return self.page.locator('[formcontrolname="tenantId"]')

    @property
    def btn_entra_advanced_setting(self):
        # 單一登入新增頁面_step.2_進階設定
        return self.page.get_by_text("進階設定")

    @property
    def input_entra_authorization_uri(self):
        # 單一登入新增頁面_step.2_Authorization URI
        return self.page.locator('[formcontrolname="authorizationUri"]')

    @property
    def input_entra_token_uri(self):
        # 單一登入新增頁面_step.2_Token URI
        return self.page.locator('[formcontrolname="tokenUri"]')

    @property
    def input_entra_user_info_uri(self):
        # 單一登入新增頁面_step.2_User Info URI
        return self.page.locator('[formcontrolname="userInfoUri"]')

    @property
    def input_entra_jwk_set_uri(self):
        # 單一登入新增頁面_step.2_JWK Set URI
        return self.page.locator('[formcontrolname="jwkSetUri"]')

    @property
    def input_entra_user_name_attribute_name(self):
        # 單一登入新增頁面_step.2_User Name Attribute Name
        return self.page.locator('[formcontrolname="userNameAttributeName"]')

    @property
    def btn_sso_create_more_provider(self):
        # 新增第三方應用程式按鈕
        return self.page.get_by_role("button", name=" 新增第三方應用程式 ", exact=True)
    
    @property
    def input_google_clientId(self):
        # 單一登入新增頁面_step.2_用戶端ID
        return self.page.locator('[formcontrolname="clientId"]').last

    @property
    def input_google_client_secret(self):
        # 單一登入新增頁面_step.2_用戶端密鑰
        return self.page.locator('[formcontrolname="clientSecret"]').last
    
    @property
    def switch_google_whitelist_active(self):
        #
        return self.page.locator('formcontrolname="whitelistEnabled"').last
    
    @property
    def input_google_identify_field(self):
        #
        return self.page.locator('[formcontrolname="whitelistKey"]').last
    
    @property
    def input_oidc_buttonName(self):
        #
        return self.page.locator('[formcontrolname="buttonName"]').last
    @property
    def input_oidc_clientId(self):
        #
        return self.page.locator('[formcontrolname="clientId"]').last
    @property
    def input_oidc_clientSecret(self):
        #
        return self.page.locator('[formcontrolname="clientSecret"]').last
    @property
    def input_oidc_whitelistKey(self):
        #
        return self.page.locator('[formcontrolname="whitelistKey"]').last
    @property
    def input_oidc_authorizationGrantTypes(self):
        #
        return self.page.locator('[formcontrolname="authorizationGrantTypes"]').last
    @property
    def input_oidc_name(self):
        #
        return self.page.locator('[formcontrolname="name"]').last
    @property
    def input_oidc_authorizationUri(self):
        #
        return self.page.locator('[formcontrolname="authorizationUri"]').last
    @property
    def input_oidc_tokenUri(self):
        #
        return self.page.locator('[formcontrolname="tokenUri"]').last
    @property
    def input_oidc_userInfoUri(self):
        #
        return self.page.locator('[formcontrolname="userInfoUri"]').last
    @property
    def input_oidc_jwkSetUri(self):
        #
        return self.page.locator('[formcontrolname="jwkSetUri"]').last
    @property
    def input_oidc_userNameAttributeName(self):
        #
        return self.page.locator('[formcontrolname="userNameAttributeName"]').last