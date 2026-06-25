from playwright.sync_api import Page


class LoginLocators:
    def __init__(self, page: Page):
        self.page = page


    @property
    def btn_login_entra(self):
        return self.page.locator(".welcome-box__password-login .welcome-box__oauth2-login--only-microsoft button").first
    

    @property
    def btn_login_google(self):
        return self.page.locator(".welcome-box__password-login .welcome-box__oauth2-login--only-microsoft .google-login button")
    

    @property
    def btn_logout(self):
        return self.page.locator(".account-action").get_by_text("登出", exact=True)
    

    @property
    def input_account(self):
        return self.page.get_by_placeholder("請輸入帳號")
    

    @property
    def input_account_entra(self):
        return self.page.get_by_placeholder("someone@example.com")
    

    @property
    def input_account_google(self):
        return self.page.locator("#identifierId")
    

    @property
    def input_password(self):
        return self.page.get_by_placeholder("請輸入密碼")
    

    @property
    def input_password_entra(self):
        return self.page.get_by_placeholder("密碼")
    

    @property
    def input_password_google(self):
        return self.page.locator('input[name="Passwd"]')
    

    @property
    def language_arrow(self):
        return self.page.locator(".header .language")
    

    @property
    def language_list(self):
        return self.page.locator(".language .language__dropdown")
    

    @property
    def language_option_en(self):
        return self.page.locator(".language .language__dropdown-item").get_by_text("EN", exact=True)
    

    @property
    def language_option_zh(self):
        return self.page.locator(".language .language__dropdown-item").get_by_text("繁中", exact=True)
    

    @property
    def logo_entra(self):
        return self.page.locator(".logo")
