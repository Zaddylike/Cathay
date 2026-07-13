from app.omni_app import OmniApp
import allure
import pytest


pytestmark = pytest.mark.scope_crud


@allure.title("[SCOPE-CRUD] Delete scope successfully")
def test_scope_delete_success(scope_app: OmniApp, created_scope):
    scope_app.scope_page.delete_scope(created_scope.code)
    scope_app.scope_page.verify_scope_deleted(created_scope.code)
