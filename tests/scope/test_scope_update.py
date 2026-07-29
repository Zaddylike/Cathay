from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-CRUD] Update scope successfully")
def test_scope_update_success(
    permission_settings_app: OmniApp,
    created_scope_data,
):
    permission_settings_app.scope_page.click_to_update_scope_page(created_scope_data.code)
    permission_settings_app.scope_page.validate_and_update_scope_name(
        created_scope_data.updated_name
    )
    permission_settings_app.scope_page.validate_and_update_scope_description(
        created_scope_data.updated_description
    )
    permission_settings_app.scope_page.disable_scope_status()
    permission_settings_app.scope_page.submit_and_verify_updated(
        created_scope_data.updated_name
    )
