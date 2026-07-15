from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Read group successfully")
def test_group_read_success(group_app: OmniApp, created_group):
    group_app.group_page.click_to_group_page()
    group_app.group_page.search_group_with_no_result()
    group_app.group_page.search_group_by_name(created_group.name)
    group_app.group_page.filter_groups_by_status()
    group_app.group_page.sort_groups_by_created_time()
