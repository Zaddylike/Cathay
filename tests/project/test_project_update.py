from app.omni_app import OmniApp
import allure

@allure.title("編輯專案")
def test_project_update_success(logged_app: OmniApp):
    logged_app.project_page.open_project_edit_form()
    logged_app.project_page.validate_and_update_project_zh_name()
    logged_app.project_page.update_project_en_name()
    logged_app.project_page.update_project_tag()
    logged_app.project_page.disable_project_status()
    logged_app.project_page.update_project_description()
    logged_app.project_page.update_project_icon()
    logged_app.project_page.submit_project_update_and_verify()
