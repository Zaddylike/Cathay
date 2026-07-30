import pytest

from app.omni_app import OmniApp
from config.settings import BASE_URL_DEV
from data.factories.resource_data import (
    AssignPermissionTestData,
    build_assign_permission_test_data,
)
from utils.permission_resources import create_permission_prerequisites
from utils.resource_cleanup import CleanupRegistry


# 用途: 產生 Assign Permission 測試資料。
@pytest.fixture
def assign_permission_data() -> AssignPermissionTestData:
    return build_assign_permission_test_data()


# 用途: 登記 Assign Permission、Role 與 Scope 資料，並在測試結束後清除。
@pytest.fixture
def assign_permission_cleanup(
    permission_sso_context,
    cleanup_registry: CleanupRegistry,
):
    context = permission_sso_context
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
        if resource_type == "assignment":
            delete_resource = (
                app.assign_permission_page.delete_assign_permission_if_exists
            )
        elif resource_type == "role":
            delete_resource = app.role_page.delete_role_if_exists
        elif resource_type == "scope":
            delete_resource = app.scope_page.delete_scope_if_exists
        else:
            raise ValueError(
                f"Unsupported assign permission cleanup resource: {resource_type}"
            )

        def cleanup() -> None:
            app.page.keyboard.press("Escape")
            ensure_cleanup_page()
            delete_resource(identifier)

        cleanup_registry.register(resource_type.title(), identifier, cleanup)

    return register


# 用途: 建立 Assign Permission 測試所需的 Role 與 Scope 前置資料。
@pytest.fixture
def assign_permission_prerequisites(
    permission_sso_app: OmniApp,
    assign_permission_data: AssignPermissionTestData,
    assign_permission_cleanup,
) -> AssignPermissionTestData:
    data = assign_permission_data
    create_permission_prerequisites(
        permission_sso_app,
        data,
        assign_permission_cleanup,
    )
    return data


# 用途: 建立供 Assign Permission 查詢、修改與刪除測試使用的資料。
@pytest.fixture
def created_assign_permission(
    permission_sso_app: OmniApp,
    assign_permission_prerequisites: AssignPermissionTestData,
    assign_permission_cleanup,
) -> AssignPermissionTestData:
    data = assign_permission_prerequisites
    assign_permission_cleanup("assignment", data.role_code)
    assign_permission_cleanup("assignment", data.updated_role_code)
    permission_sso_app.assign_permission_page.create_assign_permission(
        data.second_member,
        data.role_code,
        data.scope_code,
        data.description,
    )
    return data
