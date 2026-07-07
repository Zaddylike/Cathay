from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Delete assign permission successfully")
def test_assign_permission_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.assign_permission_page.open_assign_permission_delete_dialog()
    logged_app.assign_permission_page.verify_deleted_input()
    logged_app.assign_permission_page.verify_assign_permission_deleted()
