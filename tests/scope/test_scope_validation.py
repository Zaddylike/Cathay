import allure
import pytest

from app.omni_app import OmniApp


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Scope input fields")
def test_scope_field_validation(
    permission_settings_app: OmniApp,
    scope_data,
    scope_cleanup,
):
    scope_cleanup(scope_data.code)
    scope_cleanup(scope_data.copied_code)
    scope_page = permission_settings_app.scope_page

    scope_page.click_to_create_scope_page()
    scope_page.validate_and_fill_scope_code(scope_data.code)
    scope_page.validate_and_fill_scope_name(scope_data.name)
    scope_page.validate_and_fill_scope_description(scope_data.description)
    scope_page.validate_duplicate_scope(scope_data.code)
    scope_page.submit_and_verify_created(scope_data.code)

    scope_page.click_to_copy_scope_page(scope_data.code)
    scope_page.validate_copy_and_fill_code(scope_data.copied_code)
    scope_page.validate_copy_and_fill_name(scope_data.copied_name)
    scope_page.validate_and_copy_scope_description(scope_data.copied_description)
    scope_page.submit_and_verify_copied(scope_data.copied_code)

    scope_page.click_to_update_scope_page(scope_data.code)
    scope_page.validate_and_update_scope_name(scope_data.updated_name)
    scope_page.validate_and_update_scope_description(scope_data.updated_description)
    scope_page.disable_scope_status()
    scope_page.submit_and_verify_updated(scope_data.updated_name)
