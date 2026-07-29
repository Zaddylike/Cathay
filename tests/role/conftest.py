import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import RoleTestData, build_role_test_data
from utils.resource_cleanup import CleanupRegistry


# 用途: 產生 Role 測試資料。
@pytest.fixture
def role_data() -> RoleTestData:
    return build_role_test_data()


# 用途: 登記 Role 與 Scope 測試資料，並在測試結束後清除。
@pytest.fixture
def role_cleanup(
    permission_settings_app: OmniApp,
    cleanup_registry: CleanupRegistry,
):
    def delete_role(role_code: str) -> None:
        permission_settings_app.page.keyboard.press("Escape")
        permission_settings_app.role_page.delete_role_if_exists(role_code)

    def delete_scope(scope_code: str) -> None:
        permission_settings_app.page.keyboard.press("Escape")
        permission_settings_app.scope_page.delete_scope_if_exists(scope_code)

    def register(resource_type: str, resource_code: str) -> None:
        if resource_type == "role":
            delete_resource = delete_role
        elif resource_type == "scope":
            delete_resource = delete_scope
        else:
            raise ValueError(f"Unsupported role cleanup resource: {resource_type}")

        def cleanup() -> None:
            delete_resource(resource_code)

        cleanup_registry.register(resource_type.title(), resource_code, cleanup)

    return register


# 用途: 建立 Role 測試所需的 Scope 前置資料。
@pytest.fixture
def prepared_role_scopes(
    permission_settings_app: OmniApp,
    role_data: RoleTestData,
    role_cleanup,
) -> RoleTestData:
    role_cleanup("scope", role_data.scope_code)
    permission_settings_app.scope_page.create_scope(
        role_data.scope_code,
        role_data.scope_name,
        role_data.scope_description,
    )
    return role_data


# 用途: 建立供 Role 查詢、修改、刪除與複製測試使用的資料。
@pytest.fixture
def created_role(
    permission_settings_app: OmniApp,
    prepared_role_scopes: RoleTestData,
    role_cleanup,
) -> RoleTestData:
    role_cleanup("role", prepared_role_scopes.code)
    permission_settings_app.role_page.create_role(
        prepared_role_scopes.code,
        prepared_role_scopes.name,
        prepared_role_scopes.description,
        prepared_role_scopes.scope_code,
    )
    return prepared_role_scopes
