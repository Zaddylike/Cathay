import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import (
    ProjectMemberTestData,
    build_project_member_test_data,
)


@pytest.fixture
def project_member_data() -> ProjectMemberTestData:
    return build_project_member_test_data()


@pytest.fixture
def created_member_project(
    logged_app: OmniApp,
    project_member_data: ProjectMemberTestData,
    project_cleanup,
) -> ProjectMemberTestData:
    project_cleanup(project_member_data.project_abbreviation)

    logged_app.project_page.create_project(
        project_member_data.project_abbreviation,
        project_member_data.project_zh_name,
        project_member_data.project_en_name,
        project_member_data.project_description,
    )
    
    return project_member_data


@pytest.fixture
def created_project_member(
    logged_app: OmniApp,
    created_member_project: ProjectMemberTestData,
) -> ProjectMemberTestData:
    logged_app.project_member_page.open_to_member_page(created_member_project.project_abbreviation)
    logged_app.project_member_page.go_to_member_edit_page()
    logged_app.project_member_page.search_member_to_list(created_member_project.primary_member)
    logged_app.project_member_page.adjust_member_level()
    logged_app.project_member_page.search_member_add(created_member_project.primary_member)
    return created_member_project
