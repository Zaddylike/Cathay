from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Read group successfully")
def test_group_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.group_page.click_to_group_page()
    logged_app.group_page.search_group_with_no_result()
    logged_app.group_page.search_group_by_name()
    logged_app.group_page.filter_groups_by_status()
    logged_app.group_page.sort_groups_by_created_time()
