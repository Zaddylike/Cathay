from app.omni_app import OmniApp
import allure



@allure.step("新增專案")
def test_project_create_success(logged_app: OmniApp):
    logged_app.project_page.project_create_002()
    logged_app.project_page.project_create_003()
    logged_app.project_page.project_create_004()
    logged_app.project_page.project_create_005()
    logged_app.project_page.project_create_006()
    logged_app.project_page.project_create_007()
    logged_app.project_page.project_create_008()
    logged_app.project_page.project_create_009()
    logged_app.project_page.project_create_010_011()

@allure.step("檢視專案")
def test_project_read_success(logged_app: OmniApp):
    logged_app.project_page.project_read_002()
    logged_app.project_page.project_read_003()
    logged_app.project_page.project_read_004()
    logged_app.project_page.project_read_005()
    logged_app.project_page.project_read_006()
    logged_app.project_page.project_read_007()
    logged_app.project_page.project_read_008()
    logged_app.project_page.project_read_009()
    logged_app.project_page.project_read_010()
    logged_app.project_page.project_read_011()
    logged_app.project_page.project_read_012()
    logged_app.project_page.project_read_013()
    logged_app.project_page.project_read_014()

@allure.step("編輯專案")
def test_project_update_success(logged_app: OmniApp):
    logged_app.project_page.project_update_002()
    logged_app.project_page.project_update_003()
    logged_app.project_page.project_update_004()
    logged_app.project_page.project_update_005()
    logged_app.project_page.project_update_006()
    logged_app.project_page.project_update_007()
    logged_app.project_page.project_update_008()
    logged_app.project_page.project_update_009_011()

@allure.step("刪除專案")
def test_project_delete_success(logged_app: OmniApp):
    logged_app.project_page.project_delete_002()
    logged_app.project_page.project_delete_003()
    logged_app.project_page.project_delete_004()
    logged_app.project_page.project_delete_005()
    logged_app.project_page.project_delete_006()
