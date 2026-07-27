from app.omni_app import OmniApp
import allure


@allure.title("刪除專案")
def test_project_delete_success(logged_app: OmniApp, created_project):
    logged_app.project_page.open_project_delete_dialog(created_project.project_abbreviation)
    logged_app.project_page.verify_delete_confirm_disabled_by_default()
    logged_app.project_page.cancel_project_delete_then_reopen()
    logged_app.project_page.confirm_project_delete()
    logged_app.project_page.verify_project_deleted(created_project.project_abbreviation)
