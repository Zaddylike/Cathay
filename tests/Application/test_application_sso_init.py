from app.omni_app import OmniApp
import allure


@allure.title("初始化 單一登入")
def test_single_sign_on_init_success(logged_app: OmniApp):
    logged_app.single_signon_page.open_to_permission_page()
    logged_app.single_signon_page.open_to_create_sso_page()
    logged_app.single_signon_page.click_to_next_step()
    logged_app.single_signon_page.create_provider_entraId()
    logged_app.single_signon_page.input_entraId_clientId()
    logged_app.single_signon_page.input_entraId_secret()
    logged_app.single_signon_page.input_entraId_tenant()
    logged_app.single_signon_page.verify_advanced()

    logged_app.single_signon_page.verify_dup_create()
    logged_app.single_signon_page.create_provider_google()
    logged_app.single_signon_page.input_google_clientId()
    logged_app.single_signon_page.input_google_secret()
    logged_app.single_signon_page.switch_whitelist_active()
    logged_app.single_signon_page.input_identify_field()
    logged_app.single_signon_page.create_provider_oidc()
    logged_app.single_signon_page.input_oidc_setting()
    logged_app.single_signon_page.click_to_next_step()

