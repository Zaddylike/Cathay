from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import (
    SCOPE_CODE_PREFIX,
    SCOPE_DESCRIPTION_PREFIX,
    SCOPE_NAME_PREFIX,
)
from utils.data_mode import should_cleanup


@dataclass(frozen=True)
class ScopeTestData:
    code: str
    name: str
    description: str
    second_code: str
    second_name: str
    second_description: str
    copied_code: str
    copied_name: str
    copied_description: str
    updated_name: str
    updated_description: str


@pytest.fixture
def scope_data() -> ScopeTestData:
    suffix = uuid4().hex[:4]
    code = f"{SCOPE_CODE_PREFIX}{suffix}"
    name = f"{SCOPE_NAME_PREFIX}{suffix}"
    description=f"{SCOPE_DESCRIPTION_PREFIX}{suffix}"

    return ScopeTestData(
        code=code,
        name=name,
        description=description,
        second_code=f"{SCOPE_CODE_PREFIX}{uuid4().hex[:4]}",
        second_name=f"{SCOPE_NAME_PREFIX}{uuid4().hex[:4]}",
        second_description=f"{SCOPE_DESCRIPTION_PREFIX}{uuid4().hex[:4]}",
        copied_code=f"copy-{code}",
        copied_name=f"copy-{name}",
        copied_description=f"copy-{description}",
        updated_name=f"updated-{name}",
        updated_description=f"updated-{description}",
    )


@pytest.fixture
def scope_app(permission_project_app: OmniApp) -> OmniApp:
    permission_project_app.operate_page.open_to_permissions_page()
    return permission_project_app


"""登記 UUID Scope; yield 後 isolated 刪除,keep 保留。"""
@pytest.fixture
def scope_cleanup(scope_app: OmniApp, data_mode: str):
    tracked_codes = []

    def track(scope_code: str):
        if scope_code not in tracked_codes:
            tracked_codes.append(scope_code)

    yield track

    if not should_cleanup(data_mode):
        return

    for scope_code in reversed(tracked_codes):
        try:
            scope_app.page.keyboard.press("Escape")
            scope_app.scope_page.delete_scope_if_exists(scope_code)
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Scope cleanup failed: {scope_code}",
                attachment_type=allure.attachment_type.TEXT,
            )


@pytest.fixture
def created_scope_data(
    scope_app: OmniApp,
    scope_data: ScopeTestData,
    scope_cleanup,
) -> ScopeTestData:
    scope_cleanup(scope_data.code)
    scope_app.scope_page.create_scope(
        scope_data.code,
        scope_data.name,
        scope_data.description,
    )
    return scope_data
