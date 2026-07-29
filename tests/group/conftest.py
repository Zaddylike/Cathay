import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import GroupTestData, build_group_test_data
from utils.resource_cleanup import CleanupRegistry


# 用途: 產生 Group 測試資料。
@pytest.fixture
def group_data() -> GroupTestData:
    return build_group_test_data()


# 用途: 登記 Group 測試資料，並在測試結束後清除。
@pytest.fixture
def group_cleanup(
    permission_sso_app: OmniApp,
    cleanup_registry: CleanupRegistry,
):
    def delete_group(group_name: str) -> None:
        permission_sso_app.page.keyboard.press("Escape")
        permission_sso_app.group_page.delete_group_if_exists(group_name)

    def register(group_name: str) -> None:
        def cleanup() -> None:
            delete_group(group_name)

        cleanup_registry.register(
            "Group",
            group_name,
            cleanup,
        )

    return register


# 用途: 建立供 Group 查詢、修改、刪除與複製測試使用的資料。
@pytest.fixture
def created_group(
    permission_sso_app: OmniApp,
    group_data: GroupTestData,
    group_cleanup,
) -> GroupTestData:
    group_cleanup(group_data.name)
    permission_sso_app.group_page.create_group(
        group_data.name,
        group_data.description,
        group_data.member_keyword,
    )
    return group_data
