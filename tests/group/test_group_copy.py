from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-COPY] Copy group successfully")
def test_group_copy_success(group_app: OmniApp, created_group, group_cleanup):
    group_cleanup(created_group.copied_name)
    group_app.group_page.click_to_group_page()
    group_app.group_page.open_copy_group_page(created_group.name)
    group_app.group_page.validate_and_fill_copied_group(
        created_group.copied_name,
        created_group.copied_description,
    )
    group_app.group_page.submit_and_verify_copied(created_group.copied_name)
