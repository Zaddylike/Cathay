from app.omni_app import OmniApp
from config.settings import GOOGLE_PASSWORD, GOOGLE_USERNAME


def test_login_by_google_success(app: OmniApp):
    app.login_page.open_browser()
    app.login_page.verify_title()
    app.login_page.user_login_google(GOOGLE_USERNAME, GOOGLE_PASSWORD)
    app.login_page.user_logout()
    app.login_page.change_language("EN")
    app.login_page.change_language("繁中")
    
    
