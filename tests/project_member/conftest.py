from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import (
    BASE_URL_DEV,
    PROJECT_ABBR,
    PROJECT_DESCRIPTION_PREFIX,
    PROJECT_EN_NAME_PREFIX,
    PROJECT_MEMBER_PRIMARY_KEYWORD,
    PROJECT_MEMBER_READ_KEYWORDS,
    PROJECT_MEMBER_SECONDARY_KEYWORD,
    PROJECT_ZH_NAME_PREFIX,
)


@dataclass(frozen=True)
class ProjectMemberTestData:
    project_abbreviation: str
    project_zh_name: str
    project_en_name: str
    project_description: str
    primary_member: str
    secondary_member: str
    read_keywords: tuple[str, ...]


@pytest.fixture
def project_member_data() -> ProjectMemberTestData:
    suffix = uuid4().hex[:8]
    project_abbreviation = f"{PROJECT_ABBR}{suffix}"
    project_zh_name = f"{PROJECT_ZH_NAME_PREFIX}{suffix}"
    project_en_name = f"{PROJECT_EN_NAME_PREFIX}{suffix}"
    project_description = f"{PROJECT_DESCRIPTION_PREFIX}{suffix}"

    return ProjectMemberTestData(
        project_abbreviation=project_abbreviation,
        project_zh_name=project_zh_name,
        project_en_name=project_en_name,
        project_description=project_description,
        primary_member=PROJECT_MEMBER_PRIMARY_KEYWORD,
        secondary_member=PROJECT_MEMBER_SECONDARY_KEYWORD,
        read_keywords=PROJECT_MEMBER_READ_KEYWORDS,
    )


@pytest.fixture
def project_member_app(logged_app: OmniApp) -> OmniApp:
    return logged_app


@pytest.fixture
def member_project_cleanup(project_member_app: OmniApp):
    tracked_abbreviations = []

    def track(project_abbreviation: str):
        if project_abbreviation not in tracked_abbreviations:
            tracked_abbreviations.append(project_abbreviation)

    yield track

    for project_abbreviation in reversed(tracked_abbreviations):
        try:
            project_member_app.page.keyboard.press("Escape")
            project_member_app.page.goto(BASE_URL_DEV)
            project_member_app.project_page.delete_project_if_exists(
                project_abbreviation
            )
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Project member cleanup failed: {project_abbreviation}",
                attachment_type=allure.attachment_type.TEXT,
            )


@pytest.fixture
def created_member_project(
    project_member_app: OmniApp,
    project_member_data: ProjectMemberTestData,
    member_project_cleanup,
) -> ProjectMemberTestData:
    member_project_cleanup(project_member_data.project_abbreviation)
    project_member_app.project_page.create_project(
        project_member_data.project_abbreviation,
        project_member_data.project_zh_name,
        project_member_data.project_en_name,
        project_member_data.project_description,
    )
    return project_member_data


@pytest.fixture
def created_project_member(
    project_member_app: OmniApp,
    created_member_project: ProjectMemberTestData,
) -> ProjectMemberTestData:
    project_member_app.project_member_page.open_to_member_page(
        created_member_project.project_abbreviation
    )
    project_member_app.project_member_page.go_to_member_edit_page()
    project_member_app.project_member_page.search_member_to_list(
        created_member_project.primary_member
    )
    project_member_app.project_member_page.adjust_member_level()
    project_member_app.project_member_page.search_member_add(
        created_member_project.primary_member
    )
    return created_member_project
