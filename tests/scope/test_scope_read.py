from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-CRUD] Read scope successfully")
def test_scope_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.scope_page.search_scope_with_no_result()
    logged_app.scope_page.search_scope_by_code()
<<<<<<< HEAD
    logged_app.scope_page.search_scope_by_name()
    logged_app.scope_page.filter_projects_by_status()
    logged_app.scope_page.sort_projects_by_created_time()
=======
    logged_app.scope_page.filter_projects_by_status()
    logged_app.scope_page.sort_projects_by_created_time()
>>>>>>> 80fa955 (update)
