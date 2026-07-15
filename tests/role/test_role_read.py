from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Read role successfully")
def test_role_read_success(role_app: OmniApp, created_role):
    role_app.role_page.verify_role_list_visible()
    role_app.role_page.search_role_with_no_result()
    role_app.role_page.search_role_by_code(created_role.code)
    role_app.role_page.search_role_by_name(created_role.name)
    role_app.role_page.filter_roles_by_status()
    role_app.role_page.sort_roles_by_created_time()
