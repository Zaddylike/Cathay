from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Delete group successfully")
def test_group_delete_success(
    permission_sso_app: OmniApp,
    created_group,
):
    permission_sso_app.group_page.click_to_group_page()
    permission_sso_app.group_page.open_group_delete_dialog(created_group.name)
    permission_sso_app.group_page.verify_deleted_input()
    permission_sso_app.group_page.verify_group_deleted(created_group.name)
