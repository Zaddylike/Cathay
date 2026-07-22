from app.omni_app import OmniApp
import allure


@allure.title("[PROJECT-MEMBER-JOURNEY] Create, read, update, and delete one member")
def test_project_member_crud_journey(
    project_member_app: OmniApp,
    created_member_project,
):
    project_member_app.project_member_page.open_to_member_page(
        created_member_project.project_abbreviation
    )
    project_member_app.project_member_page.go_to_member_edit_page()
    project_member_app.project_member_page.search_member_to_list(
        created_member_project.primary_member
    )
    project_member_app.project_member_page.adjust_member_level()
    project_member_app.project_member_page.search_member_add(
        created_member_project.primary_member
    )
    project_member_app.project_member_page.search_members(
        created_member_project.read_keywords
    )
    project_member_app.project_member_page.go_to_member_edit_page()
    project_member_app.project_member_page.add_another_member(
        created_member_project.secondary_member
    )
    project_member_app.project_member_page.adjust_previous_member_level()
    project_member_app.project_member_page.go_to_member_edit_page()
    project_member_app.project_member_page.delete_member()
