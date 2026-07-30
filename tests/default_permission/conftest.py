import pytest

from app.omni_app import OmniApp
from config.settings import BASE_URL_DEV
from data.factories.resource_data import (
    DefaultPermissionTestData,
    build_permission_scenario_data,
)
from utils.permission_resources import create_permission_prerequisites
from utils.resource_cleanup import CleanupRegistry


# 用途: 產生 Default Permission 測試資料。
@pytest.fixture
def default_permission_data() -> DefaultPermissionTestData:
    return build_permission_scenario_data()


# 用途: 登記 Default Permission、Role 與 Scope 資料，並在測試結束後清除。
@pytest.fixture
def default_permission_cleanup(
    permission_initialized_context,
    cleanup_registry: CleanupRegistry,
):
    context = permission_initialized_context
    app = context.app
    cleanup_page_ready = False

    def ensure_cleanup_page() -> None:
        nonlocal cleanup_page_ready

        if cleanup_page_ready:
            return

        app.operate_page.reset_to_anchor(BASE_URL_DEV)
        app.operate_page.go_to_permission_page(context.abbreviation)
        app.operate_page.open_to_permissions_page()
        cleanup_page_ready = True

    def register(resource_type: str, identifier: str) -> None:
        if resource_type == "permission":
            delete_resource = (
                app.default_permission_page.delete_default_permission_if_exists
            )
        elif resource_type == "role":
            delete_resource = app.role_page.delete_role_if_exists
        elif resource_type == "scope":
            delete_resource = app.scope_page.delete_scope_if_exists
        else:
            raise ValueError(
                f"Unsupported default permission cleanup resource: {resource_type}"
            )

        def cleanup() -> None:
            app.page.keyboard.press("Escape")
            ensure_cleanup_page()
            delete_resource(identifier)

        cleanup_registry.register(resource_type.title(), identifier, cleanup)

    return register


# 用途: 建立 Default Permission 測試所需的 Role 與 Scope 前置資料。
@pytest.fixture
def default_permission_prerequisites(
    permission_settings_app: OmniApp,
    default_permission_data: DefaultPermissionTestData,
    default_permission_cleanup,
) -> DefaultPermissionTestData:
    data = default_permission_data
    create_permission_prerequisites(
        permission_settings_app,
        data,
        default_permission_cleanup,
    )
    return data


# 用途: 建立供 Default Permission 查詢、修改與刪除測試使用的資料。
@pytest.fixture
def created_default_permission(
    permission_settings_app: OmniApp,
    default_permission_prerequisites: DefaultPermissionTestData,
    default_permission_cleanup,
) -> DefaultPermissionTestData:
    data = default_permission_prerequisites
    default_permission_cleanup("permission", data.role_code)
    permission_settings_app.default_permission_page.create_default_permission(
        data.role_code,
        data.scope_code,
    )
    return data
