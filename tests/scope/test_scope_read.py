from app.omni_app import OmniApp
import allure
import pytest


pytestmark = pytest.mark.scope_crud


@allure.title("[SCOPE-CRUD] Read scope successfully")
def test_scope_read_success(scope_app: OmniApp, created_scope):
    scope_app.scope_page.verify_scope_list_visible()
    scope_app.scope_page.search_scope_with_no_result()
    scope_app.scope_page.search_scope_by_code(created_scope.code)
    scope_app.scope_page.search_scope_by_name(created_scope.name)
    scope_app.scope_page.filter_projects_by_status()
    scope_app.scope_page.sort_projects_by_created_time()
