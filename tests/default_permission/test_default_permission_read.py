from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Read default permission successfully")
def test_default_permission_read_success(
    permission_settings_app: OmniApp,
    created_default_permission,
):
    permission_settings_app.default_permission_page.verify_default_permission_list_visible()
    permission_settings_app.default_permission_page.search_default_permission_by_role(
        created_default_permission.role_code
    )
    permission_settings_app.default_permission_page.search_default_permission_by_scope(
        created_default_permission.scope_code
    )
    permission_settings_app.default_permission_page.search_default_permission_with_no_result()
