from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import (
    BASE_URL_DEV,
    PROJECT_ABBR_PREFIX,
    PROJECT_DESCRIPTION_PREFIX,
    PROJECT_EN_NAME_PREFIX,
    PROJECT_ZH_NAME_PREFIX,
)
from utils.data_mode import should_cleanup


@dataclass(frozen=True)
class ProjectTestData:
    project_abbreviation: str
    zh_name: str
    en_name: str
    description: str
    updated_zh_name: str
    updated_en_name: str
    updated_description: str


@pytest.fixture
def project_data() -> ProjectTestData:
    suffix = uuid4().hex[:4]
    project_abbreviation = f"{PROJECT_ABBR_PREFIX}{suffix}"
    zh_name = f"{PROJECT_ZH_NAME_PREFIX}{suffix}"
    en_name = f"{PROJECT_EN_NAME_PREFIX}{suffix}"
    description = f"{PROJECT_DESCRIPTION_PREFIX}{suffix}"

    return ProjectTestData(
        project_abbreviation=project_abbreviation,
        zh_name=zh_name,
        en_name=en_name,
        description=description,
        updated_zh_name=f"updated-{zh_name}",
        updated_en_name=f"updated-{en_name}",
        updated_description=f"updated-{description}",
    )


@pytest.fixture
def project_app(logged_app: OmniApp) -> OmniApp:
    return logged_app


@pytest.fixture
def project_cleanup(project_app: OmniApp, data_mode: str):
    """登記測試建立的專案;isolated teardown 刪除，keep teardown 保留。"""
    tracked_abbreviations = []

    def track(project_abbreviation: str):
        if project_abbreviation not in tracked_abbreviations:
            tracked_abbreviations.append(project_abbreviation)

    yield track

    if not should_cleanup(data_mode):
        return

    for project_abbreviation in reversed(tracked_abbreviations):
        try:
            project_app.page.keyboard.press("Escape")
            project_app.page.goto(BASE_URL_DEV)
            project_app.project_page.delete_project_if_exists(project_abbreviation)
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Project cleanup failed: {project_abbreviation}",
                attachment_type=allure.attachment_type.TEXT,
            )


@pytest.fixture
def created_project(
    project_app: OmniApp,
    project_data: ProjectTestData,
    project_cleanup,
) -> ProjectTestData:
    project_cleanup(project_data.project_abbreviation)
    project_app.project_page.create_project(
        project_data.project_abbreviation,
        project_data.zh_name,
        project_data.en_name,
        project_data.description,
    )
    return project_data
