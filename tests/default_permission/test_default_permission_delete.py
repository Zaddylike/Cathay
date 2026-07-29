from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Delete default permission successfully")
def test_default_permission_delete_success(
    permission_settings_app: OmniApp,
    created_default_permission,
):
    permission_settings_app.default_permission_page.open_default_permission_delete_dialog(
        created_default_permission.role_code
    )
    permission_settings_app.default_permission_page.verify_deleted_input()
    permission_settings_app.default_permission_page.verify_default_permission_deleted(
        created_default_permission.role_code
    )
