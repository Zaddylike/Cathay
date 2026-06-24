from app.omni_app import OmniApp
from config.settings import ENTRA_PASSWORD, ENTRA_USERNAME


def test_login_by_entra_success(app: OmniApp):
    app.login_page.open_browser()
    app.login_page.verify_title()
    app.login_page.user_login_entra(ENTRA_USERNAME, ENTRA_PASSWORD)
    app.login_page.user_logout()
    app.login_page.change_language("EN")
    app.login_page.change_language("繁中")
    
    
