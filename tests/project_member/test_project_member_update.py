from app.omni_app import OmniApp
import allure


@allure.title("編輯成員")
def test_project_member_edit_success(logged_app: OmniApp):
    logged_app.project_member_page.open_to_member_page()
    logged_app.project_member_page.go_to_member_edit_page()
    logged_app.project_member_page.add_another_member()
    logged_app.project_member_page.adjust_previous_member_level()