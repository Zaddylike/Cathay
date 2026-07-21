from collections.abc import Iterator
from dataclasses import dataclass
from uuid import uuid4

import allure
import pytest

from app.omni_app import OmniApp
from config.settings import (
    BASE_URL_DEV,
    GROUP_DESCRIPTION_PREFIX,
    GROUP_NAME,
    PERMISSION_PROJECT_ABBR,
    PERMISSION_PROJECT_DESCRIPTION,
    PERMISSION_PROJECT_EN_NAME,
    PERMISSION_PROJECT_ZH_NAME,
    PERMISSION_ROLE_CODE,
    PERMISSION_S2S_APPLICATION_NAME,
    PERMISSION_SCOPE_CODE,
    PERMISSION_SSO_APPLICATION_NAME,
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
from utils.data_mode import KEEP, permission_project_lock, should_cleanup
from utils.permission_baseline import (
    ensure_permission_project_member,
    ensure_permission_initialization,
    ensure_permission_scope,
    ensure_sso_application,
    ensure_shared_project,
)


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



"""
用途:建立每個 Application 測試專屬的測試資料。

執行流程:
    1. 每次 fixture 呼叫都產生新的 UUID suffix。
    2. isolated 使用 UUID 專案名稱，測試之間互不共用專案。
    3. keep 固定使用 project-abbr-main，但 SSO/S2S 名稱仍使用 UUID。
    4. 回傳 frozen dataclass，避免測試中意外修改資料。
"""
@pytest.fixture
def application_data(data_mode: str) -> ApplicationTestData:
    suffix = uuid4().hex[:4]

    if data_mode == KEEP:
        project_abbreviation = PERMISSION_PROJECT_ABBR
        project_zh_name = PERMISSION_PROJECT_ZH_NAME
        project_en_name = PERMISSION_PROJECT_EN_NAME
        project_description = PERMISSION_PROJECT_DESCRIPTION
    else:
        project_abbreviation = f"{PROJECT_ABBR_PREFIX}{suffix}"
        project_zh_name = f"{PROJECT_ZH_NAME_PREFIX}{suffix}"
        project_en_name = f"{PROJECT_EN_NAME_PREFIX}{suffix}"
        project_description = f"{PROJECT_DESCRIPTION_PREFIX}{suffix}"

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
        scope_code=f"{SCOPE_CODE_PREFIX}{suffix}",
        scope_name=f"{SCOPE_NAME_PREFIX}{suffix}",
        scope_description=f"{SCOPE_DESCRIPTION_PREFIX}{suffix}",
        second_scope_code=f"{SCOPE_CODE_PREFIX}2-{suffix}",
        second_scope_name=f"{SCOPE_NAME_PREFIX}2-{suffix}",
        second_scope_description=f"{SCOPE_DESCRIPTION_PREFIX}2-{suffix}",
        third_scope_code=f"{SCOPE_CODE_PREFIX}3-{suffix}",
        third_scope_name=f"{SCOPE_NAME_PREFIX}3-{suffix}",
        role_code=f"{ROLE_CODE}{suffix}",
        role_name=f"{ROLE_NAME_PREFIX}{suffix}",
        role_description=f"{ROLE_DESCRIPTION_PREFIX}{suffix}",
        second_role_code=f"{ROLE_CODE}2-{suffix}",
        second_role_name=f"{ROLE_NAME_PREFIX}2-{suffix}",
        second_role_description=f"{ROLE_DESCRIPTION_PREFIX}2-{suffix}",
        group_name=f"{GROUP_NAME}{suffix}",
        group_description=f"{GROUP_DESCRIPTION_PREFIX}{suffix}",
        group_member_description=f"{GROUP_DESCRIPTION_PREFIX}member-{suffix}",
        member_keyword=PROJECT_MEMBER_SECONDARY_KEYWORD,
        assignment_description=f"assignment-description-{suffix}",
    )



