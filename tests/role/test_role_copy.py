from app.omni_app import OmniApp
import allure


@allure.title("[ROLE-COPY] Copy role successfully")
def test_role_copy_success(
    permission_settings_app: OmniApp,
    created_role,
    role_cleanup,
):
    role_cleanup("role", created_role.copied_code)
    permission_settings_app.role_page.click_to_copy_role_page(created_role.code)
    permission_settings_app.role_page.validate_copy_and_fill_code(
        created_role.copied_code
    )
    permission_settings_app.role_page.validate_copy_and_fill_name(
        created_role.copied_name
    )
    permission_settings_app.role_page.validate_and_copy_role_description(
        created_role.copied_description
    )
    permission_settings_app.role_page.submit_and_verify_copied(
        created_role.copied_code
    )
