from app.omni_app import OmniApp
import allure


@allure.title("檢視成員")
def test_project_member_read_success(logged_app: OmniApp):
    logged_app.project_member_page.open_to_member_page()
    logged_app.project_member_page.search_members()
    logged_app.project_member_page.filter_project_members_by_role()
    