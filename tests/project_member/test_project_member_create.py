from app.omni_app import OmniApp
import allure


@allure.title("新增成員")
def test_project_create_success(logged_app: OmniApp):
    logged_app.project_member_page.open_to_member_page()
    logged_app.project_member_page.add_member_to_list()
