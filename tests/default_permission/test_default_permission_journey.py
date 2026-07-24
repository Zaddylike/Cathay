from app.omni_app import OmniApp
import allure


@allure.title("[DEFAULT-PERMISSION-JOURNEY] Create, read, update, and delete")
def test_default_permission_crud_journey(
    default_permission_app: OmniApp,
    default_permission_prerequisites,
    default_permission_cleanup,
):
    data = default_permission_prerequisites
    default_permission_cleanup("permission", data.role_code)
    default_permission_cleanup("permission", data.updated_role_code)
    default_permission_app.default_permission_page.create_default_permission(
        data.role_code,
        data.scope_code,
    )

    default_permission_app.default_permission_page.search_default_permission_by_role(
        data.role_code
    )

    default_permission_app.default_permission_page.open_update_default_permission_page()
    default_permission_app.default_permission_page.replace_default_role_permission(
        data.updated_role_code
    )
    default_permission_app.default_permission_page.replace_default_scope_permission(
        data.updated_scope_code
    )
    default_permission_app.default_permission_page.submit_and_verify_updated(
        data.updated_role_code
    )
    
    default_permission_app.default_permission_page.delete_default_permission(
        data.updated_role_code
    )
    default_permission_app.default_permission_page.verify_default_permission_deleted(
        data.updated_role_code
    )
