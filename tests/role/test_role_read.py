from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Read role successfully")
def test_role_read_success(
    permission_settings_app: OmniApp,
    created_role,
):
    permission_settings_app.role_page.verify_role_list_visible()
    permission_settings_app.role_page.search_role_with_no_result()
    permission_settings_app.role_page.search_role_by_code(created_role.code)
    permission_settings_app.role_page.search_role_by_name(created_role.name)
    permission_settings_app.role_page.filter_roles_by_status()
    permission_settings_app.role_page.sort_roles_by_created_time()
