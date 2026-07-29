from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-CRUD] Read scope successfully")
def test_scope_read_success(
    permission_settings_app: OmniApp,
    created_scope_data,
):
    permission_settings_app.scope_page.verify_scope_list_visible()
    permission_settings_app.scope_page.search_scope_with_no_result()
    permission_settings_app.scope_page.search_scope_by_code(created_scope_data.code)
    permission_settings_app.scope_page.search_scope_by_name(created_scope_data.name)
    permission_settings_app.scope_page.filter_projects_by_status()
    permission_settings_app.scope_page.sort_projects_by_created_time()
