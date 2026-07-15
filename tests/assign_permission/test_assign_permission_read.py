from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Read assign permission successfully")
def test_assign_permission_read_success(assign_permission_app: OmniApp, created_assign_permission):
    assign_permission_app.assign_permission_page.verify_assign_permission_list_visible()
    assign_permission_app.assign_permission_page.search_assign_permission_by_member(created_assign_permission.second_member)
    assign_permission_app.assign_permission_page.search_assign_permission_with_no_result()
    assign_permission_app.assign_permission_page.sort_assign_permissions_by_created_time()
