from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import (
    ASSIGN_PERMISSION_DESCRIPTION_PREFIX,
    ASSIGN_PERMISSION_MEMBER,
    ASSIGN_PERMISSION_SECOND_MEMBER,
    BASE_URL_DEV,
    GROUP_DESCRIPTION_PREFIX,
    GROUP_MEMBER_KEYWORD,
    GROUP_NAME,
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
from utils.data_mode import should_cleanup
from utils.permission_baseline import ensure_permission_project_member


@dataclass(frozen=True)
class SchemaValidationData:
    project_abbreviation: str
    project_zh_name: str
    project_en_name: str
    project_description: str
    updated_project_zh_name: str
    updated_project_en_name: str
    updated_project_description: str
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
    init_scope_code: str
    init_scope_name: str
    init_scope_description: str
    init_second_scope_code: str
    init_second_scope_name: str
    init_second_scope_description: str
    init_third_scope_code: str
    init_third_scope_name: str
    init_role_code: str
    init_role_name: str
    init_role_description: str
    init_second_role_code: str
    init_second_role_name: str
    init_second_role_description: str
    init_group_name: str
    init_group_description: str
    init_group_member_description: str
    init_assignment_description: str
    init_member_keyword: str
    scope_code: str
    scope_name: str
    scope_description: str
    copied_scope_code: str
    copied_scope_name: str
    copied_scope_description: str
    updated_scope_name: str
    updated_scope_description: str
    role_code: str
    role_name: str
    role_description: str
    copied_role_code: str
    copied_role_name: str
    copied_role_description: str
    updated_role_name: str
    updated_role_description: str
    group_name: str
    group_description: str
    updated_group_name: str
    updated_group_description: str
    assignment_description: str
    second_assignment_description: str
    updated_assignment_description: str


def build_schema_validation_data() -> SchemaValidationData:
    suffix = uuid4().hex[:4]
    scope_code = f"{SCOPE_CODE_PREFIX}-{suffix}"
    scope_name = f"{SCOPE_NAME_PREFIX}-{suffix}"
    scope_description = f"{SCOPE_DESCRIPTION_PREFIX}-{suffix}"
    role_code = f"{ROLE_CODE}-{suffix}"
    role_name = f"{ROLE_NAME_PREFIX}-{suffix}"
    role_description = f"{ROLE_DESCRIPTION_PREFIX}-{suffix}"
    group_name = f"{GROUP_NAME}-{suffix}"
    group_description = f"{GROUP_DESCRIPTION_PREFIX}-{suffix}"
    assignment_description = f"{ASSIGN_PERMISSION_DESCRIPTION_PREFIX}-{suffix}"

    return SchemaValidationData(
        project_abbreviation=f"{PROJECT_ABBR_PREFIX}-schema-{suffix}",
        project_zh_name=f"{PROJECT_ZH_NAME_PREFIX}-schema-{suffix}",
        project_en_name=f"{PROJECT_EN_NAME_PREFIX}-schema-{suffix}",
        project_description=f"{PROJECT_DESCRIPTION_PREFIX}-schema-{suffix}",
        updated_project_zh_name=f"updated-{PROJECT_ZH_NAME_PREFIX}-{suffix}",
        updated_project_en_name=f"updated-{PROJECT_EN_NAME_PREFIX}-{suffix}",
        updated_project_description=f"updated-{PROJECT_DESCRIPTION_PREFIX}-{suffix}",
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
        init_scope_code=f"{SCOPE_CODE_PREFIX}-i-{suffix}",
        init_scope_name=f"{SCOPE_NAME_PREFIX}-i-{suffix}",
        init_scope_description=f"{SCOPE_DESCRIPTION_PREFIX}-i-{suffix}",
        init_second_scope_code=f"{SCOPE_CODE_PREFIX}-i2-{suffix}",
        init_second_scope_name=f"{SCOPE_NAME_PREFIX}-i2-{suffix}",
        init_second_scope_description=f"{SCOPE_DESCRIPTION_PREFIX}i2-{suffix}",
        init_third_scope_code=f"{SCOPE_CODE_PREFIX}-i3-{suffix}",
        init_third_scope_name=f"{SCOPE_NAME_PREFIX}-i3-{suffix}",
        init_role_code=f"{ROLE_CODE}-i-{suffix}",
        init_role_name=f"{ROLE_NAME_PREFIX}-i-{suffix}",
        init_role_description=f"{ROLE_DESCRIPTION_PREFIX}-i-{suffix}",
        init_second_role_code=f"{ROLE_CODE}-i2-{suffix}",
        init_second_role_name=f"{ROLE_NAME_PREFIX}-i2-{suffix}",
        init_second_role_description=f"{ROLE_DESCRIPTION_PREFIX}-i2-{suffix}",
        init_group_name=f"{GROUP_NAME}-i-{suffix}",
        init_group_description=f"{GROUP_DESCRIPTION_PREFIX}-i-{suffix}",
        init_group_member_description=(
            f"{GROUP_DESCRIPTION_PREFIX}-member-{suffix}"
        ),
        init_assignment_description=f"assignment-description-{suffix}",
        init_member_keyword=PROJECT_MEMBER_SECONDARY_KEYWORD,
        scope_code=scope_code,
        scope_name=scope_name,
        scope_description=scope_description,
        copied_scope_code=f"copy-{scope_code}",
        copied_scope_name=f"copy-{scope_name}",
        copied_scope_description=f"copy-{scope_description}",
        updated_scope_name=f"updated-{scope_name}",
        updated_scope_description=f"updated-{scope_description}",
        role_code=role_code,
        role_name=role_name,
        role_description=role_description,
        copied_role_code=f"copy-{role_code}",
        copied_role_name=f"copy-{role_name}",
        copied_role_description=f"copy-{role_description}",
        updated_role_name=f"updated-{role_name}",
        updated_role_description=f"updated-{role_description}",
        group_name=group_name,
        group_description=group_description,
        updated_group_name=f"updated-{group_name}",
        updated_group_description=f"updated-{group_description}",
        assignment_description=assignment_description,
        second_assignment_description=f"second-{assignment_description}",
        updated_assignment_description=f"updated-{assignment_description}",
    )


@pytest.fixture
def schema_validation_data(
    logged_app: OmniApp,
    data_mode: str,
) -> SchemaValidationData:
    data = build_schema_validation_data()

    yield data

    if not should_cleanup(data_mode):
        return

    cleanup_errors = []

    def cleanup_step(resource_name: str, action) -> None:
        try:
            logged_app.page.keyboard.press("Escape")
            action()
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Schema cleanup failed: {resource_name}",
                attachment_type=allure.attachment_type.TEXT,
            )
            cleanup_errors.append(f"{resource_name}: {error}")

    logged_app.page.goto(BASE_URL_DEV)
    if not logged_app.project_page.project_exists(data.project_abbreviation):
        return

    logged_app.operate_page.go_to_permission_page(data.project_abbreviation)
    logged_app.operate_page.open_to_permissions_page()

    for role_code in (
        data.init_second_role_code,
        data.init_role_code,
    ):
        cleanup_step(
            f"Default Permission {role_code}",
            lambda role_code=role_code: logged_app.default_permission_page.delete_default_permission_if_exists(
                role_code
            ),
        )

    for assignment_key in (
        data.copied_role_code,
        data.role_code,
        data.init_second_role_code,
        data.init_role_code,
    ):
        cleanup_step(
            f"Assign Permission {assignment_key}",
            lambda assignment_key=assignment_key: logged_app.assign_permission_page.delete_assign_permission_if_exists(
                assignment_key
            ),
        )

    for group_name in (
        data.updated_group_name,
        data.group_name,
        data.init_group_name,
    ):
        cleanup_step(
            f"Group {group_name}",
            lambda group_name=group_name: logged_app.group_page.delete_group_if_exists(
                group_name
            ),
        )

    for role_code in (
        data.copied_role_code,
        data.role_code,
        data.init_second_role_code,
        data.init_role_code,
    ):
        cleanup_step(
            f"Role {role_code}",
            lambda role_code=role_code: logged_app.role_page.delete_role_if_exists(
                role_code
            ),
        )

    cleanup_step(
        f"SSO {data.sso_application_name}",
        lambda: logged_app.single_sign_on_page.delete_application_if_exists(
            data.sso_application_name
        ),
    )
    cleanup_step(
        f"S2S {data.s2s_application_name}",
        lambda: logged_app.server_to_server_page.delete_application_if_exists(
            data.s2s_application_name
        ),
    )

    logged_app.operate_page.open_to_permissions_page()
    for scope_code in (
        data.copied_scope_code,
        data.scope_code,
        data.init_third_scope_code,
        data.init_second_scope_code,
        data.init_scope_code,
    ):
        cleanup_step(
            f"Scope {scope_code}",
            lambda scope_code=scope_code: logged_app.scope_page.delete_scope_if_exists(
                scope_code
            ),
        )

    logged_app.page.goto(BASE_URL_DEV)
    cleanup_step(
        f"Project {data.project_abbreviation}",
        lambda: logged_app.project_page.delete_project_if_exists(
            data.project_abbreviation
        ),
    )

    if cleanup_errors:
        allure.attach(
            "\n".join(cleanup_errors),
            name=f"Schema validation cleanup failed: {data.project_abbreviation}",
            attachment_type=allure.attachment_type.TEXT,
        )
        raise AssertionError(
            f"Schema validation cleanup failed for "
            f"{data.project_abbreviation}: {'; '.join(cleanup_errors)}"
        )


