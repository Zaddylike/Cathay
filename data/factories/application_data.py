from dataclasses import dataclass
from uuid import uuid4

from config.settings import (
    GROUP_DESCRIPTION_PREFIX,
    GROUP_NAME,
    PERMISSION_PROJECT_ABBR,
    PERMISSION_PROJECT_DESCRIPTION,
    PERMISSION_PROJECT_EN_NAME,
    PERMISSION_PROJECT_ZH_NAME,
    PROJECT_ABBR_PREFIX,
    PROJECT_DESCRIPTION_PREFIX,
    PROJECT_EN_NAME_PREFIX,
    PROJECT_MEMBER_SECONDARY_KEYWORD,
    PROJECT_ZH_NAME_PREFIX,
    ROLE_CODE,
    ROLE_DESCRIPTION_PREFIX,
    ROLE_NAME_PREFIX,
    SCOPE_CODE_PREFIX,
    SCOPE_DESCRIPTION_PREFIX,
    SCOPE_NAME_PREFIX,
)
from utils.data_mode import KEEP


@dataclass(frozen=True)
class ApplicationTestData:
    project_abbreviation: str
    project_zh_name: str
    project_en_name: str
    project_description: str
    entra_client_id: str
    entra_secret: str
    entra_tenant: str
    entra_attribute: str
    google_client_id: str
    google_secret: str
    google_identify_field: str
    oidc_value: str
    sso_application_name: str
    redirect_url: str
    logout_url: str
    s2s_application_name: str
    s2s_description: str
    s2s_scope_description: str
    scope_code: str
    scope_name: str
    scope_description: str
    second_scope_code: str
    second_scope_name: str
    second_scope_description: str
    third_scope_code: str
    third_scope_name: str
    role_code: str
    role_name: str
    role_description: str
    second_role_code: str
    second_role_name: str
    second_role_description: str
    group_name: str
    group_description: str
    group_member_description: str
    member_keyword: str
    assignment_description: str


def build_application_test_data(data_mode: str) -> ApplicationTestData:
    suffix = uuid4().hex[:4]

    if data_mode == KEEP:
        project_abbreviation = PERMISSION_PROJECT_ABBR
        project_zh_name = PERMISSION_PROJECT_ZH_NAME
        project_en_name = PERMISSION_PROJECT_EN_NAME
        project_description = PERMISSION_PROJECT_DESCRIPTION
    else:
        project_abbreviation = f"{PROJECT_ABBR_PREFIX}-{suffix}"
        project_zh_name = f"{PROJECT_ZH_NAME_PREFIX}-{suffix}"
        project_en_name = f"{PROJECT_EN_NAME_PREFIX}-{suffix}"
        project_description = f"{PROJECT_DESCRIPTION_PREFIX}-{suffix}"

    return ApplicationTestData(
        project_abbreviation=project_abbreviation,
        project_zh_name=project_zh_name,
        project_en_name=project_en_name,
        project_description=project_description,
        entra_client_id=f"entra-client-{suffix}",
        entra_secret=f"entra-secret-{suffix}",
        entra_tenant=f"entra-tenant-{suffix}",
        entra_attribute=f"entra-attribute-{suffix}",
        google_client_id=f"google-client-{suffix}",
        google_secret=f"google-secret-{suffix}",
        google_identify_field=f"google-identify-{suffix}",
        oidc_value=f"oidc-field-{suffix}",
        sso_application_name=f"sso-application-{suffix}",
        redirect_url=f"https://e2e/testing/omni/{suffix}",
        logout_url=f"https://e2e/testing/logout/{suffix}",
        s2s_application_name=f"s2s-application-{suffix}",
        s2s_description=f"s2s-description-{suffix}",
        s2s_scope_description=f"s2s-scope-{suffix}",
        scope_code=f"{SCOPE_CODE_PREFIX}-{suffix}",
        scope_name=f"{SCOPE_NAME_PREFIX}-{suffix}",
        scope_description=f"{SCOPE_DESCRIPTION_PREFIX}-{suffix}",
        second_scope_code=f"{SCOPE_CODE_PREFIX}-2-{suffix}",
        second_scope_name=f"{SCOPE_NAME_PREFIX}-2-{suffix}",
        second_scope_description=f"{SCOPE_DESCRIPTION_PREFIX}-2-{suffix}",
        third_scope_code=f"{SCOPE_CODE_PREFIX}-3-{suffix}",
        third_scope_name=f"{SCOPE_NAME_PREFIX}-3-{suffix}",
        role_code=f"{ROLE_CODE}-{suffix}",
        role_name=f"{ROLE_NAME_PREFIX}-{suffix}",
        role_description=f"{ROLE_DESCRIPTION_PREFIX}-{suffix}",
        second_role_code=f"{ROLE_CODE}-2-{suffix}",
        second_role_name=f"{ROLE_NAME_PREFIX}-2-{suffix}",
        second_role_description=f"{ROLE_DESCRIPTION_PREFIX}-2-{suffix}",
        group_name=f"{GROUP_NAME}-{suffix}",
        group_description=f"{GROUP_DESCRIPTION_PREFIX}-{suffix}",
        group_member_description=f"{GROUP_DESCRIPTION_PREFIX}-member-{suffix}",
        member_keyword=PROJECT_MEMBER_SECONDARY_KEYWORD,
        assignment_description=f"assignment-description-{suffix}",
    )
