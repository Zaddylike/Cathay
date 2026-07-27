import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import ScopeTestData, build_scope_test_data
from utils.resource_cleanup import CleanupRegistry


@pytest.fixture
def scope_app(permission_settings_app: OmniApp) -> OmniApp:
    return permission_settings_app


@pytest.fixture
def scope_data() -> ScopeTestData:
    return build_scope_test_data()


@pytest.fixture
def created_scope_data(
    scope_app: OmniApp,
    scope_data: ScopeTestData,
    scope_cleanup,
) -> ScopeTestData:
    scope_cleanup(scope_data.code)
    scope_app.scope_page.create_scope(
        scope_data.code,
        scope_data.name,
        scope_data.description,
    )
    return scope_data


@pytest.fixture
def scope_cleanup(
    scope_app: OmniApp,
    cleanup_registry: CleanupRegistry,
):
    def delete_scope(scope_code: str) -> None:
        scope_app.page.keyboard.press("Escape")
        scope_app.scope_page.delete_scope_if_exists(scope_code)

    def register(scope_code: str) -> None:
        def cleanup() -> None:
            delete_scope(scope_code)

        cleanup_registry.register(
            "Scope",
            scope_code,
            cleanup,
        )

    return register
