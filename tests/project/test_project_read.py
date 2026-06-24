from app.omni_app import OmniApp
import allure

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