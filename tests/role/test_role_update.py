from app.omni_app import OmniApp
from config.settings import PERMISSION_SCOPE_CODE
import allure


@allure.title("[ROLE-CRUD] Update role successfully")
def test_role_update_success(
    permission_settings_app: OmniApp,
    created_role,
):
    permission_settings_app.role_page.click_to_update_role_page(created_role.code)
    permission_settings_app.role_page.validate_and_update_role_name(
        created_role.updated_name
    )
    permission_settings_app.role_page.validate_and_update_role_description(
        created_role.updated_description
    )
    permission_settings_app.role_page.add_role_scope(PERMISSION_SCOPE_CODE)
    permission_settings_app.role_page.submit_and_verify_updated(
        created_role.updated_name
    )
