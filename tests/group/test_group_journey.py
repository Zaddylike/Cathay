from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-JOURNEY] Create, read, update, and delete one group")
def test_group_crud_journey(
    permission_sso_app: OmniApp,
    group_data,
    group_cleanup,
):
    group_cleanup(group_data.name)
    group_cleanup(group_data.updated_name)
    permission_sso_app.group_page.create_group(
        group_data.name,
        group_data.description,
        group_data.member_keyword,
    )
    permission_sso_app.group_page.search_group_by_name(group_data.name)
    permission_sso_app.group_page.open_update_group_page(group_data.name)
    permission_sso_app.group_page.validate_and_update_group_name(
        group_data.updated_name
    )
    permission_sso_app.group_page.validate_and_update_group_description(
        group_data.updated_description
    )
    permission_sso_app.group_page.submit_and_verify_updated(group_data.updated_name)
    permission_sso_app.group_page.delete_group(group_data.updated_name)
    permission_sso_app.group_page.verify_group_deleted(group_data.updated_name)
