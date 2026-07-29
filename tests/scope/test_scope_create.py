from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-CRUD] Create scope successfully")
def test_scope_create_success(
    permission_settings_app: OmniApp,
    scope_data,
    scope_cleanup,
):
    scope_cleanup(scope_data.code)

    permission_settings_app.scope_page.click_to_create_scope_page()
    permission_settings_app.scope_page.validate_and_fill_scope_code(scope_data.code)
    permission_settings_app.scope_page.validate_and_fill_scope_name(scope_data.name)
    permission_settings_app.scope_page.validate_and_fill_scope_description(
        scope_data.description
    )
    permission_settings_app.scope_page.validate_duplicate_scope(scope_data.code)
    permission_settings_app.scope_page.submit_and_verify_created(scope_data.code)

    
