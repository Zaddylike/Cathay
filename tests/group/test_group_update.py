from app.omni_app import OmniApp
import allure


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
