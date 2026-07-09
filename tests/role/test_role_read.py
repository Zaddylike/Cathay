from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Read role successfully")
def test_role_read_success(logged_app: OmniApp):
<<<<<<< HEAD
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
=======
>>>>>>> 80fa955 (update)
    logged_app.role_page.verify_role_list_visible()
    logged_app.role_page.search_role_with_no_result()
    logged_app.role_page.search_role_by_code()
    logged_app.role_page.search_role_by_name()
    logged_app.role_page.filter_roles_by_status()
<<<<<<< HEAD
    logged_app.role_page.sort_roles_by_created_time()
=======
    logged_app.role_page.sort_roles_by_created_time()
>>>>>>> 80fa955 (update)
