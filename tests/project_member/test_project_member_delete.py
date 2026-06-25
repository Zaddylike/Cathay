from app.omni_app import OmniApp
import allure


@allure.title("刪除成員")
def test_project_member_delete_success(logged_app: OmniApp):
    logged_app.project_member_page.open_to_member_page()
    logged_app.project_member_page.go_to_member_edit_page()
    logged_app.project_member_page.delete_member()