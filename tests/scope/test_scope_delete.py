from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-CRUD] Delete scope successfully")
def test_scope_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.scope_page.click_to_delete_scope_page()
    logged_app.scope_page.verify_scope_deleted()
