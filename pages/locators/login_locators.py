from playwright.sync_api import Page

class LoginLocators:
    def __init__(self, page: Page):
        self.page = page

    # Account Login

    @property
    # 登入頁面_帳號欄位
    def input_account(self):
        return self.page.get_by_placeholder("請輸入帳號")

    @property
    # 登入頁面_密碼欄位
    def input_password(self):
        return self.page.get_by_placeholder("請輸入密碼")

    # Entra Login

    @property
    # 登入頁面_Entra登入按鈕
    def btn_login_entra(self):
        return self.page.locator(".welcome-box__password-login .welcome-box__oauth2-login--only-microsoft button").first

    @property
    # Entra登入頁面_帳號欄位
    def input_account_entra(self):
        return self.page.get_by_placeholder("someone@example.com")

    @property
    # Entra登入頁面_密碼欄位
    def input_password_entra(self):
        return self.page.get_by_placeholder("密碼")

    @property
    # Entra登入頁面_logo
    def logo_entra(self):
        return self.page.locator(".logo")

    # Google Login

    @property
    # 登入頁面_Google登入按鈕
    def btn_login_google(self):
        return self.page.locator(".welcome-box__password-login .welcome-box__oauth2-login--only-microsoft .google-login button")

    @property
    # Google登入頁面_帳號欄位
    def input_account_google(self):
        return self.page.locator("#identifierId")

    @property
    # Google登入頁面_密碼欄位
    def input_password_google(self):
        return self.page.locator('input[name="Passwd"]')

    # Language

    @property
    # 頁首_語系箭頭
    def language_arrow(self):
        return self.page.locator(".header .language")

    @property
    # 頁首_語系列表
    def language_list(self):
        return self.page.locator(".language .language__dropdown")

    @property
    # 頁首_語系選項_EN
    def language_option_en(self):
        return self.page.locator(".language .language__dropdown-item").get_by_text("EN", exact=True)

    @property
    # 頁首_語系選項_繁中
    def language_option_zh(self):
        return self.page.locator(".language .language__dropdown-item").get_by_text("繁中", exact=True)

    # Session

    @property
    # 使用者選單_登出按鈕
    def btn_logout(self):
        return self.page.locator(".account-action").get_by_text("登出", exact=True)
