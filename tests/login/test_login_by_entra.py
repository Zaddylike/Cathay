from app.omni_app import OmniApp


def test_login_by_entra_success(app: OmniApp):
    app.login_page.open_browser()
    app.login_page.verify_title()
    app.login_page.user_login_entra("omnitest3@cathlife.symphox.com", "Omni168168168")
    app.login_page.user_logout()
    app.login_page.change_language("EN")
    app.login_page.change_language("繁中")
    
    