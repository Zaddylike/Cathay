from app.omni_app import OmniApp
import allure


@allure.title("初始化 權限設定")
def test_application_init_success(logged_app: OmniApp):
    logged_app.application_page.open_to_permission_page()
    logged_app.application_page.open_to_create_permission_page()
    logged_app.application_page.validate_and_fill_scope_code()
    logged_app.application_page.validate_and_fill_scope_name()
    logged_app.application_page.validate_and_fill_scope_description()
    logged_app.application_page.validate_duplicate_scope()
    logged_app.application_page.create_another_scope()
    logged_app.application_page.click_to_role_next_step()

    logged_app.application_page.click_to_extend_role_page()
    logged_app.application_page.validate_and_fill_role_code()
    logged_app.application_page.validate_and_fill_role_name()
    logged_app.application_page.validate_and_fill_role_description()
    logged_app.application_page.select_created_scope()
    logged_app.application_page.validate_duplicate_role()
    logged_app.application_page.create_another_role()
    logged_app.application_page.create_scope_in_role_page()
    logged_app.application_page.click_to_group_next_step()

    logged_app.application_page.click_to_extend_group_page()
    logged_app.application_page.validate_and_fill_group_name()
    logged_app.application_page.validate_and_fill_group_description()
    # logged_app.application_page.
    # logged_app.application_page.

