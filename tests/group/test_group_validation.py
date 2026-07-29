import allure
import pytest

from app.omni_app import OmniApp


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Group input fields")
def test_group_field_validation(
    permission_sso_app: OmniApp,
    group_data,
    group_cleanup,
):
    group_cleanup(group_data.name)
    group_cleanup(group_data.updated_name)
    group_page = permission_sso_app.group_page

    group_page.click_to_create_group_page()
    group_page.open_create_group_page()
    group_page.validate_and_fill_group_name(group_data.name)
    group_page.validate_and_fill_group_description(group_data.description)
    group_page.invite_group_member(
        group_data.member_keyword,
        group_data.description,
    )
    group_page.submit_and_verify_created(group_data.name)

    group_page.click_to_group_page()
    group_page.open_update_group_page(group_data.name)
    group_page.validate_and_update_group_name(group_data.updated_name)
    group_page.validate_and_update_group_description(group_data.updated_description)
    group_page.disable_group_status()
    group_page.submit_and_verify_updated(group_data.updated_name)
