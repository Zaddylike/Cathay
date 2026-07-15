from app.omni_app import OmniApp
import allure


@allure.title("編輯成員")
def test_project_member_edit_success(project_member_app: OmniApp, created_project_member):
    project_member_app.project_member_page.go_to_member_edit_page()
    project_member_app.project_member_page.add_another_member(
        created_project_member.secondary_member
    )
    project_member_app.project_member_page.adjust_previous_member_level()
