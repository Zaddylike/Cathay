import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import RoleTestData, build_role_test_data
from utils.resource_cleanup import CleanupRegistry


@pytest.fixture
def role_app(permission_settings_app: OmniApp) -> OmniApp:
    return permission_settings_app


@pytest.fixture
def role_data() -> RoleTestData:
    return build_role_test_data()


@pytest.fixture
def role_cleanup(
    role_app: OmniApp,
    cleanup_registry: CleanupRegistry,
):
    def delete_role(role_code: str) -> None:
        role_app.page.keyboard.press("Escape")
        role_app.role_page.delete_role_if_exists(role_code)

    def delete_scope(scope_code: str) -> None:
        role_app.page.keyboard.press("Escape")
        role_app.scope_page.delete_scope_if_exists(scope_code)

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

@pytest.fixture
def prepared_role_scopes(
    role_app: OmniApp,
    role_data: RoleTestData,
    role_cleanup,
) -> RoleTestData:
    role_cleanup("scope", role_data.scope_code)
    
    role_app.scope_page.create_scope(
        role_data.scope_code,
        role_data.scope_name,
        role_data.scope_description,
    )
    return role_data

# 用途: 新增角色資料用於測試Read, Update, Delete, Copy 情境
@pytest.fixture
def created_role(
    role_app: OmniApp,
    prepared_role_scopes: RoleTestData,
    role_cleanup,
) -> RoleTestData:
    role_cleanup("role", prepared_role_scopes.code)
    role_app.role_page.create_role(
        prepared_role_scopes.code,
        prepared_role_scopes.name,
        prepared_role_scopes.description,
        prepared_role_scopes.scope_code,
    )
    return prepared_role_scopes
