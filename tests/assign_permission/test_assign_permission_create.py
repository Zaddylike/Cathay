from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Create assign permission successfully")
def test_assign_permission_create_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.assign_permission_page.open_create_assign_permission_page()
    logged_app.assign_permission_page.select_assign_permission_member()
    logged_app.assign_permission_page.select_assign_role_permission()
    logged_app.assign_permission_page.select_assign_scope_permission()
    logged_app.assign_permission_page.validate_and_fill_description()
    logged_app.assign_permission_page.create_another_assign_permission()
    logged_app.assign_permission_page.submit_and_verify_created()
