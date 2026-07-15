from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-JOURNEY] Create, read, update, and delete")
def test_assign_permission_crud_journey(assign_permission_app: OmniApp, assign_permission_prerequisites, assign_permission_cleanup ):
    data = assign_permission_prerequisites
    assign_permission_cleanup("assignment", data.role_code)
    assign_permission_cleanup("assignment", data.updated_role_code)
    assign_permission_app.assign_permission_page.create_assign_permission(
        data.second_member,
        data.role_code,
        data.scope_code,
        data.description,
    )
    assign_permission_app.assign_permission_page.search_assign_permission_by_member(data.second_member)
    assign_permission_app.assign_permission_page.open_update_assign_permission_page(data.role_code)
    assign_permission_app.assign_permission_page.replace_assign_role_permission(data.updated_role_code)
    assign_permission_app.assign_permission_page.replace_assign_scope_permission(data.updated_scope_code)
    assign_permission_app.assign_permission_page.validate_and_update_description(data.updated_description)
    assign_permission_app.assign_permission_page.submit_and_verify_updated(data.updated_role_code)
    assign_permission_app.assign_permission_page.delete_assign_permission(data.updated_role_code)
    assign_permission_app.assign_permission_page.verify_assign_permission_deleted(data.updated_role_code)
