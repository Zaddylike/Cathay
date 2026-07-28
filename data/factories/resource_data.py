from dataclasses import asdict, dataclass
from uuid import uuid4

from config.settings import (
    ASSIGN_PERMISSION_DESCRIPTION_PREFIX,
    ASSIGN_PERMISSION_MEMBER,
    ASSIGN_PERMISSION_SECOND_MEMBER,
    GROUP_DESCRIPTION_PREFIX,
    GROUP_MEMBER_KEYWORD,
    GROUP_NAME,
    PROJECT_ABBR_PREFIX,
    PROJECT_DESCRIPTION_PREFIX,
    PROJECT_EN_NAME_PREFIX,
    PROJECT_MEMBER_PRIMARY_KEYWORD,
    PROJECT_MEMBER_READ_KEYWORDS,
    PROJECT_MEMBER_SECONDARY_KEYWORD,
    PROJECT_ZH_NAME_PREFIX,
    ROLE_CODE,
    ROLE_DESCRIPTION_PREFIX,
    ROLE_NAME_PREFIX,
    SCOPE_CODE_PREFIX,
    SCOPE_DESCRIPTION_PREFIX,
    SCOPE_NAME_PREFIX,
)


def _new_suffix(length: int = 4) -> str:
    return uuid4().hex[:length]


@dataclass(frozen=True)
class ProjectTestData:
    project_abbreviation: str
    zh_name: str
    en_name: str
    description: str
    updated_zh_name: str
    updated_en_name: str
    updated_description: str


