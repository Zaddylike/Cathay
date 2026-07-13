from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Delete group successfully")
def test_group_delete_success(logged_app: OmniApp):
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.group_page.click_to_group_page()
    logged_app.group_page.open_group_delete_dialog()
    logged_app.group_page.verify_deleted_input()
    logged_app.group_page.verify_group_deleted()
