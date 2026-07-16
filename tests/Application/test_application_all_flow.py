from app.omni_app import OmniApp
import allure


@allure.title("初始化 單一登入")
def test_single_sign_on_init_success(logged_app: OmniApp, application_project):
    data = application_project
    logged_app.single_sign_on_page.open_to_permission_page(data.project_abbreviation)
    logged_app.single_sign_on_page.open_to_create_sso_page()
    logged_app.operate_page.click_to_next_step()
    logged_app.single_sign_on_page.create_provider_entraId()
    logged_app.single_sign_on_page.input_entraId_clientId(data.entra_client_id)
    logged_app.single_sign_on_page.input_entraId_secret(data.entra_secret)
    logged_app.single_sign_on_page.input_entraId_tenant(data.entra_tenant)
    logged_app.single_sign_on_page.verify_advanced(data.entra_tenant, data.entra_attribute)

    logged_app.single_sign_on_page.verify_dup_create()
    logged_app.single_sign_on_page.create_provider_google()
    logged_app.single_sign_on_page.input_google_clientId(data.google_client_id)
    logged_app.single_sign_on_page.input_google_secret(data.google_secret)
    logged_app.single_sign_on_page.switch_whitelist_active()
    logged_app.single_sign_on_page.input_identify_field(data.google_identify_field)

    logged_app.single_sign_on_page.create_provider_oidc()
    logged_app.single_sign_on_page.input_oidc_setting(data.oidc_value)
    logged_app.operate_page.click_to_next_step()

    logged_app.single_sign_on_page.input_application_name(data.sso_application_name)
    logged_app.single_sign_on_page.select_tenant()
    logged_app.single_sign_on_page.input_application_redirectUrl(data.redirect_url)
    logged_app.single_sign_on_page.input_application_logoutUrl(data.logout_url)
    logged_app.single_sign_on_page.setting_date()
    logged_app.single_sign_on_page.submit_sso_and_verify_success()


@allure.title("初始化 權限設定")
def test_application_init_success(logged_app: OmniApp, application_permission_init_project):
    data = application_permission_init_project
    # Scope
    logged_app.application_permission_page.open_to_permission_page(data.project_abbreviation)
    logged_app.application_permission_page.open_to_create_permission_page()
    logged_app.application_permission_page.validate_and_fill_scope_code(data.scope_code)
    logged_app.application_permission_page.validate_and_fill_scope_name(data.scope_name)
    logged_app.application_permission_page.validate_and_fill_scope_description(data.scope_description)
    logged_app.application_permission_page.validate_duplicate_scope(data.scope_code)
    logged_app.application_permission_page.create_another_scope(data.second_scope_code, data.second_scope_name, data.second_scope_description)
    logged_app.application_permission_page.click_to_role_next_step()
    # Role
    logged_app.application_permission_page.click_to_extend_role_page()
    logged_app.application_permission_page.validate_and_fill_role_code(data.role_code)
    logged_app.application_permission_page.validate_and_fill_role_name(data.role_name)
    logged_app.application_permission_page.validate_and_fill_role_description(data.role_description)
    logged_app.application_permission_page.select_created_scope()
    logged_app.application_permission_page.validate_duplicate_role(data.role_code)
    logged_app.application_permission_page.create_another_role(data.second_role_code, data.second_role_name, data.second_role_description)
    logged_app.application_permission_page.create_scope_in_role_page(data.second_scope_code, data.second_scope_name, data.third_scope_code, data.third_scope_name)
    logged_app.application_permission_page.click_to_group_next_step()
    # Group
    logged_app.application_permission_page.click_to_extend_group_page()
    logged_app.application_permission_page.validate_and_fill_group_name(data.group_name)
    logged_app.application_permission_page.validate_and_fill_group_description(data.group_description)
    logged_app.application_permission_page.invite_team_member(data.member_keyword, data.group_member_description)
    logged_app.application_permission_page.click_to_permission_next_step()
    # Assign Permission
    logged_app.application_permission_page.create_permission_setting(data.member_keyword)
    logged_app.application_permission_page.create_permission_role()
    logged_app.application_permission_page.create_permission_scope()
    logged_app.application_permission_page.create_permission_description(data.assignment_description)
    logged_app.application_permission_page.click_to_default_permission_next_step()
    # Default Permission
    logged_app.application_permission_page.create_role_for_member()
    logged_app.application_permission_page.create_scope_for_member()
    logged_app.application_permission_page.verify_permission_creation()


@allure.title("初始化 伺服器串接")
def test_server_to_server_init_success(logged_app: OmniApp, application_s2s_project):
    data = application_s2s_project
    logged_app.server_to_server_page.open_to_permission_page(data.project_abbreviation)
    logged_app.server_to_server_page.open_to_create_s2s_page()
    logged_app.server_to_server_page.input_s2s_application_name(data.s2s_application_name)
    logged_app.server_to_server_page.setting_date()
    logged_app.server_to_server_page.input_application_description(data.s2s_description)
    logged_app.server_to_server_page.continue_to_scope_step()
    logged_app.server_to_server_page.create_scope()
    logged_app.server_to_server_page.input_scope_description(data.s2s_scope_description)
    logged_app.server_to_server_page.submit_s2s_and_verify_success()
