from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-COPY] Copy role successfully")
def test_role_copy_success(logged_app: OmniApp):
<<<<<<< HEAD
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
=======
>>>>>>> 80fa955 (update)
    logged_app.role_page.click_to_copy_role_page()
    logged_app.role_page.validate_copy_and_fill_code()
    logged_app.role_page.validate_copy_and_fill_name()
    logged_app.role_page.validate_and_copy_role_description()
<<<<<<< HEAD
=======
    logged_app.role_page.enable_role_status()
>>>>>>> 80fa955 (update)
    logged_app.role_page.submit_and_verify_copied()
