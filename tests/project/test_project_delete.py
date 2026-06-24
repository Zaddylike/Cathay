from app.omni_app import OmniApp
import allure


@allure.title("[PROJECT-DELETE] Delete project successfully")
def test_project_delete_success(logged_app: OmniApp):
    logged_app.project_page.open_project_delete_dialog()
    logged_app.project_page.verify_delete_confirm_disabled_by_default()
    logged_app.project_page.cancel_project_delete_then_reopen()
    logged_app.project_page.confirm_project_delete()
