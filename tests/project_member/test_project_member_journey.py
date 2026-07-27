from app.omni_app import OmniApp
import allure


@allure.title("[PROJECT-MEMBER-JOURNEY] Create, read, update, and delete one member")
def test_project_member_crud_journey(
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
    logged_app.project_member_page.search_members(
        created_member_project.read_keywords
    )
    logged_app.project_member_page.go_to_member_edit_page()
    logged_app.project_member_page.add_another_member(
        created_member_project.secondary_member
    )
    logged_app.project_member_page.adjust_previous_member_level()
    logged_app.project_member_page.go_to_member_edit_page()
    logged_app.project_member_page.delete_member()
