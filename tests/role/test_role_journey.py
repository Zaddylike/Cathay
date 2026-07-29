from app.omni_app import OmniApp
from config.settings import PERMISSION_SCOPE_CODE
import allure


@allure.title("[ROLE-JOURNEY] Create, read, update, and delete one role")
def test_role_crud_journey(
    permission_settings_app: OmniApp,
    prepared_role_scopes,
    role_cleanup,
):
    role_data = prepared_role_scopes
    role_cleanup("role", role_data.code)
    permission_settings_app.role_page.create_role(
        role_data.code,
        role_data.name,
        role_data.description,
        role_data.scope_code,
    )
    permission_settings_app.role_page.verify_role_list_visible()
    permission_settings_app.role_page.search_role_by_code(role_data.code)
    permission_settings_app.role_page.search_role_by_name(role_data.name)
    permission_settings_app.role_page.click_to_update_role_page(role_data.code)
    permission_settings_app.role_page.validate_and_update_role_name(
        role_data.updated_name
    )
    permission_settings_app.role_page.validate_and_update_role_description(
        role_data.updated_description
    )
    permission_settings_app.role_page.add_role_scope(PERMISSION_SCOPE_CODE)
    permission_settings_app.role_page.submit_and_verify_updated(role_data.updated_name)
    permission_settings_app.role_page.delete_role(role_data.code)
    permission_settings_app.role_page.verify_role_deleted(role_data.code)
