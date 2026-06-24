from app.omni_app import OmniApp


def test_login_by_account_success(app: OmniApp):
    app.login_by_account("testuser01", "testuser01")
    app.login_page.user_logout()
    app.login_page.change_language("EN")
    app.login_page.change_language("繁中")