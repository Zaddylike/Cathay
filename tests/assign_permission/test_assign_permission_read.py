from app.omni_app import OmniApp
import allure


@allure.title("[ASSIGN-PERMISSION-CRUD] Read assign permission successfully")
def test_assign_permission_read_success(
    permission_sso_app: OmniApp,
    created_assign_permission,
):
    permission_sso_app.assign_permission_page.verify_assign_permission_list_visible()
    permission_sso_app.assign_permission_page.search_assign_permission_by_member(
        created_assign_permission.second_member
    )
    permission_sso_app.assign_permission_page.search_assign_permission_with_no_result()
    permission_sso_app.assign_permission_page.sort_assign_permissions_by_created_time()
