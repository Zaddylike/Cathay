import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import ScopeTestData, build_scope_test_data
from utils.resource_cleanup import CleanupRegistry


# 用途: 產生 Scope 測試資料。
@pytest.fixture
def scope_data() -> ScopeTestData:
    return build_scope_test_data()


# 用途: 登記 Scope 測試資料，並在測試結束後清除。
@pytest.fixture
def scope_cleanup(
    permission_settings_app: OmniApp,
    cleanup_registry: CleanupRegistry,
):
    def delete_scope(scope_code: str) -> None:
        permission_settings_app.page.keyboard.press("Escape")
        permission_settings_app.scope_page.delete_scope_if_exists(scope_code)

    def register(scope_code: str) -> None:
        def cleanup() -> None:
            delete_scope(scope_code)

        cleanup_registry.register(
            "Scope",
            scope_code,
            cleanup,
        )

    return register


# 用途: 建立供 Scope 查詢、修改、刪除與複製測試使用的資料。
@pytest.fixture
def created_scope_data(
    permission_settings_app: OmniApp,
    scope_data: ScopeTestData,
    scope_cleanup,
) -> ScopeTestData:
    scope_cleanup(scope_data.code)
    permission_settings_app.scope_page.create_scope(
        scope_data.code,
        scope_data.name,
        scope_data.description,
    )
    return scope_data
