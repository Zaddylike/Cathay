import pytest

from app.omni_app import OmniApp
from config.settings import BASE_URL_DEV
from data.factories.resource_data import (
    AssignPermissionTestData,
    build_assign_permission_test_data,
)
from utils.permission_resources import create_permission_prerequisites
from utils.resource_cleanup import CleanupRegistry


@pytest.fixture
def assign_permission_app(permission_settings_sso_app: OmniApp) -> OmniApp:
    return permission_settings_sso_app


@pytest.fixture
def assign_permission_data() -> AssignPermissionTestData:
    return build_assign_permission_test_data()


@pytest.fixture
def assign_permission_cleanup(
    assign_permission_app: OmniApp,
    permission_project,
    cleanup_registry: CleanupRegistry,
):
    def return_to_permission_settings() -> None:
        assign_permission_app.page.keyboard.press("Escape")
        assign_permission_app.page.goto(BASE_URL_DEV)
        assign_permission_app.operate_page.go_to_permission_page(permission_project.abbreviation)
        assign_permission_app.operate_page.open_to_permissions_page()

    def register(resource_type: str, identifier: str) -> None:
        if resource_type == "assignment":
            delete_resource = (
                assign_permission_app.assign_permission_page.delete_assign_permission_if_exists
            )
        elif resource_type == "role":
            delete_resource = assign_permission_app.role_page.delete_role_if_exists
        elif resource_type == "scope":
            delete_resource = assign_permission_app.scope_page.delete_scope_if_exists
        else:
            raise ValueError(f"Unsupported assign permission cleanup resource: {resource_type}")

        def cleanup() -> None:
            return_to_permission_settings()
            delete_resource(identifier)

        cleanup_registry.register(resource_type.title(), identifier, cleanup)

    return register


@pytest.fixture
def assign_permission_prerequisites(
    assign_permission_app: OmniApp,
    assign_permission_data: AssignPermissionTestData,
    assign_permission_cleanup,
) -> AssignPermissionTestData:
    data = assign_permission_data
    create_permission_prerequisites(
        assign_permission_app,
        data,
        assign_permission_cleanup,
    )
    return data


@pytest.fixture
def created_assign_permission(
    assign_permission_app: OmniApp,
    assign_permission_prerequisites: AssignPermissionTestData,
    assign_permission_cleanup,
) -> AssignPermissionTestData:
    data = assign_permission_prerequisites
    assign_permission_cleanup("assignment", data.role_code)
    assign_permission_cleanup("assignment", data.updated_role_code)
    assign_permission_app.assign_permission_page.create_assign_permission(
        data.second_member,
        data.role_code,
        data.scope_code,
        data.description,
    )
    return data
