from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-COPY] Copy scope successfully")
def test_scope_copy_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
<<<<<<< HEAD
    logged_app.scope_page.click_to_copy_scope_page()
    logged_app.scope_page.validate_copy_and_fill_code()
    logged_app.scope_page.validate_and_copy_scope_description()
    logged_app.scope_page.submit_and_verify_copied()
=======
    logged_app.scope_page.click_to_update_scope_page()
    logged_app.scope_page.validate_and_update_scope_name()
    logged_app.scope_page.validate_and_update_scope_description()
    logged_app.scope_page.disable_scope_status()
    logged_app.scope_page.submit_and_verify_updated()
>>>>>>> 80fa955 (update)
