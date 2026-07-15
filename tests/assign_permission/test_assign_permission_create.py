from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Create assign permission successfully")
def test_assign_permission_create_success(
    assign_permission_app: OmniApp,
    assign_permission_prerequisites,
    assign_permission_cleanup,
):
    data = assign_permission_prerequisites
    assign_permission_cleanup("assignment", data.role_code)
    assign_permission_cleanup("assignment", data.updated_role_code)
    assign_permission_app.assign_permission_page.open_create_assign_permission_page()
    assign_permission_app.assign_permission_page.select_assign_permission_member(
        data.member
    )
    assign_permission_app.assign_permission_page.select_assign_role_permission(
        data.role_code
    )
    assign_permission_app.assign_permission_page.select_assign_scope_permission(
        data.scope_code
    )
    assign_permission_app.assign_permission_page.validate_and_fill_description(
        data.description
    )
    assign_permission_app.assign_permission_page.create_another_assign_permission(
        data.second_member,
        data.updated_role_code,
        data.updated_scope_code,
        data.second_description,
    )
    assign_permission_app.assign_permission_page.submit_and_verify_created(
        data.role_code
    )
