from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Delete assign permission successfully")
def test_assign_permission_delete_success(assign_permission_app: OmniApp, created_assign_permission):
    assign_permission_app.assign_permission_page.open_assign_permission_delete_dialog(created_assign_permission.role_code)
    assign_permission_app.assign_permission_page.verify_deleted_input()
    assign_permission_app.assign_permission_page.verify_assign_permission_deleted(created_assign_permission.role_code)
    
