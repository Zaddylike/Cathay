from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Update default permission successfully")
def test_default_permission_update_success(
    default_permission_app: OmniApp,
    created_default_permission,
):
    default_permission_app.default_permission_page.open_update_default_permission_page()
    default_permission_app.default_permission_page.replace_default_role_permission(
        created_default_permission.updated_role_code
    )
    default_permission_app.default_permission_page.replace_default_scope_permission(
        created_default_permission.updated_scope_code
    )
    default_permission_app.default_permission_page.submit_and_verify_updated(
        created_default_permission.updated_role_code
    )