"""
用途:準備 Application 測試要進入的專案，並管理專案生命週期。

執行流程:
    1. keep 取得跨程序鎖，確認/建立 project-abbr-main 與固定專案成員。
    2. isolated 建立本次測試專屬的 UUID 專案與固定專案成員。
    3. yield 將 ApplicationTestData 交給測試程式使用。
    4. 測試結束後回到 finally。
    5. keep 直接保留專案;isolated 刪除自己建立的 UUID 專案。

注意:
    cleanup 只會使用 application_data.project_abbreviation，
    isolated 不會碰到 project-abbr-main。
"""
@pytest.fixture
def application_project(
    logged_app: OmniApp,
    application_data: ApplicationTestData,
    data_mode: str,
) -> Iterator[ApplicationTestData]:
    test_started = False

    try:
        if data_mode == KEEP:
            with permission_project_lock():
                ensure_shared_project(logged_app, create_missing=True)
                ensure_permission_project_member(
                    logged_app,
                    application_data.project_abbreviation,
                    create_missing=True,
                )
        else:
            logged_app.project_page.create_project(
                application_data.project_abbreviation,
                application_data.project_zh_name,
                application_data.project_en_name,
                application_data.project_description,
            )
            ensure_permission_project_member(
                logged_app,
                application_data.project_abbreviation,
                create_missing=True,
            )

        test_started = True
        yield application_data
    finally:
        if should_cleanup(data_mode):
            try:
                if application_data.project_abbreviation == PERMISSION_PROJECT_ABBR:
                    raise AssertionError(
                        "Isolated Application cleanup received the baseline project"
                    )
                if application_data.sso_application_name == PERMISSION_SSO_APPLICATION_NAME:
                    raise AssertionError(
                        "Isolated Application cleanup received the baseline SSO application"
                    )
                if application_data.s2s_application_name == PERMISSION_S2S_APPLICATION_NAME:
                    raise AssertionError(
                        "Isolated Application cleanup received the baseline S2S application"
                    )

                logged_app.page.keyboard.press("Escape")
                logged_app.page.goto(BASE_URL_DEV)
                if logged_app.project_page.project_exists(
                    application_data.project_abbreviation
                ):
                    if test_started:
                        logged_app.operate_page.go_to_permission_page(
                            application_data.project_abbreviation
                        )
                        logged_app.single_sign_on_page.delete_application_if_exists(
                            application_data.sso_application_name
                        )
                        logged_app.server_to_server_page.delete_application_if_exists(
                            application_data.s2s_application_name
                        )
                        logged_app.page.goto(BASE_URL_DEV)

                    logged_app.project_page.delete_project_if_exists(
                        application_data.project_abbreviation
                    )
            except Exception as error:
                allure.attach(
                    str(error),
                    name=(
                        "Application project cleanup failed: "
                        f"{application_data.project_abbreviation}"
                    ),
                    attachment_type=allure.attachment_type.TEXT,
                )
                raise AssertionError(
                    "Application isolated cleanup failed for "
                    f"{application_data.project_abbreviation}: {error}"
                ) from error



"""
用途:提供 S2S 測試可選取的 Permission Scope 前置資料。

執行流程:
    1. application_project 先準備測試專案。
    2. 確認 Permission Init 已完成。
    3. 確認固定 Scope 存在，讓 S2S 建立頁可以精準選取。
    4. keep 使用跨程序鎖，避免平行 process 同時補建前置資料。
    5. yield 將測試資料交給主測試。
    6. isolated 測試結束後依序刪除 Default Permission、Role、S2S、Scope。
    7. application_project 最後刪除 UUID Project。
"""
@pytest.fixture
def application_s2s_project(
    logged_app: OmniApp,
    application_project: ApplicationTestData,
    data_mode: str,
) -> Iterator[ApplicationTestData]:
    data = application_project

    """將目前 Page 準備成 S2S 測試可開始的專案狀態"""
    def prepare_permission_scope():
        logged_app.page.goto(BASE_URL_DEV)
        logged_app.operate_page.go_to_permission_page(data.project_abbreviation)
        ensure_permission_initialization(logged_app, create_missing=True)
        ensure_permission_scope(logged_app, create_missing=True)
        logged_app.page.goto(BASE_URL_DEV)

    try:
        if data_mode == KEEP:
            with permission_project_lock():
                prepare_permission_scope()
        else:
            prepare_permission_scope()
        yield data
    finally:
        if should_cleanup(data_mode):
            try:
                if data.project_abbreviation == PERMISSION_PROJECT_ABBR:
                    raise AssertionError(
                        "Isolated S2S cleanup received the baseline project"
                    )
                if data.s2s_application_name == PERMISSION_S2S_APPLICATION_NAME:
                    raise AssertionError(
                        "Isolated S2S cleanup received the baseline S2S application"
                    )

                logged_app.page.keyboard.press("Escape")
                logged_app.page.goto(BASE_URL_DEV)
                if logged_app.project_page.project_exists(data.project_abbreviation):
                    logged_app.operate_page.go_to_permission_page(
                        data.project_abbreviation
                    )
                    permission_initialized = not logged_app.application_permission_page.permission_initialization_available()
                    if permission_initialized:
                        logged_app.default_permission_page.delete_default_permission_if_exists(
                            PERMISSION_ROLE_CODE
                        )
                        logged_app.role_page.delete_role_if_exists(
                            PERMISSION_ROLE_CODE
                        )

                    logged_app.server_to_server_page.delete_application_if_exists(
                        data.s2s_application_name
                    )

                    if permission_initialized:
                        logged_app.operate_page.open_to_permissions_page()
                        logged_app.scope_page.delete_scope_if_exists(
                            PERMISSION_SCOPE_CODE
                        )
            except Exception as error:
                allure.attach(
                    str(error),
                    name=f"S2S prerequisite cleanup failed: {data.project_abbreviation}",
                    attachment_type=allure.attachment_type.TEXT,
                )
                raise AssertionError(
                    "S2S isolated prerequisite cleanup failed for "
                    f"{data.project_abbreviation}: {error}"
                ) from error




