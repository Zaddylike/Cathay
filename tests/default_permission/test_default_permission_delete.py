from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-CRUD] Delete default permission successfully")
def test_default_permission_delete_success(
    default_permission_app: OmniApp,
    created_default_permission,
):
    default_permission_app.default_permission_page.open_default_permission_delete_dialog(
        created_default_permission.role_code
    )
    default_permission_app.default_permission_page.verify_deleted_input()
    default_permission_app.default_permission_page.verify_default_permission_deleted(
        created_default_permission.role_code
    )
