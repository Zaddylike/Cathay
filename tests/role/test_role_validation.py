import allure
import pytest

from app.omni_app import OmniApp
from config.settings import PERMISSION_SCOPE_CODE


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Role input fields")
def test_role_field_validation(
    permission_settings_app: OmniApp,
    prepared_role_scopes,
    role_cleanup,
):
    data = prepared_role_scopes
    role_cleanup("role", data.code)
    role_cleanup("role", data.copied_code)
    role_page = permission_settings_app.role_page

    role_page.click_to_create_role_page()
    role_page.validate_and_fill_role_code(data.code)
    role_page.validate_and_fill_role_name(data.name)
    role_page.validate_and_fill_role_description(data.description)
    role_page.select_role_scopes(data.scope_code)
    role_page.validate_duplicate_role(data.code)
    role_page.submit_and_verify_created(data.code)

    role_page.click_to_copy_role_page(data.code)
    role_page.validate_copy_and_fill_code(data.copied_code)
    role_page.validate_copy_and_fill_name(data.copied_name)
    role_page.validate_and_copy_role_description(data.copied_description)
    role_page.submit_and_verify_copied(data.copied_code)

    role_page.click_to_update_role_page(data.code)
    role_page.validate_and_update_role_name(data.updated_name)
    role_page.validate_and_update_role_description(data.updated_description)
    role_page.add_role_scope(PERMISSION_SCOPE_CODE)
    role_page.submit_and_verify_updated(data.updated_name)