def open_permission_settings(app: OmniApp, project_abbreviation: str) -> None:
    app.page.goto(BASE_URL_DEV)
    app.operate_page.go_to_permission_page(project_abbreviation)
    app.operate_page.open_to_permissions_page()


@allure.title("[SCHEMA] Validate every existing verify_input flow")
def test_all_existing_verify_input_flows(
    logged_app: OmniApp,
    schema_validation_data: SchemaValidationData,
):
    app = logged_app
    data = schema_validation_data

    with allure.step("Project Create schema validation"):
        app.project_page.open_create_project_dialog()
        app.project_page.validate_and_fill_project_abbreviation(
            data.project_abbreviation
        )
        app.project_page.validate_and_fill_project_zh_name(data.project_zh_name)
        app.project_page.fill_project_en_name(data.project_en_name)
        app.project_page.validate_and_add_project_tags()
        app.project_page.enable_project_status()
        app.project_page.validate_and_fill_project_description(
            data.project_description
        )
        app.project_page.select_project_icon()
        app.project_page.submit_project_and_verify_created(
            data.project_abbreviation
        )

    with allure.step("Project Update schema validation"):
        app.project_page.open_project_edit_form(data.project_abbreviation)
        app.project_page.validate_and_update_project_zh_name(
            data.updated_project_zh_name
        )
        app.project_page.update_project_en_name(data.updated_project_en_name)
        app.project_page.update_project_tag()
        app.project_page.disable_project_status()
        app.project_page.update_project_description(
            data.updated_project_description
        )
        app.project_page.update_project_icon()
        app.project_page.submit_project_update_and_verify(
            data.project_abbreviation
        )

    with allure.step("Restore Project status for dependent schema flows"):
        app.project_page.open_project_edit_form(data.project_abbreviation)
        app.project_page.enable_project_status()
        app.project_page.submit_project_update_and_verify(
            data.project_abbreviation
        )

    ensure_permission_project_member(
        app,
        data.project_abbreviation,
        create_missing=True,
    )

    with allure.step("Application SSO Init schema validation"):
        app.page.goto(BASE_URL_DEV)
        app.single_sign_on_page.open_to_permission_page(
            data.project_abbreviation
        )
        app.single_sign_on_page.open_to_create_sso_page()
        app.operate_page.click_to_next_step()
        app.single_sign_on_page.create_provider_entraId()
        app.single_sign_on_page.input_entraId_clientId(data.entra_client_id)
        app.single_sign_on_page.input_entraId_secret(data.entra_secret)
        app.single_sign_on_page.input_entraId_tenant(data.entra_tenant)
        app.single_sign_on_page.verify_advanced(
            data.entra_tenant,
            data.entra_attribute,
        )
        app.single_sign_on_page.verify_dup_create()
        app.single_sign_on_page.create_provider_google()
        app.single_sign_on_page.input_google_clientId(data.google_client_id)
        app.single_sign_on_page.input_google_secret(data.google_secret)
        app.single_sign_on_page.switch_whitelist_active()
        app.single_sign_on_page.input_identify_field(
            data.google_identify_field
        )
        app.single_sign_on_page.create_provider_oidc()
        app.single_sign_on_page.input_oidc_setting(data.oidc_value)
        app.operate_page.click_to_next_step()
        app.single_sign_on_page.input_application_name(
            data.sso_application_name
        )
        app.single_sign_on_page.select_tenant()
        app.single_sign_on_page.input_application_redirectUrl(
            data.redirect_url
        )
        app.single_sign_on_page.input_application_logoutUrl(data.logout_url)
        app.single_sign_on_page.setting_date()
        app.single_sign_on_page.submit_sso_and_verify_success()

    with allure.step("Application Permission Init schema validation"):
        app.page.goto(BASE_URL_DEV)
        app.application_permission_page.open_to_permission_page(
            data.project_abbreviation
        )
        app.application_permission_page.open_to_create_permission_page()
        app.application_permission_page.validate_and_fill_scope_code(
            data.init_scope_code
        )
        app.application_permission_page.validate_and_fill_scope_name(
            data.init_scope_name
        )
        app.application_permission_page.validate_and_fill_scope_description(
            data.init_scope_description
        )
        app.application_permission_page.validate_duplicate_scope(
            data.init_scope_code
        )
        app.application_permission_page.create_another_scope(
            data.init_second_scope_code,
            data.init_second_scope_name,
            data.init_second_scope_description,
        )
        app.application_permission_page.click_to_role_next_step()
        app.application_permission_page.click_to_extend_role_page()
        app.application_permission_page.validate_and_fill_role_code(
            data.init_role_code
        )
        app.application_permission_page.validate_and_fill_role_name(
            data.init_role_name
        )
        app.application_permission_page.validate_and_fill_role_description(
            data.init_role_description
        )
        app.application_permission_page.select_created_scope()
        app.application_permission_page.validate_duplicate_role(
            data.init_role_code
        )
        app.application_permission_page.create_another_role(
            data.init_second_role_code,
            data.init_second_role_name,
            data.init_second_role_description,
        )
        app.application_permission_page.create_scope_in_role_page(
            data.init_second_scope_code,
            data.init_second_scope_name,
            data.init_third_scope_code,
            data.init_third_scope_name,
        )
        app.application_permission_page.click_to_group_next_step()
        app.application_permission_page.click_to_extend_group_page()
        app.application_permission_page.validate_and_fill_group_name(
            data.init_group_name
        )
        app.application_permission_page.validate_and_fill_group_description(
            data.init_group_description
        )
        app.application_permission_page.invite_team_member(
            data.init_member_keyword,
            data.init_group_member_description,
        )
        app.application_permission_page.click_to_permission_next_step()
        app.application_permission_page.create_permission_setting(
            data.init_member_keyword
        )
        app.application_permission_page.create_permission_role()
        app.application_permission_page.create_permission_scope()
        app.application_permission_page.create_permission_description(
            data.init_assignment_description
        )
        app.application_permission_page.click_to_default_permission_next_step()
        app.application_permission_page.create_role_for_member()
        app.application_permission_page.create_scope_for_member()
        app.application_permission_page.verify_permission_creation()

    with allure.step("Application S2S Init schema validation"):
        app.page.goto(BASE_URL_DEV)
        app.server_to_server_page.open_to_permission_page(
            data.project_abbreviation
        )
        app.server_to_server_page.open_to_create_s2s_page()
        app.server_to_server_page.input_s2s_application_name(
            data.s2s_application_name
        )
        app.server_to_server_page.setting_date()
        app.server_to_server_page.input_application_description(
            data.s2s_description
        )
        app.server_to_server_page.continue_to_scope_step()
        app.server_to_server_page.create_scope(data.init_scope_code)
        app.server_to_server_page.input_scope_description(
            data.s2s_scope_description
        )
        app.server_to_server_page.submit_s2s_and_verify_success()

    with allure.step("Scope Create schema validation"):
        open_permission_settings(app, data.project_abbreviation)
        app.scope_page.click_to_create_scope_page()
        app.scope_page.validate_and_fill_scope_code(data.scope_code)
        app.scope_page.validate_and_fill_scope_name(data.scope_name)
        app.scope_page.validate_and_fill_scope_description(
            data.scope_description
        )
        app.scope_page.validate_duplicate_scope(data.scope_code)
        app.scope_page.submit_and_verify_created(data.scope_code)

    with allure.step("Scope Copy schema validation"):
        app.scope_page.click_to_copy_scope_page(data.scope_code)
        app.scope_page.validate_copy_and_fill_code(data.copied_scope_code)
        app.scope_page.validate_copy_and_fill_name(data.copied_scope_name)
        app.scope_page.validate_and_copy_scope_description(
            data.copied_scope_description
        )
        app.scope_page.submit_and_verify_copied(data.copied_scope_code)

    with allure.step("Scope Update schema validation"):
        app.scope_page.click_to_update_scope_page(data.scope_code)
        app.scope_page.validate_and_update_scope_name(data.updated_scope_name)
        app.scope_page.validate_and_update_scope_description(
            data.updated_scope_description
        )
        app.scope_page.disable_scope_status()
        app.scope_page.submit_and_verify_updated(data.updated_scope_name)

    with allure.step("Role Create schema validation"):
        app.role_page.click_to_create_role_page()
        app.role_page.validate_and_fill_role_code(data.role_code)
        app.role_page.validate_and_fill_role_name(data.role_name)
        app.role_page.validate_and_fill_role_description(data.role_description)
        app.role_page.select_role_scopes(data.init_scope_code)
        app.role_page.submit_and_verify_created(data.role_code)

    with allure.step("Role Copy schema validation"):
        app.role_page.click_to_copy_role_page(data.role_code)
        app.role_page.validate_copy_and_fill_code(data.copied_role_code)
        app.role_page.validate_copy_and_fill_name(data.copied_role_name)
        app.role_page.validate_and_copy_role_description(
            data.copied_role_description
        )
        app.role_page.submit_and_verify_copied(data.copied_role_code)

    with allure.step("Role Update schema validation"):
        app.role_page.click_to_update_role_page(data.role_code)
        app.role_page.validate_and_update_role_name(data.updated_role_name)
        app.role_page.validate_and_update_role_description(
            data.updated_role_description
        )
        app.role_page.add_role_scope(data.init_second_scope_code)
        app.role_page.submit_and_verify_updated(data.updated_role_name)

    with allure.step("Group Create schema validation"):
        app.group_page.click_to_create_group_page()
        app.group_page.open_create_group_page()
        app.group_page.validate_and_fill_group_name(data.group_name)
        app.group_page.validate_and_fill_group_description(
            data.group_description
        )
        app.group_page.invite_group_member(
            GROUP_MEMBER_KEYWORD,
            data.group_description,
        )
        app.group_page.submit_and_verify_created(data.group_name)

    with allure.step("Group Update schema validation"):
        app.group_page.click_to_group_page()
        app.group_page.open_update_group_page(data.group_name)
        app.group_page.validate_and_update_group_name(data.updated_group_name)
        app.group_page.validate_and_update_group_description(
            data.updated_group_description
        )
        app.group_page.disable_group_status()
        app.group_page.submit_and_verify_updated(data.updated_group_name)

    with allure.step("Assign Permission Create schema validation"):
        app.assign_permission_page.open_create_assign_permission_page()
        app.assign_permission_page.select_assign_permission_member(
            ASSIGN_PERMISSION_MEMBER
        )
        app.assign_permission_page.select_assign_role_permission(
            data.role_code
        )
        app.assign_permission_page.select_assign_scope_permission(
            data.init_scope_code
        )
        app.assign_permission_page.validate_and_fill_description(
            data.assignment_description
        )
        app.assign_permission_page.create_another_assign_permission(
            ASSIGN_PERMISSION_SECOND_MEMBER,
            data.copied_role_code,
            data.init_second_scope_code,
            data.second_assignment_description,
        )
        app.assign_permission_page.submit_and_verify_created(
            ASSIGN_PERMISSION_MEMBER
        )

    with allure.step("Assign Permission Update schema validation"):
        app.assign_permission_page.open_update_assign_permission_page(
            ASSIGN_PERMISSION_MEMBER
        )
        app.assign_permission_page.replace_assign_role_permission(
            data.copied_role_code
        )
        app.assign_permission_page.replace_assign_scope_permission(
            data.init_third_scope_code
        )
        app.assign_permission_page.validate_and_update_description(
            data.updated_assignment_description
        )
        app.assign_permission_page.submit_and_verify_updated(
            ASSIGN_PERMISSION_MEMBER
        )
