from app.omni_app import OmniApp
import allure

@allure.title("編輯專案")
def test_project_update_success(project_app: OmniApp, created_project):
    project_app.project_page.open_project_edit_form(created_project.abbreviation)
    project_app.project_page.validate_and_update_project_zh_name(
        created_project.updated_zh_name
    )
    project_app.project_page.update_project_en_name(created_project.updated_en_name)
    project_app.project_page.update_project_tag()
    project_app.project_page.disable_project_status()
    project_app.project_page.update_project_description(
        created_project.updated_description
    )
    project_app.project_page.update_project_icon()
    project_app.project_page.submit_project_update_and_verify(
        created_project.abbreviation
    )
