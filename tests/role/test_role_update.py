from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Update role successfully")
def test_role_update_success(role_app: OmniApp, created_role):
    role_app.role_page.click_to_update_role_page(created_role.code)
    role_app.role_page.validate_and_update_role_name(created_role.updated_name)
    role_app.role_page.validate_and_update_role_description(
        created_role.updated_description
    )
    role_app.role_page.update_role_scopes(
        created_role.updated_scope_code,
        created_role.second_scope_code,
    )
    role_app.role_page.submit_and_verify_updated(created_role.updated_name)
