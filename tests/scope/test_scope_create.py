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

