from app.omni_app import OmniApp
import allure

@allure.title("[ROLE-CRUD] Create role successfully")
def test_role_create_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.role_page.click_to_create_role_page()
    logged_app.role_page.validate_and_fill_role_code()
    logged_app.role_page.validate_and_fill_role_name()
    logged_app.role_page.validate_and_fill_role_description()
    logged_app.role_page.select_role_scopes()
    logged_app.role_page.submit_and_verify_created()


@allure.title("[ROLE-COPY] Copy role successfully")
def test_role_copy_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.role_page.click_to_copy_role_page()
    logged_app.role_page.validate_copy_and_fill_code()
    logged_app.role_page.validate_copy_and_fill_name()
    logged_app.role_page.validate_and_copy_role_description()
    logged_app.role_page.submit_and_verify_copied()


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


@allure.title("[ROLE-CRUD] Update role successfully")
def test_role_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.role_page.click_to_update_role_page()
    logged_app.role_page.validate_and_update_role_name()
    logged_app.role_page.validate_and_update_role_description()
    logged_app.role_page.update_role_scopes()
    logged_app.role_page.submit_and_verify_updated()


@allure.title("[ROLE-CRUD] Delete role successfully")
def test_role_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.role_page.open_role_delete_dialog()
    logged_app.role_page.verify_deleted_input()
    logged_app.role_page.verify_role_deleted()