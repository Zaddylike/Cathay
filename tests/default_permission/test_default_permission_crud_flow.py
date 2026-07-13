from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Create default permission successfully")
def test_default_permission_create_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.default_permission_page.open_create_default_permission_page()
    logged_app.default_permission_page.select_default_role_permission()
    logged_app.default_permission_page.select_default_scope_permission()
    logged_app.default_permission_page.submit_and_verify_created()

@allure.title("[DEFAULT-PERMISSION-CRUD] Read default permission successfully")
def test_default_permission_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.default_permission_page.verify_default_permission_list_visible()
    logged_app.default_permission_page.search_default_permission_by_role()
    logged_app.default_permission_page.search_default_permission_by_scope()
    logged_app.default_permission_page.search_default_permission_with_no_result()

@allure.title("[DEFAULT-PERMISSION-CRUD] Update default permission successfully")
def test_default_permission_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.default_permission_page.open_update_default_permission_page()
    logged_app.default_permission_page.replace_default_role_permission()
    logged_app.default_permission_page.replace_default_scope_permission()
    logged_app.default_permission_page.submit_and_verify_updated()

@allure.title("[DEFAULT-PERMISSION-CRUD] Delete default permission successfully")
def test_default_permission_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.default_permission_page.open_default_permission_delete_dialog()
    logged_app.default_permission_page.verify_deleted_input()
    logged_app.default_permission_page.verify_default_permission_deleted()
