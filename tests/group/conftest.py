import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import GroupTestData, build_group_test_data
from utils.resource_cleanup import CleanupRegistry


@pytest.fixture
def group_app(permission_settings_sso_app: OmniApp) -> OmniApp:
    return permission_settings_sso_app


@pytest.fixture
def group_data() -> GroupTestData:
    return build_group_test_data()


@pytest.fixture
def group_cleanup(
    group_app: OmniApp,
    cleanup_registry: CleanupRegistry,
):
    def delete_group(group_name: str) -> None:
        group_app.page.keyboard.press("Escape")
        group_app.group_page.delete_group_if_exists(group_name)

    def register(group_name: str) -> None:
        def cleanup() -> None:
            delete_group(group_name)

        cleanup_registry.register(
            "Group",
            group_name,
            cleanup,
        )

    return register


@pytest.fixture
def created_group(
    group_app: OmniApp,
    group_data: GroupTestData,
    group_cleanup,
) -> GroupTestData:
    group_cleanup(group_data.name)
    group_app.group_page.create_group(
        group_data.name,
        group_data.description,
        group_data.member_keyword,
    )
    return group_data
