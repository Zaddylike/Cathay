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

@allure.title("[ASSIGN-PERMISSION-CRUD] Read assign permission successfully")
def test_assign_permission_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.assign_permission_page.verify_assign_permission_list_visible()
    logged_app.assign_permission_page.search_assign_permission_by_member()
    logged_app.assign_permission_page.search_assign_permission_with_no_result()
    logged_app.assign_permission_page.sort_assign_permissions_by_created_time()

@allure.title("[ASSIGN-PERMISSION-CRUD] Update assign permission successfully")
def test_assign_permission_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.assign_permission_page.open_update_assign_permission_page()
    logged_app.assign_permission_page.replace_assign_role_permission()
    logged_app.assign_permission_page.replace_assign_scope_permission()
    logged_app.assign_permission_page.validate_and_update_description()
    logged_app.assign_permission_page.submit_and_verify_updated()

@allure.title("[ASSIGN-PERMISSION-CRUD] Delete assign permission successfully")
def test_assign_permission_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.assign_permission_page.open_assign_permission_delete_dialog()
    logged_app.assign_permission_page.verify_deleted_input()
    logged_app.assign_permission_page.verify_assign_permission_deleted()
