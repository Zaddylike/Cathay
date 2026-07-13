from app.omni_app import OmniApp
import allure
import pytest


pytestmark = pytest.mark.journey


@allure.title("[SCOPE-JOURNEY] Create, read, update, and delete one scope")
def test_scope_crud_journey(scope_app: OmniApp, scope_data, scope_cleanup):
    scope_cleanup(scope_data.code)

    scope_app.scope_page.create_scope(
        scope_data.code,
        scope_data.name,
        scope_data.description,
    )
    scope_app.scope_page.verify_scope_list_visible()
    scope_app.scope_page.search_scope_by_code(scope_data.code)
    scope_app.scope_page.search_scope_by_name(scope_data.name)

    scope_app.scope_page.click_to_update_scope_page(scope_data.code)
    scope_app.scope_page.validate_and_update_scope_name(scope_data.updated_name)
    scope_app.scope_page.validate_and_update_scope_description(
        scope_data.updated_description
    )
    scope_app.scope_page.disable_scope_status()
    scope_app.scope_page.submit_and_verify_updated(scope_data.updated_name)

    scope_app.scope_page.delete_scope(scope_data.code)
    scope_app.scope_page.verify_scope_deleted(scope_data.code)

