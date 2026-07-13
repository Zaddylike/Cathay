from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-COPY] Copy group successfully")
def test_group_copy_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.group_page.click_to_group_page()
    logged_app.group_page.open_copy_group_page()
    logged_app.group_page.validate_and_fill_copied_group()
    logged_app.group_page.submit_and_verify_copied()
