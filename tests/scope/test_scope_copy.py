from app.omni_app import OmniApp
import allure
import pytest


pytestmark = pytest.mark.scope_copy


@allure.title("[SCOPE-COPY] Copy scope successfully")
def test_scope_copy_success(
    scope_app: OmniApp,
    created_scope,
    scope_cleanup,
):
    scope_cleanup(created_scope.copied_code)

    scope_app.scope_page.click_to_copy_scope_page(created_scope.code)
    scope_app.scope_page.validate_copy_and_fill_code(created_scope.copied_code)
    scope_app.scope_page.validate_and_copy_scope_description(
        created_scope.copied_description
    )
    scope_app.scope_page.submit_and_verify_copied(created_scope.copied_code)
