from app.omni_app import OmniApp
import allure
import pytest


pytestmark = pytest.mark.scope_crud


@allure.title("[SCOPE-CRUD] Create scope successfully")
def test_scope_create_success(scope_app: OmniApp, scope_data, scope_cleanup):
    scope_cleanup(scope_data.code)
    scope_cleanup(scope_data.second_code)

    scope_app.scope_page.click_to_create_scope_page()
    scope_app.scope_page.validate_and_fill_scope_code(scope_data.code)
    scope_app.scope_page.validate_and_fill_scope_name(scope_data.name)
    scope_app.scope_page.validate_and_fill_scope_description(scope_data.description)
    scope_app.scope_page.validate_duplicate_scope(scope_data.code)
    scope_app.scope_page.create_another_scope(
        scope_data.second_code,
        scope_data.second_name,
        scope_data.second_description,
    )
    scope_app.scope_page.submit_and_verify_created(scope_data.code)
