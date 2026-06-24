from app.omni_app import OmniApp
import allure



@allure.title("新增專案")
def test_project_create_success(logged_app: OmniApp):
    logged_app.project_page.open_create_project_dialog()
    logged_app.project_page.validate_and_fill_project_abbreviation()
    logged_app.project_page.validate_and_fill_project_zh_name()
    logged_app.project_page.fill_project_en_name()
    logged_app.project_page.validate_and_add_project_tags()
    logged_app.project_page.enable_project_status()
    logged_app.project_page.validate_and_fill_project_description()
    logged_app.project_page.select_project_icon()
    logged_app.project_page.submit_project_and_verify_created()

@allure.title("檢視專案")
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

@allure.title("刪除專案")
def test_project_delete_success(logged_app: OmniApp):
    logged_app.project_page.open_project_delete_dialog()
    logged_app.project_page.verify_delete_confirm_disabled_by_default()
    logged_app.project_page.cancel_project_delete_then_reopen()
    logged_app.project_page.confirm_project_delete()
    logged_app.project_page.verify_project_deleted()
