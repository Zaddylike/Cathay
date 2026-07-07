from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Delete default permission successfully")
def test_default_permission_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.default_permission_page.open_default_permission_delete_dialog()
    logged_app.default_permission_page.verify_deleted_input()
    logged_app.default_permission_page.verify_default_permission_deleted()
