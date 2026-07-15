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


@dataclass(frozen=True)
class RoleTestData:
    code: str
    name: str
    description: str
    copied_code: str
    copied_name: str
    copied_description: str
    updated_name: str
    updated_description: str

    scope_code: str
    scope_name: str
    scope_description: str

    updated_scope_code: str
    updated_scope_name: str
    updated_scope_description: str
    second_scope_code: str
    second_scope_name: str
    second_scope_description: str


@pytest.fixture
def role_data() -> RoleTestData:
    suffix = uuid4().hex[:4]
    code = f"{ROLE_CODE}{suffix}"
    name = f"{ROLE_NAME_PREFIX}{suffix}"
    description = f"{ROLE_DESCRIPTION_PREFIX}{suffix}"
    scope_suffix = uuid4().hex[:4]
    scope_code = f"{SCOPE_CODE_PREFIX}{scope_suffix}"
    scope_name = f"{SCOPE_NAME_PREFIX}{scope_suffix}"
    scope_description = f"{SCOPE_DESCRIPTION_PREFIX}{scope_suffix}"
    updated_scope_suffix = uuid4().hex[:4]
    second_scope_suffix = uuid4().hex[:4]

    return RoleTestData(
        code=code,
        name=name,
        description=description,
        copied_code=f"copy-{code}",
        copied_name=f"copy-{name}",
        copied_description=f"copy-{description}",
        updated_name=f"updated-{name}",
        updated_description=f"updated-{description}",

        scope_code=scope_code,
        scope_name=scope_name,
        scope_description=scope_description,
        updated_scope_code=f"{SCOPE_CODE_PREFIX}{updated_scope_suffix}",
        updated_scope_name=f"{SCOPE_NAME_PREFIX}{updated_scope_suffix}",
        updated_scope_description=f"{SCOPE_DESCRIPTION_PREFIX}{updated_scope_suffix}",
        second_scope_code=f"{SCOPE_CODE_PREFIX}{second_scope_suffix}",
        second_scope_name=f"{SCOPE_NAME_PREFIX}{second_scope_suffix}",
        second_scope_description=f"{SCOPE_DESCRIPTION_PREFIX}{second_scope_suffix}",
    )


@pytest.fixture
def role_app(logged_app: OmniApp) -> OmniApp:
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    return logged_app


@pytest.fixture
def role_cleanup(role_app: OmniApp):
    tracked_codes = {
        "role": [], 
        "scope": []
    }

    def track(resource_type: str, resource_code: str):
        if resource_code not in tracked_codes[resource_type]:
            tracked_codes[resource_type].append(resource_code)

    yield track

    for role_code in reversed(tracked_codes["role"]):
        try:
            role_app.page.keyboard.press("Escape")
            role_app.role_page.delete_role_if_exists(role_code)
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Role cleanup failed: {role_code}",
                attachment_type=allure.attachment_type.TEXT,
            )

    for scope_code in reversed(tracked_codes["scope"]):
        try:
            role_app.page.keyboard.press("Escape")
            role_app.scope_page.delete_scope_if_exists(scope_code)
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Scope cleanup failed: {scope_code}",
                attachment_type=allure.attachment_type.TEXT,
            )


@pytest.fixture
def prepared_role_scopes(
    role_app: OmniApp,
    role_data: RoleTestData,
    role_cleanup,
) -> RoleTestData:
    scopes = (
        (
            role_data.scope_code,
            role_data.scope_name,
            role_data.scope_description,
        ),
        (
            role_data.updated_scope_code,
            role_data.updated_scope_name,
            role_data.updated_scope_description,
        ),
        (
            role_data.second_scope_code,
            role_data.second_scope_name,
            role_data.second_scope_description,
        ),
    )

    for code, name, description in scopes:
        role_cleanup("scope", code)
        role_app.scope_page.create_scope(code, name, description)

    return role_data


@pytest.fixture
def created_role(
    role_app: OmniApp,
    prepared_role_scopes: RoleTestData,
    role_cleanup,
) -> RoleTestData:
    data = prepared_role_scopes
    role_cleanup("role", data.code)
    role_app.role_page.create_role(
        data.code,
        data.name,
        data.description,
        data.scope_code,
    )
    return data
