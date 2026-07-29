from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Delete role successfully")
def test_role_delete_success(
    permission_settings_app: OmniApp,
    created_role,
):
    permission_settings_app.role_page.open_role_delete_dialog(created_role.code)
    permission_settings_app.role_page.verify_deleted_input()
    permission_settings_app.role_page.verify_role_deleted(created_role.code)
