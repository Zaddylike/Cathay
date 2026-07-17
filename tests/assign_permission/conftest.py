from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import (
    ASSIGN_PERMISSION_DESCRIPTION_PREFIX,
    ASSIGN_PERMISSION_MEMBER,
    ASSIGN_PERMISSION_SECOND_MEMBER,
    BASE_URL_DEV,
    ROLE_CODE,
    ROLE_DESCRIPTION_PREFIX,
    ROLE_NAME_PREFIX,
    SCOPE_CODE_PREFIX,
    SCOPE_DESCRIPTION_PREFIX,
    SCOPE_NAME_PREFIX,
)
from utils.data_mode import should_cleanup


@dataclass(frozen=True)
class AssignPermissionTestData:
    member: str
    second_member: str
    description: str
    second_description: str
    updated_description: str
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
def assign_permission_data() -> AssignPermissionTestData:
    suffix = uuid4().hex[:4]
    updated_suffix = uuid4().hex[:4]
    description = f"{ASSIGN_PERMISSION_DESCRIPTION_PREFIX}{suffix}"
    second_description = f"{ASSIGN_PERMISSION_DESCRIPTION_PREFIX}{updated_suffix}"
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

    return AssignPermissionTestData(
        member=ASSIGN_PERMISSION_MEMBER,
        second_member=ASSIGN_PERMISSION_SECOND_MEMBER,
        description=description,
        second_description=second_description,
        updated_description=f"updated-{description}",
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
def assign_permission_app(assign_permission_project_app: OmniApp) -> OmniApp:
    assign_permission_project_app.operate_page.open_to_permissions_page()
    return assign_permission_project_app


@pytest.fixture
def assign_permission_cleanup(
    assign_permission_app: OmniApp,
    data_mode: str,
    permission_project,
):
    """登記 Assignment／Role／Scope；isolated 依相依順序清除，keep 保留。"""
    tracked = {"assignment": [], "role": [], "scope": []}

    def track(resource_type: str, identifier: str):
        if identifier not in tracked[resource_type]:
            tracked[resource_type].append(identifier)

    yield track

    if not should_cleanup(data_mode):
        return

    def return_to_permission_settings():
        assign_permission_app.page.keyboard.press("Escape")
        assign_permission_app.page.goto(BASE_URL_DEV)
        assign_permission_app.operate_page.go_to_permission_page(
            permission_project.abbreviation
        )
        assign_permission_app.operate_page.open_to_permissions_page()

    for assignment_key in reversed(tracked["assignment"]):
        try:
            return_to_permission_settings()
            assign_permission_app.assign_permission_page.delete_assign_permission_if_exists(
                assignment_key
            )
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Assign permission cleanup failed: {assignment_key}",
                attachment_type=allure.attachment_type.TEXT,
            )

    for role_code in reversed(tracked["role"]):
        try:
            return_to_permission_settings()
            assign_permission_app.role_page.delete_role_if_exists(role_code)
        except Exception as error:
            allure.attach(str(error), name=f"Role cleanup failed: {role_code}")

    for scope_code in reversed(tracked["scope"]):
        try:
            return_to_permission_settings()
            assign_permission_app.scope_page.delete_scope_if_exists(scope_code)
        except Exception as error:
            allure.attach(str(error), name=f"Scope cleanup failed: {scope_code}")


@pytest.fixture
def assign_permission_prerequisites(
    assign_permission_app: OmniApp,
    assign_permission_data: AssignPermissionTestData,
    assign_permission_cleanup,
) -> AssignPermissionTestData:
    data = assign_permission_data
    for scope_code, scope_name, scope_description in (
        (data.scope_code, data.scope_name, data.scope_description),
        (data.updated_scope_code, data.updated_scope_name, data.updated_scope_description),
    ):
        assign_permission_cleanup("scope", scope_code)
        assign_permission_app.scope_page.create_scope(
            scope_code,
            scope_name,
            scope_description,
        )

    for role_code, role_name, role_description, scope_code in (
        (data.role_code, data.role_name, data.role_description, data.scope_code),
        (
            data.updated_role_code,
            data.updated_role_name,
            data.updated_role_description,
            data.updated_scope_code,
        ),
    ):
        assign_permission_cleanup("role", role_code)
        assign_permission_app.role_page.create_role(
            role_code,
            role_name,
            role_description,
            scope_code,
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
