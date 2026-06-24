from app.omni_app import OmniApp
from config.settings import ACCOUNT_PASSWORD, ACCOUNT_USERNAME


def test_login_by_account_success(app: OmniApp):
    app.login_by_account(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    app.login_page.user_logout()
    app.login_page.change_language("EN")
    app.login_page.change_language("繁中")
