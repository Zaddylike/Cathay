from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Create role successfully")
def test_role_create_success(logged_app: OmniApp):
<<<<<<< HEAD
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
=======
>>>>>>> 80fa955 (update)
    logged_app.role_page.click_to_create_role_page()
    logged_app.role_page.validate_and_fill_role_code()
    logged_app.role_page.validate_and_fill_role_name()
    logged_app.role_page.validate_and_fill_role_description()
    logged_app.role_page.select_role_scopes()
<<<<<<< HEAD
=======
    logged_app.role_page.validate_duplicate_role()
    logged_app.role_page.create_another_role()
>>>>>>> 80fa955 (update)
    logged_app.role_page.submit_and_verify_created()
