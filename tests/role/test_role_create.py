from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Create role successfully")
def test_role_create_success(
    role_app: OmniApp,
    prepared_role_scopes,
    role_cleanup,
):
    role_data = prepared_role_scopes
    role_cleanup("role", role_data.code)
    role_app.role_page.click_to_create_role_page()
    role_app.role_page.validate_and_fill_role_code(role_data.code)
    role_app.role_page.validate_and_fill_role_name(role_data.name)
    role_app.role_page.validate_and_fill_role_description(role_data.description)
    role_app.role_page.select_role_scopes(role_data.scope_code)
    role_app.role_page.submit_and_verify_created(role_data.code)
