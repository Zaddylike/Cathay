from app.omni_app import OmniApp
import allure

@allure.step("檢視專案")
@allure.title("[PROJECT-READ] Read project successfully")
def test_project_read_success(logged_app: OmniApp):
    logged_app.project_page.verify_project_cards_visible()
    logged_app.project_page.switch_to_project_list_view()
    logged_app.project_page.switch_to_project_card_view()
    logged_app.project_page.search_project_with_no_result()
    logged_app.project_page.search_project_by_abbreviation()
    logged_app.project_page.search_project_by_zh_name()
    logged_app.project_page.filter_projects_by_status()
    logged_app.project_page.sort_projects_by_created_time()
    logged_app.project_page.open_project_detail_from_search()
    logged_app.project_page.open_project_members()
    logged_app.project_page.search_project_members()
    logged_app.project_page.filter_project_members_by_role()
    logged_app.project_page.return_to_project_overview()
