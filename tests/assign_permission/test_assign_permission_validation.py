import allure
import pytest

from app.omni_app import OmniApp


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Assign Permission input fields")
def test_assign_permission_field_validation(
    permission_sso_app: OmniApp,
    assign_permission_prerequisites,
    assign_permission_cleanup,
):
    data = assign_permission_prerequisites
    assign_permission_cleanup("assignment", data.role_code)
    assign_permission_cleanup("assignment", data.updated_role_code)
    assign_page = permission_sso_app.assign_permission_page

    assign_page.open_create_assign_permission_page()
    assign_page.select_assign_permission_member(data.second_member)
    assign_page.select_assign_role_permission(data.role_code)
    assign_page.select_assign_scope_permission(data.scope_code)
    assign_page.validate_and_fill_description(data.description)
    assign_page.submit_and_verify_created(data.role_code)

    assign_page.open_update_assign_permission_page(data.role_code)
    assign_page.replace_assign_role_permission(data.updated_role_code)
    assign_page.replace_assign_scope_permission(data.updated_scope_code)
    assign_page.validate_and_update_description(data.updated_description)
    assign_page.submit_and_verify_updated(data.updated_role_code)
