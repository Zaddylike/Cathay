from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Create default permission successfully")
def test_default_permission_create_success(default_permission_app: OmniApp, default_permission_prerequisites, default_permission_cleanup):
    data = default_permission_prerequisites
    default_permission_cleanup("permission", data.role_code)
    default_permission_app.default_permission_page.open_create_default_permission_page()
    default_permission_app.default_permission_page.select_default_role_permission(
        data.role_code
    )
    default_permission_app.default_permission_page.select_default_scope_permission(
        data.scope_code
    )
    default_permission_app.default_permission_page.submit_and_verify_created(
        data.role_code
    )