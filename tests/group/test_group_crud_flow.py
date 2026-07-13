from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Create group successfully")
def test_group_create_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.group_page.click_to_create_group_page()
    logged_app.group_page.open_create_group_page()
    logged_app.group_page.validate_and_fill_group_name()
    logged_app.group_page.validate_and_fill_group_description()
    logged_app.group_page.invite_group_member()
    logged_app.group_page.submit_and_verify_created()

@allure.title("[GROUP-COPY] Copy group successfully")
def test_group_copy_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.group_page.click_to_group_page()
    logged_app.group_page.open_copy_group_page()
    logged_app.group_page.validate_and_fill_copied_group()
    logged_app.group_page.submit_and_verify_copied()

@allure.title("[GROUP-CRUD] Read group successfully")
def test_group_read_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.group_page.click_to_group_page()
    logged_app.group_page.search_group_with_no_result()
    logged_app.group_page.search_group_by_name()
    logged_app.group_page.filter_groups_by_status()
    logged_app.group_page.sort_groups_by_created_time()

@allure.title("[GROUP-CRUD] Update group successfully")
def test_group_update_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.group_page.click_to_group_page()
    logged_app.group_page.open_update_group_page()
    logged_app.group_page.validate_and_update_group_name()
    logged_app.group_page.validate_and_update_group_description()
    logged_app.group_page.disable_group_status()
    logged_app.group_page.submit_and_verify_updated()

