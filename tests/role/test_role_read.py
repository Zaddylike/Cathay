from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Read role successfully")
def test_role_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.role_page.verify_role_list_visible()
    logged_app.role_page.search_role_with_no_result()
    logged_app.role_page.search_role_by_code()
    logged_app.role_page.search_role_by_name()
    logged_app.role_page.filter_roles_by_status()
    logged_app.role_page.sort_roles_by_created_time()