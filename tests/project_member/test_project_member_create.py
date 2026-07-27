from app.omni_app import OmniApp
import allure


@allure.title("新增成員")
def test_project_member_create_success(
    logged_app: OmniApp,
    created_member_project,
):
    logged_app.project_member_page.open_to_member_page(
        created_member_project.project_abbreviation
    )
    logged_app.project_member_page.go_to_member_edit_page()
    logged_app.project_member_page.search_member_to_list(
        created_member_project.primary_member
    )
    logged_app.project_member_page.adjust_member_level()
    logged_app.project_member_page.search_member_add(
        created_member_project.primary_member
    )
