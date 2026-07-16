from app.omni_app import OmniApp
import allure

@allure.title("檢視專案")
def test_project_read_success(project_app: OmniApp, created_project):
    project_app.project_page.verify_project_cards_visible()
    project_app.project_page.switch_to_project_list_view()
    project_app.project_page.switch_to_project_card_view()
    project_app.project_page.search_project_with_no_result()
    project_app.project_page.search_project_by_abbreviation(
        created_project.project_abbreviation
    )
    project_app.project_page.search_project_by_zh_name(created_project.zh_name)
    project_app.project_page.filter_projects_by_status()
    project_app.project_page.sort_projects_by_created_time()
    project_app.project_page.open_project_detail_from_search(
        created_project.project_abbreviation
    )
    project_app.project_page.open_project_members()
    project_app.project_page.search_project_members()
    project_app.project_page.filter_project_members_by_role()
    project_app.project_page.return_to_project_overview()
