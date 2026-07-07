from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Update assign permission successfully")
def test_assign_permission_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.assign_permission_page.open_update_assign_permission_page()
    logged_app.assign_permission_page.replace_assign_permission_member()
    logged_app.assign_permission_page.replace_assign_role_permission()
    logged_app.assign_permission_page.replace_assign_scope_permission()
    logged_app.assign_permission_page.validate_and_update_description()
    logged_app.assign_permission_page.submit_and_verify_updated()
