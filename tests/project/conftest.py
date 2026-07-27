import pytest

from app.omni_app import OmniApp
from data.factories.resource_data import (
    ProjectTestData,
    build_project_test_data,
)


@pytest.fixture
def project_data() -> ProjectTestData:
    return build_project_test_data()


@pytest.fixture
def created_project(
    logged_app: OmniApp,
    project_data: ProjectTestData,
    project_cleanup,
) -> ProjectTestData:
    project_cleanup(project_data.project_abbreviation)
    logged_app.project_page.create_project(
        project_data.project_abbreviation,
        project_data.zh_name,
        project_data.en_name,
        project_data.description,
    )
    return project_data
