from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-CRUD] Create scope successfully")
def test_scope_create_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.scope_page.click_to_create_scope_page()
    logged_app.scope_page.validate_and_fill_scope_code()
    logged_app.scope_page.validate_and_fill_scope_name()
    logged_app.scope_page.validate_and_fill_scope_description()
    logged_app.scope_page.validate_duplicate_scope()
    logged_app.scope_page.create_another_scope()
    logged_app.scope_page.submit_and_verify_created()

@allure.title("[SCOPE-CRUD] Read scope successfully")
def test_scope_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.scope_page.search_scope_with_no_result()
    logged_app.scope_page.search_scope_by_code()
    logged_app.scope_page.filter_projects_by_status()
    logged_app.scope_page.sort_projects_by_created_time()

@allure.title("[SCOPE-CRUD] Update scope successfully")
def test_scope_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.scope_page.click_to_update_scope_page()
    logged_app.scope_page.validate_and_update_scope_name()
    logged_app.scope_page.validate_and_update_scope_description()
    logged_app.scope_page.disable_scope_status()
    logged_app.scope_page.submit_and_verify_updated()

@allure.title("[SCOPE-COPY] Copy scope successfully")
def test_scope_copy_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.scope_page.click_to_update_scope_page()
    logged_app.scope_page.validate_and_update_scope_name()
    logged_app.scope_page.validate_and_update_scope_description()
    logged_app.scope_page.disable_scope_status()
    logged_app.scope_page.submit_and_verify_updated()

@allure.title("[SCOPE-CRUD] Delete scope successfully")
def test_scope_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.scope_page.click_to_delete_scope_page()
    logged_app.scope_page.verify_deleted_input()
    logged_app.scope_page.verify_scope_deleted()
