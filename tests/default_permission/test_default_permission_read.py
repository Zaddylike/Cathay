from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Read default permission successfully")
def test_default_permission_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.default_permission_page.verify_default_permission_list_visible()
    logged_app.default_permission_page.search_default_permission_by_role()
    logged_app.default_permission_page.search_default_permission_by_scope()
    logged_app.default_permission_page.search_default_permission_with_no_result()
