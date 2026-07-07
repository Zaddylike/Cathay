from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Read assign permission successfully")
def test_assign_permission_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.assign_permission_page.verify_assign_permission_list_visible()
    logged_app.assign_permission_page.search_assign_permission_by_member()
    logged_app.assign_permission_page.search_assign_permission_with_no_result()
    logged_app.assign_permission_page.sort_assign_permissions_by_created_time()
