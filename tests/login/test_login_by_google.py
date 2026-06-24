from app.omni_app import OmniApp


def test_login_by_google_success(app: OmniApp):
    app.login_page.open_browser()
    app.login_page.verify_title()
    app.login_page.user_login_google("", "")
    app.login_page.user_logout()
    app.login_page.change_language("EN")
    app.login_page.change_language("繁中")
    
    