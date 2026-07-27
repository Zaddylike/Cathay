import pytest

from app.omni_app import OmniApp
from config.settings import BASE_URL_DEV
from data.factories.resource_data import (
    DefaultPermissionTestData,
    build_permission_scenario_data,
)
from utils.permission_resources import create_permission_prerequisites
from utils.resource_cleanup import CleanupRegistry


@pytest.fixture
def default_permission_app(permission_settings_app: OmniApp) -> OmniApp:
    return permission_settings_app


@pytest.fixture
def default_permission_data() -> DefaultPermissionTestData:
    return build_permission_scenario_data()


@pytest.fixture
def default_permission_cleanup(
    default_permission_app: OmniApp,
    permission_project,
    cleanup_registry: CleanupRegistry,
):
    def return_to_permission_settings() -> None:
        default_permission_app.page.keyboard.press("Escape")
        default_permission_app.page.goto(BASE_URL_DEV)
        default_permission_app.operate_page.go_to_permission_page(permission_project.abbreviation)
        default_permission_app.operate_page.open_to_permissions_page()

    def register(resource_type: str, identifier: str) -> None:
        if resource_type == "permission":
            delete_resource = (
                default_permission_app.default_permission_page.delete_default_permission_if_exists
            )
        elif resource_type == "role":
            delete_resource = default_permission_app.role_page.delete_role_if_exists
        elif resource_type == "scope":
            delete_resource = default_permission_app.scope_page.delete_scope_if_exists
        else:
            raise ValueError(f"Unsupported default permission cleanup resource: {resource_type}")

        def cleanup() -> None:
            return_to_permission_settings()
            delete_resource(identifier)

        cleanup_registry.register(resource_type.title(), identifier, cleanup)

    return register


@pytest.fixture
def default_permission_prerequisites(
    default_permission_app: OmniApp,
    default_permission_data: DefaultPermissionTestData,
    default_permission_cleanup,
) -> DefaultPermissionTestData:
    data = default_permission_data
    create_permission_prerequisites(
        default_permission_app,
        data,
        default_permission_cleanup,
    )
    return data


@pytest.fixture
def created_default_permission(
    default_permission_app: OmniApp,
    default_permission_prerequisites: DefaultPermissionTestData,
    default_permission_cleanup,
) -> DefaultPermissionTestData:
    data = default_permission_prerequisites
    default_permission_cleanup("permission", data.role_code)
    default_permission_app.default_permission_page.create_default_permission(
        data.role_code,
        data.scope_code,
    )
    return data
