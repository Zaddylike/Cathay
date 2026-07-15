from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Delete role successfully")
def test_role_delete_success(role_app: OmniApp, created_role):
    role_app.role_page.open_role_delete_dialog(created_role.code)
    role_app.role_page.verify_deleted_input()
    role_app.role_page.verify_role_deleted(created_role.code)
