from app.omni_app import OmniApp
import allure


@allure.title("初始化 權限設定")
def test_application_init_success(logged_app: OmniApp):
    logged_app.application_page.open_to_member_page()
    logged_app.application_page.open_to_permission_page()