def build_project_test_data(suffix: str | None = None) -> ProjectTestData:
    suffix = suffix or _new_suffix()
    project_abbreviation = f"{PROJECT_ABBR_PREFIX}-{suffix}"
    zh_name = f"{PROJECT_ZH_NAME_PREFIX}-{suffix}"
    en_name = f"{PROJECT_EN_NAME_PREFIX}-{suffix}"
    description = f"{PROJECT_DESCRIPTION_PREFIX}-{suffix}"

    return ProjectTestData(
        project_abbreviation=project_abbreviation,
        zh_name=zh_name,
        en_name=en_name,
        description=description,
        updated_zh_name=f"updated-{zh_name}",
        updated_en_name=f"updated-{en_name}",
        updated_description=f"updated-{description}",
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


def build_project_member_test_data() -> ProjectMemberTestData:
    project = build_project_test_data(_new_suffix(length=8))
    return ProjectMemberTestData(
        project_abbreviation=project.project_abbreviation,
        project_zh_name=project.zh_name,
        project_en_name=project.en_name,
        project_description=project.description,
        primary_member=PROJECT_MEMBER_PRIMARY_KEYWORD,
        secondary_member=PROJECT_MEMBER_SECONDARY_KEYWORD,
        read_keywords=PROJECT_MEMBER_READ_KEYWORDS,
    )



# Scope Data 

@dataclass(frozen=True)
class ScopeTestData:
    code: str
    name: str
    description: str
    copied_code: str
    copied_name: str
    copied_description: str
    updated_name: str
    updated_description: str

def build_scope_test_data(suffix: str | None = None) -> ScopeTestData:
    suffix = suffix or _new_suffix()
    code = f"{SCOPE_CODE_PREFIX}-{suffix}"
    name = f"{SCOPE_NAME_PREFIX}-{suffix}"
    description = f"{SCOPE_DESCRIPTION_PREFIX}-{suffix}"

    return ScopeTestData(
        code=code,
        name=name,
        description=description,
        copied_code=f"copy-{code}",
        copied_name=f"copy-{name}",
        copied_description=f"copy-{description}",
        updated_name=f"updated-{name}",
        updated_description=f"updated-{description}",
    )



# Role Data

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


def build_role_test_data() -> RoleTestData:
    suffix = _new_suffix()
    scope = build_scope_test_data()
    code = f"{ROLE_CODE}-{suffix}"
    name = f"{ROLE_NAME_PREFIX}-{suffix}"
    description = f"{ROLE_DESCRIPTION_PREFIX}-{suffix}"

    return RoleTestData(
        code=code,
        name=name,
        description=description,
        copied_code=f"copy-{code}",
        copied_name=f"copy-{name}",
        copied_description=f"copy-{description}",
        updated_name=f"updated-{name}",
        updated_description=f"updated-{description}",
        scope_code=scope.code,
        scope_name=scope.name,
        scope_description=scope.description,
    )


@dataclass(frozen=True)
class GroupTestData:
    name: str
    description: str
    copied_name: str
    copied_description: str
    updated_name: str
    updated_description: str
    member_keyword: str


def build_group_test_data() -> GroupTestData:
    suffix = _new_suffix()
    name = f"{GROUP_NAME}-{suffix}"
    description = f"{GROUP_DESCRIPTION_PREFIX}-{suffix}"

    return GroupTestData(
        name=name,
        description=description,
        copied_name=f"copy-{name}",
        copied_description=f"copy-{description}",
        updated_name=f"updated-{name}",
        updated_description=f"updated-{description}",
        member_keyword=GROUP_MEMBER_KEYWORD,
    )


@dataclass(frozen=True)
class PermissionScenarioData:
    role_code: str
    role_name: str
    role_description: str
    scope_code: str
    scope_name: str
    scope_description: str
    updated_role_code: str
    updated_role_name: str
    updated_role_description: str
    updated_scope_code: str
    updated_scope_name: str
    updated_scope_description: str


def build_permission_scenario_data(
    suffix: str | None = None,
    updated_suffix: str | None = None,
) -> PermissionScenarioData:
    suffix = suffix or _new_suffix()
    updated_suffix = updated_suffix or _new_suffix()

    return PermissionScenarioData(
        role_code=f"{ROLE_CODE}-{suffix}",
        role_name=f"{ROLE_NAME_PREFIX}-{suffix}",
        role_description=f"{ROLE_DESCRIPTION_PREFIX}-{suffix}",
        scope_code=f"{SCOPE_CODE_PREFIX}-{suffix}",
        scope_name=f"{SCOPE_NAME_PREFIX}-{suffix}",
        scope_description=f"{SCOPE_DESCRIPTION_PREFIX}-{suffix}",
        updated_role_code=f"{ROLE_CODE}-{updated_suffix}",
        updated_role_name=f"{ROLE_NAME_PREFIX}-{updated_suffix}",
        updated_role_description=f"{ROLE_DESCRIPTION_PREFIX}-{updated_suffix}",
        updated_scope_code=f"{SCOPE_CODE_PREFIX}-{updated_suffix}",
        updated_scope_name=f"{SCOPE_NAME_PREFIX}-{updated_suffix}",
        updated_scope_description=f"{SCOPE_DESCRIPTION_PREFIX}-{updated_suffix}",
    )


DefaultPermissionTestData = PermissionScenarioData


@dataclass(frozen=True)
class AssignPermissionTestData(PermissionScenarioData):
    member: str
    second_member: str
    description: str
    second_description: str
    updated_description: str


def build_assign_permission_test_data() -> AssignPermissionTestData:
    suffix = _new_suffix()
    updated_suffix = _new_suffix()
    scenario = build_permission_scenario_data(suffix, updated_suffix)
    description = f"{ASSIGN_PERMISSION_DESCRIPTION_PREFIX}-{suffix}"
    second_description = f"{ASSIGN_PERMISSION_DESCRIPTION_PREFIX}-{updated_suffix}"
    
    return AssignPermissionTestData(
        **asdict(scenario),
        member=ASSIGN_PERMISSION_MEMBER,
        second_member=ASSIGN_PERMISSION_SECOND_MEMBER,
        description=description,
        second_description=second_description,
        updated_description=f"updated-{description}",
    )
