from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import GROUP_DESCRIPTION_PREFIX, GROUP_MEMBER_KEYWORD, GROUP_NAME
from utils.data_mode import should_cleanup


@dataclass(frozen=True)
class GroupTestData:
    name: str
    description: str
    copied_name: str
    copied_description: str
    updated_name: str
    updated_description: str
    member_keyword: str


@pytest.fixture
def group_data() -> GroupTestData:
    suffix = uuid4().hex[:4]
    name = f"{GROUP_NAME}{suffix}"
    description = f"{GROUP_DESCRIPTION_PREFIX}{suffix}"

    return GroupTestData(
        name=name,
        description=description,
        copied_name=f"copy-{name}",
        copied_description=f"copy-{description}",
        updated_name=f"updated-{name}",
        updated_description=f"updated-{description}",
        member_keyword=GROUP_MEMBER_KEYWORD,
    )


@pytest.fixture
def group_app(group_permission_project_app: OmniApp) -> OmniApp:
    group_permission_project_app.operate_page.open_to_permissions_page()
    return group_permission_project_app


@pytest.fixture
def group_cleanup(group_app: OmniApp, data_mode: str):
    """登記 UUID Group；yield 後 isolated 刪除，keep 保留。"""
    tracked_names = []

    def track(group_name: str):
        if group_name not in tracked_names:
            tracked_names.append(group_name)

    yield track

    if not should_cleanup(data_mode):
        return

    for group_name in reversed(tracked_names):
        try:
            group_app.page.keyboard.press("Escape")
            group_app.group_page.delete_group_if_exists(group_name)
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Group cleanup failed: {group_name}",
                attachment_type=allure.attachment_type.TEXT,
            )


@pytest.fixture
def created_group(group_app: OmniApp, group_data: GroupTestData, group_cleanup):
    group_cleanup(group_data.name)
    group_app.group_page.create_group(
        group_data.name,
        group_data.description,
        group_data.member_keyword,
    )
    return group_data
