import allure
import pytest

from app.omni_app import OmniApp


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Permission Init input fields")
def test_application_permission_field_validation(
    logged_app: OmniApp,
    application_permission_init_project,
):
    data = application_permission_init_project
    permission_page = logged_app.application_permission_page

    permission_page.open_to_permission_page(data.project_abbreviation)
    permission_page.open_to_create_permission_page()

    permission_page.validate_and_fill_scope_code(data.scope_code)
    permission_page.validate_and_fill_scope_name(data.scope_name)
    permission_page.validate_and_fill_scope_description(data.scope_description)
    permission_page.validate_duplicate_scope(data.scope_code)
    permission_page.create_another_scope(
        data.second_scope_code,
        data.second_scope_name,
        data.second_scope_description,
    )
    permission_page.click_to_role_next_step()

    permission_page.click_to_extend_role_page()
    permission_page.validate_and_fill_role_code(data.role_code)
    permission_page.validate_and_fill_role_name(data.role_name)
    permission_page.validate_and_fill_role_description(data.role_description)
    permission_page.select_created_scope(data.scope_code)
    permission_page.validate_duplicate_role(data.role_code)
    permission_page.create_another_role(
        data.second_role_code,
        data.second_role_name,
        data.second_role_description,
    )
    permission_page.create_scope_in_role_page(
        data.second_scope_code,
        data.second_scope_name,
        data.third_scope_code,
        data.third_scope_name,
    )
    permission_page.click_to_group_next_step()

    permission_page.click_to_extend_group_page()
    permission_page.validate_and_fill_group_name(data.group_name)
    permission_page.validate_and_fill_group_description(data.group_description)
    permission_page.invite_team_member(
        data.member_keyword,
        data.group_member_description,
    )
    permission_page.click_to_permission_next_step()

    permission_page.create_permission_setting(data.member_keyword)
    permission_page.create_permission_role()
    permission_page.create_permission_scope()
    permission_page.create_permission_description(data.assignment_description)
    permission_page.click_to_default_permission_next_step()

    permission_page.create_role_for_member()
    permission_page.create_scope_for_member()
    permission_page.verify_permission_creation()
