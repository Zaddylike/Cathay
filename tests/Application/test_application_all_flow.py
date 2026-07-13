from app.omni_app import OmniApp
import allure


@allure.title("初始化 單一登入")
def test_single_sign_on_init_success(logged_app: OmniApp):
    logged_app.single_signon_page.open_to_permission_page()
    logged_app.single_signon_page.open_to_create_sso_page()
    logged_app.operate_page.click_to_next_step()
    logged_app.single_signon_page.create_provider_entraId()
    logged_app.single_signon_page.input_entraId_clientId()
    logged_app.single_signon_page.input_entraId_secret()
    logged_app.single_signon_page.input_entraId_tenant()
    logged_app.single_signon_page.verify_advanced()

    logged_app.single_signon_page.verify_dup_create()
    logged_app.single_signon_page.create_provider_google()
    logged_app.single_signon_page.input_google_clientId()
    logged_app.single_signon_page.input_google_secret()
    logged_app.single_signon_page.switch_whitelist_active()
    logged_app.single_signon_page.input_identify_field()

    logged_app.single_signon_page.create_provider_oidc()
    logged_app.single_signon_page.input_oidc_setting()
    logged_app.operate_page.click_to_next_step()

    logged_app.single_signon_page.input_application_name()
    logged_app.single_signon_page.select_tenant()
    logged_app.single_signon_page.input_application_redirectUrl()
    logged_app.single_signon_page.input_application_logoutUrl()
    logged_app.single_signon_page.setting_date()
    logged_app.single_signon_page.submit_sso_and_verify_success()


@allure.title("初始化 權限設定")
def test_application_init_success(logged_app: OmniApp):
    # Scope
    logged_app.permission_page.open_to_permission_page()
    logged_app.permission_page.open_to_create_permission_page()
    logged_app.permission_page.validate_and_fill_scope_code()
    logged_app.permission_page.validate_and_fill_scope_name()
    logged_app.permission_page.validate_and_fill_scope_description()
    logged_app.permission_page.validate_duplicate_scope()
    logged_app.permission_page.create_another_scope()
    logged_app.permission_page.click_to_role_next_step()
    # Role
    logged_app.permission_page.click_to_extend_role_page()
    logged_app.permission_page.validate_and_fill_role_code()
    logged_app.permission_page.validate_and_fill_role_name()
    logged_app.permission_page.validate_and_fill_role_description()
    logged_app.permission_page.select_created_scope()
    logged_app.permission_page.validate_duplicate_role()
    logged_app.permission_page.create_another_role()
    logged_app.permission_page.create_scope_in_role_page()
    logged_app.permission_page.click_to_group_next_step()
    # Group
    logged_app.permission_page.click_to_extend_group_page()
    logged_app.permission_page.validate_and_fill_group_name()
    logged_app.permission_page.validate_and_fill_group_description()
    logged_app.permission_page.invite_team_member()
    logged_app.permission_page.click_to_permission_next_step()
    # Assign Permission
    logged_app.permission_page.create_permission_setting()
    logged_app.permission_page.create_permission_role()
    logged_app.permission_page.create_permission_scope()
    logged_app.permission_page.create_permission_description()
    logged_app.permission_page.click_to_default_permission_next_step()
    # Default Permission
    logged_app.permission_page.create_role_for_member()
    logged_app.permission_page.create_scope_for_member()
    logged_app.permission_page.verify_permission_creation()


@allure.title("初始化 伺服器串接")
def test_server_to_server_init_success(logged_app: OmniApp):
    logged_app.server_to_servser_page.open_to_permission_page()
    logged_app.server_to_servser_page.open_to_create_s2s_page()
    logged_app.server_to_servser_page.input_s2s_application_name()
    logged_app.server_to_servser_page.setting_date()
    logged_app.server_to_servser_page.input_application_description()
    logged_app.operate_page.click_to_next_step()
    logged_app.server_to_servser_page.create_scope()
    logged_app.server_to_servser_page.input_scope_description()
    logged_app.server_to_servser_page.submit_s2s_and_verify_success()