"""
用途:提供 Permission Init 測試專用的專案狀態。

執行流程:
    1. application_project 先準備 isolated UUID 專案或 keep 主專案。
    2. 確認/建立 Group 需要的固定 SSO 前置資料。
    3. keep 使用鎖檢查主專案是否已完成 Permission Init。
    4. keep 已初始化時 pytest.skip，避免重複執行一次性 wizard。
    5. isolated 的新專案若已初始化，代表環境異常並直接 fail。
    6. yield 將測試資料交給主測試。
    7. isolated 依序刪除 Default、Assign、Group、Role、SSO、Scope。
    8. application_project 最後刪除 UUID Project。
"""
@pytest.fixture
def application_permission_init_project(
    logged_app: OmniApp,
    application_project: ApplicationTestData,
    data_mode: str,
) -> Iterator[ApplicationTestData]:
    data = application_project

    def prepare_permission_initialization() -> bool:
        logged_app.page.goto(BASE_URL_DEV)
        logged_app.operate_page.go_to_permission_page(data.project_abbreviation)
        if not logged_app.application_permission_page.permission_initialization_available():
            return False
        ensure_sso_application(logged_app, create_missing=True)
        logged_app.page.goto(BASE_URL_DEV)
        return True

    if data_mode == KEEP:
        with permission_project_lock():
            if not prepare_permission_initialization():
                pytest.skip(
                    f"Permission Init already exists in {data.project_abbreviation}"
                )
            yield data
        return

    cleanup_errors = []

    def cleanup_step(resource_name: str, action) -> None:
        try:
            logged_app.page.keyboard.press("Escape")
            action()
        except Exception as error:
            allure.attach(
                str(error),
                name=f"Permission Init cleanup failed: {resource_name}",
                attachment_type=allure.attachment_type.TEXT,
            )
            cleanup_errors.append(f"{resource_name}: {error}")

    try:
        if not prepare_permission_initialization():
            pytest.fail(
                f"Fresh project is already initialized: {data.project_abbreviation}"
            )
        yield data
    finally:
        try:
            if data.project_abbreviation == PERMISSION_PROJECT_ABBR:
                raise AssertionError(
                    "Isolated Permission Init cleanup received the baseline project"
                )

            logged_app.page.keyboard.press("Escape")
            logged_app.page.goto(BASE_URL_DEV)
            if logged_app.project_page.project_exists(data.project_abbreviation):
                logged_app.operate_page.go_to_permission_page(
                    data.project_abbreviation
                )
                logged_app.operate_page.open_to_permissions_page()
                permission_initialized = not logged_app.application_permission_page.permission_initialization_available()

                if permission_initialized:
                    for role_code in (
                        data.second_role_code,
                        data.role_code,
                    ):
                        cleanup_step(
                            f"Default Permission {role_code}",
                            lambda role_code=role_code: logged_app.default_permission_page.delete_default_permission_if_exists(
                                role_code
                            ),
                        )
                    for role_code in (
                        data.second_role_code,
                        data.role_code,
                    ):
                        cleanup_step(
                            f"Assign Permission {role_code}",
                            lambda role_code=role_code: logged_app.assign_permission_page.delete_assign_permission_if_exists(
                                role_code
                            ),
                        )
                    cleanup_step(
                        f"Group {data.group_name}",
                        lambda: logged_app.group_page.delete_group_if_exists(
                            data.group_name
                        ),
                    )
                    for role_code in (
                        data.second_role_code,
                        data.role_code,
                    ):
                        cleanup_step(
                            f"Role {role_code}",
                            lambda role_code=role_code: logged_app.role_page.delete_role_if_exists(
                                role_code
                            ),
                        )

                cleanup_step(
                    f"SSO {PERMISSION_SSO_APPLICATION_NAME}",
                    lambda: logged_app.single_sign_on_page.delete_application_if_exists(
                        PERMISSION_SSO_APPLICATION_NAME
                    ),
                )

                if permission_initialized:
                    logged_app.operate_page.open_to_permissions_page()
                    for scope_code in (
                        data.third_scope_code,
                        data.second_scope_code,
                        data.scope_code,
                    ):
                        cleanup_step(
                            f"Scope {scope_code}",
                            lambda scope_code=scope_code: logged_app.scope_page.delete_scope_if_exists(
                                scope_code
                            ),
                        )
        except Exception as error:
            allure.attach(
                str(error),
                name=(
                    "Permission Init prerequisite cleanup failed: "
                    f"{data.project_abbreviation}"
                ),
                attachment_type=allure.attachment_type.TEXT,
            )
            cleanup_errors.append(str(error))

        if cleanup_errors:
            raise AssertionError(
                "Permission Init isolated cleanup failed for "
                f"{data.project_abbreviation}: {'; '.join(cleanup_errors)}"
            )
