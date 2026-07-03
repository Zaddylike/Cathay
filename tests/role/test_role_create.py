from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-CRUD] Create role successfully")
def test_role_create_success(logged_app: OmniApp):
    logged_app.role_page.click_to_create_role_page()
    logged_app.role_page.validate_and_fill_role_code()
    logged_app.role_page.validate_and_fill_role_name()
    logged_app.role_page.validate_and_fill_role_description()
    logged_app.role_page.select_role_scopes()
    logged_app.role_page.validate_duplicate_role()
    logged_app.role_page.create_another_role()
    logged_app.role_page.submit_and_verify_created()
