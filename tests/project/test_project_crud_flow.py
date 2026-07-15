from app.omni_app import OmniApp
import allure


@allure.title("[PROJECT-JOURNEY] Create, read, update, and delete one project")
def test_project_crud_journey(project_app: OmniApp, project_data, project_cleanup):
    project_cleanup(project_data.abbreviation)
    project_app.project_page.create_project(
        project_data.abbreviation,
        project_data.zh_name,
        project_data.en_name,
        project_data.description,
    )
    project_app.project_page.search_project_by_abbreviation(project_data.abbreviation)
    project_app.project_page.search_project_by_zh_name(project_data.zh_name)
    project_app.project_page.open_project_edit_form(project_data.abbreviation)
    project_app.project_page.validate_and_update_project_zh_name(
        project_data.updated_zh_name
    )
    project_app.project_page.update_project_en_name(project_data.updated_en_name)
    project_app.project_page.update_project_description(
        project_data.updated_description
    )
    project_app.project_page.submit_project_update_and_verify(
        project_data.abbreviation
    )
    project_app.project_page.delete_project(project_data.abbreviation)
    project_app.project_page.verify_project_deleted(project_data.abbreviation)
