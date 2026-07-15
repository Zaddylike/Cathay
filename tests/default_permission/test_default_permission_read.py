from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Read default permission successfully")
def test_default_permission_read_success(
    default_permission_app: OmniApp,
    created_default_permission,
):
    default_permission_app.default_permission_page.verify_default_permission_list_visible()
    default_permission_app.default_permission_page.search_default_permission_by_role(
        created_default_permission.role_code
    )
    default_permission_app.default_permission_page.search_default_permission_by_scope(
        created_default_permission.scope_code
    )
    default_permission_app.default_permission_page.search_default_permission_with_no_result()
