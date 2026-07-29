import allure
import pytest

from app.omni_app import OmniApp


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Application SSO input fields")
def test_application_sso_field_validation(
    logged_app: OmniApp,
    application_project,
):
    data = application_project

    logged_app.single_sign_on_page.open_to_permission_page(
        data.project_abbreviation
    )
    logged_app.single_sign_on_page.open_to_create_sso_page()
    logged_app.operate_page.click_to_next_step()

    logged_app.single_sign_on_page.create_provider_entraId()
    logged_app.single_sign_on_page.input_entraId_clientId(data.entra_client_id)
    logged_app.single_sign_on_page.input_entraId_secret(data.entra_secret)
    logged_app.single_sign_on_page.input_entraId_tenant(data.entra_tenant)
    logged_app.single_sign_on_page.verify_advanced(
        data.entra_tenant,
        data.entra_attribute,
    )
    logged_app.single_sign_on_page.verify_dup_create()

    logged_app.single_sign_on_page.create_provider_google()
    logged_app.single_sign_on_page.input_google_clientId(data.google_client_id)
    logged_app.single_sign_on_page.input_google_secret(data.google_secret)
    logged_app.single_sign_on_page.switch_whitelist_active()
    logged_app.single_sign_on_page.input_identify_field(
        data.google_identify_field
    )

    logged_app.single_sign_on_page.create_provider_oidc()
    logged_app.single_sign_on_page.input_oidc_setting(data.oidc_value)
    logged_app.operate_page.click_to_next_step()

    logged_app.single_sign_on_page.input_application_name(
        data.sso_application_name
    )
    logged_app.single_sign_on_page.select_tenant()
    logged_app.single_sign_on_page.input_application_redirectUrl(
        data.redirect_url
    )
    logged_app.single_sign_on_page.input_application_logoutUrl(data.logout_url)
    logged_app.single_sign_on_page.setting_date()
    logged_app.single_sign_on_page.submit_sso_and_verify_success()
