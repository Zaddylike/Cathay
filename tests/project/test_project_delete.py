from app.omni_app import OmniApp
import allure


@allure.title("刪除專案")
def test_project_delete_success(project_app: OmniApp, created_project):
    project_app.project_page.open_project_delete_dialog(created_project.project_abbreviation)
    project_app.project_page.verify_delete_confirm_disabled_by_default()
    project_app.project_page.cancel_project_delete_then_reopen()
    project_app.project_page.confirm_project_delete()
    project_app.project_page.verify_project_deleted(created_project.project_abbreviation)
