import allure
import pytest

from app.omni_app import OmniApp


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Application S2S input fields")
def test_application_s2s_field_validation(
    logged_app: OmniApp,
    application_s2s_project,
):
    data = application_s2s_project

    logged_app.server_to_server_page.open_to_permission_page(
        data.project_abbreviation
    )
    logged_app.server_to_server_page.open_to_create_s2s_page()
    logged_app.server_to_server_page.input_s2s_application_name(
        data.s2s_application_name
    )
    logged_app.server_to_server_page.setting_date()
    logged_app.server_to_server_page.input_application_description(
        data.s2s_description
    )
    logged_app.server_to_server_page.continue_to_scope_step()
    logged_app.server_to_server_page.create_scope()
    logged_app.server_to_server_page.input_scope_description(
        data.s2s_scope_description
    )
    logged_app.server_to_server_page.submit_s2s_and_verify_success()
