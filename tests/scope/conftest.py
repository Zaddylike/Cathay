from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp


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
    suffix = uuid4().hex[:8]
    code = f"e2e-sc-{suffix}"
    return ScopeTestData(
        code=code,
        name=f"e2e-scope-{suffix}",
        description=f"e2e-scope-description-{suffix}",
        second_code=f"e2e-s2-{suffix}",
        second_name=f"e2e-scope-two-{suffix}",
        second_description=f"e2e-scope-two-description-{suffix}",
        copied_code=f"copy-{code}",
        copied_name=f"copy-scope-{suffix}",
        copied_description=f"copy-scope-description-{suffix}",
        updated_name=f"updated-scope-{suffix}",
        updated_description=f"updated-scope-description-{suffix}",
    )


@pytest.fixture
def scope_app(logged_app: OmniApp) -> OmniApp:
    logged_app.operate_page.go_to_permission_page()
    logged_app.operate_page.open_to_permissions_page()
    return logged_app


@pytest.fixture
def scope_cleanup(scope_app: OmniApp):
    tracked_codes = []

    def track(scope_code: str):
        if scope_code not in tracked_codes:
            tracked_codes.append(scope_code)

    yield track

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
def created_scope(scope_app: OmniApp, scope_data: ScopeTestData, scope_cleanup):
    scope_cleanup(scope_data.code)
    scope_app.scope_page.create_scope(
        scope_data.code,
        scope_data.name,
        scope_data.description,
    )
    return scope_data
