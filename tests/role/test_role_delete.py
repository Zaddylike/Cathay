from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Delete role successfully")
def test_role_delete_success(logged_app: OmniApp):
<<<<<<< HEAD
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    logged_app.role_page.open_role_delete_dialog()
    logged_app.role_page.verify_deleted_input()
    logged_app.role_page.verify_role_deleted()
=======
    logged_app.role_page.open_role_delete_dialog()
    logged_app.role_page.verify_delete_confirm_disabled_by_default()
    logged_app.role_page.cancel_role_delete_then_reopen()
    logged_app.role_page.confirm_role_delete()
    logged_app.role_page.verify_role_deleted()
>>>>>>> 80fa955 (update)
