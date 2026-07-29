from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-COPY] Copy group successfully")
def test_group_copy_success(
    permission_sso_app: OmniApp,
    created_group,
    group_cleanup,
):
    group_cleanup(created_group.copied_name)
    permission_sso_app.group_page.click_to_group_page()
    permission_sso_app.group_page.open_copy_group_page(created_group.name)
    permission_sso_app.group_page.validate_and_fill_copied_group(
        created_group.copied_name,
        created_group.copied_description,
    )
    permission_sso_app.group_page.submit_and_verify_copied(created_group.copied_name)
