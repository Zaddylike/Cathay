from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Update role successfully")
def test_role_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.role_page.click_to_update_role_page()
    logged_app.role_page.validate_and_update_role_name()
    logged_app.role_page.validate_and_update_role_description()
    logged_app.role_page.update_role_scopes()
    logged_app.role_page.submit_and_verify_updated()
