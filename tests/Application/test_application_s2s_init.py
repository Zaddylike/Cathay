from app.omni_app import OmniApp
import allure


@allure.title("初始化 伺服器串接")
def test_server_to_server_init_success(logged_app: OmniApp):
    logged_app.server_to_servser_page.open_to_permission_page()
    logged_app.server_to_servser_page.open_to_create_s2s_page()
    logged_app.server_to_servser_page.click_to_next_step()
    logged_app.server_to_servser_page.input_s2s_application_name()
    logged_app.server_to_servser_page.setting_date()
    logged_app.server_to_servser_page.input_application_description()
    logged_app.server_to_servser_page.create_scope()
    logged_app.server_to_servser_page.input_scope_description()
    logged_app.server_to_servser_page.submit_s2s_and_verify_success()





