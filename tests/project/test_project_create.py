from app.omni_app import OmniApp
import allure


@allure.title("新增專案")
def test_project_create_success(project_app: OmniApp, project_data, project_cleanup):
    project_cleanup(project_data.project_abbreviation)
    project_app.project_page.open_create_project_dialog()
    project_app.project_page.validate_and_fill_project_abbreviation(
        project_data.project_abbreviation
    )
    project_app.project_page.validate_and_fill_project_zh_name(project_data.zh_name)
    project_app.project_page.fill_project_en_name(project_data.en_name)
    project_app.project_page.validate_and_add_project_tags()
    project_app.project_page.enable_project_status()
    project_app.project_page.validate_and_fill_project_description(
        project_data.description
    )
    project_app.project_page.select_project_icon()
    project_app.project_page.submit_project_and_verify_created(
        project_data.project_abbreviation
    )
