from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Read group successfully")
def test_group_read_success(
    permission_sso_app: OmniApp,
    created_group,
):
    permission_sso_app.group_page.click_to_group_page()
    permission_sso_app.group_page.search_group_with_no_result()
    permission_sso_app.group_page.search_group_by_name(created_group.name)
    permission_sso_app.group_page.filter_groups_by_status()
    permission_sso_app.group_page.sort_groups_by_created_time()
