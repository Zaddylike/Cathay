from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import (
    ROLE_CODE,
    ROLE_DESCRIPTION_PREFIX,
    ROLE_NAME_PREFIX,
    SCOPE_CODE_PREFIX,
    SCOPE_DESCRIPTION_PREFIX,
    SCOPE_NAME_PREFIX,
)
from utils.data_mode import should_cleanup


@dataclass(frozen=True)
class DefaultPermissionTestData:
    role_code: str
    role_name: str
    role_description: str
    scope_code: str
    scope_name: str
    scope_description: str
    updated_role_code: str
    updated_role_name: str
    updated_role_description: str
    updated_scope_code: str
    updated_scope_name: str
    updated_scope_description: str


@pytest.fixture
def default_permission_data() -> DefaultPermissionTestData:
    suffix = uuid4().hex[:4]
    updated_suffix = uuid4().hex[:4]
    role_code = f"{ROLE_CODE}{suffix}"
    role_name = f"{ROLE_NAME_PREFIX}{suffix}"
    role_description = f"{ROLE_DESCRIPTION_PREFIX}{suffix}"
    scope_code = f"{SCOPE_CODE_PREFIX}{suffix}"
    scope_name = f"{SCOPE_NAME_PREFIX}{suffix}"
    scope_description = f"{SCOPE_DESCRIPTION_PREFIX}{suffix}"
    updated_role_code = f"{ROLE_CODE}{updated_suffix}"
    updated_role_name = f"{ROLE_NAME_PREFIX}{updated_suffix}"
    updated_role_description = f"{ROLE_DESCRIPTION_PREFIX}{updated_suffix}"
    updated_scope_code = f"{SCOPE_CODE_PREFIX}{updated_suffix}"
    updated_scope_name = f"{SCOPE_NAME_PREFIX}{updated_suffix}"
    updated_scope_description = f"{SCOPE_DESCRIPTION_PREFIX}{updated_suffix}"

    return DefaultPermissionTestData(
        role_code=role_code,
        role_name=role_name,
        role_description=role_description,
        scope_code=scope_code,
        scope_name=scope_name,
        scope_description=scope_description,
        updated_role_code=updated_role_code,
        updated_role_name=updated_role_name,
        updated_role_description=updated_role_description,
        updated_scope_code=updated_scope_code,
        updated_scope_name=updated_scope_name,
        updated_scope_description=updated_scope_description,
    )


@pytest.fixture
def default_permission_app(permission_project_app: OmniApp) -> OmniApp:
    permission_project_app.operate_page.open_to_permissions_page()
    return permission_project_app


@pytest.fixture
def default_permission_cleanup(default_permission_app: OmniApp, data_mode: str):
    """登記 Default Permission/Role/Scope;isolated 清除，keep 保留。"""
    tracked = {"permission": [], "role": [], "scope": []}

    def track(resource_type: str, identifier: str):
        if identifier not in tracked[resource_type]:
            tracked[resource_type].append(identifier)

    yield track

    if not should_cleanup(data_mode):
        return

    for role_code in reversed(tracked["permission"]):
        try:
            default_permission_app.page.keyboard.press("Escape")
            default_permission_app.default_permission_page.delete_default_permission_if_exists(
                role_code
            )
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Default permission cleanup failed: {role_code}",
                attachment_type=allure.attachment_type.TEXT,
            )

    for role_code in reversed(tracked["role"]):
        try:
            default_permission_app.role_page.delete_role_if_exists(role_code)
        except Exception as error:
            allure.attach(str(error), name=f"Role cleanup failed: {role_code}")

    for scope_code in reversed(tracked["scope"]):
        try:
            default_permission_app.scope_page.delete_scope_if_exists(scope_code)
        except Exception as error:
            allure.attach(str(error), name=f"Scope cleanup failed: {scope_code}")


@pytest.fixture
def default_permission_prerequisites(
    default_permission_app: OmniApp,
    default_permission_data: DefaultPermissionTestData,
    default_permission_cleanup,
) -> DefaultPermissionTestData:
    for scope_code, scope_name, scope_description in (
        (
            default_permission_data.scope_code,
            default_permission_data.scope_name,
            default_permission_data.scope_description,
        ),
        (
            default_permission_data.updated_scope_code,
            default_permission_data.updated_scope_name,
            default_permission_data.updated_scope_description,
        ),
    ):
        default_permission_cleanup("scope", scope_code)
        default_permission_app.scope_page.create_scope(
            scope_code,
            scope_name,
            scope_description,
        )

    for role_code, role_name, role_description, scope_code in (
        (
            default_permission_data.role_code,
            default_permission_data.role_name,
            default_permission_data.role_description,
            default_permission_data.scope_code,
        ),
        (
            default_permission_data.updated_role_code,
            default_permission_data.updated_role_name,
            default_permission_data.updated_role_description,
            default_permission_data.updated_scope_code,
        ),
    ):
        default_permission_cleanup("role", role_code)
        default_permission_app.role_page.create_role(
            role_code,
            role_name,
            role_description,
            scope_code,
        )

    return default_permission_data


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
