from app.omni_app import OmniApp
import allure


@allure.title("檢視成員")
def test_project_member_read_success(logged_app: OmniApp, created_project_member):
    logged_app.project_member_page.search_members(
        created_project_member.read_keywords
    )
    logged_app.project_member_page.filter_project_members_by_role()
