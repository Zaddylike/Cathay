from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Update assign permission successfully")
def test_assign_permission_update_success(
    permission_sso_app: OmniApp,
    created_assign_permission,
):
    permission_sso_app.assign_permission_page.open_update_assign_permission_page(
        created_assign_permission.role_code
    )
    permission_sso_app.assign_permission_page.replace_assign_role_permission(
        created_assign_permission.updated_role_code
    )
    permission_sso_app.assign_permission_page.replace_assign_scope_permission(
        created_assign_permission.updated_scope_code
    )
    permission_sso_app.assign_permission_page.validate_and_update_description(
        created_assign_permission.updated_description
    )
    permission_sso_app.assign_permission_page.submit_and_verify_updated(
        created_assign_permission.updated_role_code
    )
