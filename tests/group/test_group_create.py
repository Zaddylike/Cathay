from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Create group successfully")
def test_group_create_success(
    permission_sso_app: OmniApp,
    group_data,
    group_cleanup,
):
    group_cleanup(group_data.name)

    permission_sso_app.group_page.click_to_create_group_page()
    permission_sso_app.group_page.open_create_group_page()
    permission_sso_app.group_page.validate_and_fill_group_name(group_data.name)
    permission_sso_app.group_page.validate_and_fill_group_description(
        group_data.description
    )
    permission_sso_app.group_page.invite_group_member(
        group_data.member_keyword,
        group_data.description,
    )
    permission_sso_app.group_page.submit_and_verify_created(group_data.name)
