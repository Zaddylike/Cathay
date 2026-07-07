from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Update default permission successfully")
def test_default_permission_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.default_permission_page.open_update_default_permission_page()
    logged_app.default_permission_page.replace_default_role_permission()
    logged_app.default_permission_page.replace_default_scope_permission()
    logged_app.default_permission_page.submit_and_verify_updated()
