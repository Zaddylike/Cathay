from app.omni_app import OmniApp
import allure


@allure.title("[GROUP-CRUD] Update group successfully")
def test_group_update_success(group_app: OmniApp, created_group, group_cleanup):
    group_cleanup(created_group.updated_name)
    group_app.group_page.click_to_group_page()
    group_app.group_page.open_update_group_page(created_group.name)
    group_app.group_page.validate_and_update_group_name(created_group.updated_name)
    group_app.group_page.validate_and_update_group_description(
        created_group.updated_description
    )
    group_app.group_page.disable_group_status()
    group_app.group_page.submit_and_verify_updated(created_group.updated_name)
