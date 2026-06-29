from app.omni_app import OmniApp
import allure


@allure.title("新增成員")
def test_project_member_create_success(logged_app: OmniApp):
    logged_app.project_member_page.open_to_member_page()
    logged_app.project_member_page.go_to_member_edit_page()
    logged_app.project_member_page.search_member_to_list()
    logged_app.project_member_page.adjust_member_level()
    logged_app.project_member_page.search_member_add() 