from app.omni_app import OmniApp
import allure
import pytest


pytestmark = pytest.mark.scope_crud


@allure.title("[SCOPE-CRUD] Update scope successfully")
def test_scope_update_success(scope_app: OmniApp, created_scope):
    scope_app.scope_page.click_to_update_scope_page(created_scope.code)
    scope_app.scope_page.validate_and_update_scope_name(created_scope.updated_name)
    scope_app.scope_page.validate_and_update_scope_description(
        created_scope.updated_description
    )
    scope_app.scope_page.disable_scope_status()
    scope_app.scope_page.submit_and_verify_updated(created_scope.updated_name)
