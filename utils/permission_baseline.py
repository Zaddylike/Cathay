from app.omni_app import OmniApp
from config.settings import (
    BASE_URL_DEV,
    PERMISSION_ENTRA_ATTRIBUTE,
    PERMISSION_ENTRA_CLIENT_ID,
    PERMISSION_ENTRA_SECRET,
    PERMISSION_ENTRA_TENANT,
    PERMISSION_GOOGLE_CLIENT_ID,
    PERMISSION_GOOGLE_IDENTIFY_FIELD,
    PERMISSION_GOOGLE_SECRET,
    PERMISSION_OIDC_VALUE,
    PERMISSION_PROJECT_ABBR,
    PERMISSION_PROJECT_DESCRIPTION,
    PERMISSION_PROJECT_EN_NAME,
    PERMISSION_PROJECT_ZH_NAME,
    PERMISSION_ROLE_CODE,
    PERMISSION_ROLE_DESCRIPTION,
    PERMISSION_ROLE_NAME,
    PERMISSION_S2S_APPLICATION_NAME,
    PERMISSION_S2S_DESCRIPTION,
    PERMISSION_S2S_SCOPE_DESCRIPTION,
    PERMISSION_SCOPE_CODE,
    PERMISSION_SCOPE_DESCRIPTION,
    PERMISSION_SCOPE_NAME,
    PERMISSION_SECOND_ROLE_CODE,
    PERMISSION_SECOND_ROLE_DESCRIPTION,
    PERMISSION_SECOND_ROLE_NAME,
    PERMISSION_SECOND_SCOPE_CODE,
    PERMISSION_SECOND_SCOPE_DESCRIPTION,
    PERMISSION_SECOND_SCOPE_NAME,
    PERMISSION_SSO_APPLICATION_NAME,
    PERMISSION_SSO_LOGOUT_URL,
    PERMISSION_SSO_REDIRECT_URL,
    PERMISSION_THIRD_SCOPE_CODE,
    PERMISSION_THIRD_SCOPE_NAME,
    PROJECT_MEMBER_SECONDARY_KEYWORD,
)


def ensure_shared_project(app: OmniApp, create_missing: bool) -> None:
    """
    用途：確認固定共用專案 project-abbr-main 是否存在。

    執行流程：
        1. 回到專案列表並用完整 abbreviation 精準搜尋。
        2. 已存在時直接結束，不重複建立。
        3. 不存在且 create_missing=False 時立即 fail，符合 isolated 規則。
        4. 不存在且 create_missing=True 時建立固定共用專案，符合 keep 規則。
    """
    app.page.goto(BASE_URL_DEV)
    if app.project_page.project_exists(PERMISSION_PROJECT_ABBR):
        return
    if not create_missing:
        raise AssertionError(
            f"Required project does not exist: {PERMISSION_PROJECT_ABBR}"
        )
    app.project_page.create_project(
        PERMISSION_PROJECT_ABBR,
        PERMISSION_PROJECT_ZH_NAME,
        PERMISSION_PROJECT_EN_NAME,
        PERMISSION_PROJECT_DESCRIPTION,
    )


def open_shared_permission_project(app: OmniApp) -> None:
    """
    用途：將目前 Page 統一導向 project-abbr-main 的應用程式設定首頁。

    baseline 每完成一段流程後可能回到專案列表或新增頁，因此由此方法
    統一恢復下一個 baseline 檢查所需要的頁面狀態。
    """
    app.page.goto(BASE_URL_DEV)
    app.operate_page.go_to_permission_page(PERMISSION_PROJECT_ABBR)


def ensure_permission_project_member(
    app: OmniApp,
    project_abbreviation: str,
    create_missing: bool,
) -> None:
    """
    用途：確認 Permission Init 需要使用的測試成員已加入專案。

    執行流程：
        1. 進入指定專案的成員頁。
        2. 成員已存在就直接結束。
        3. isolated 不可修改 baseline，因此缺少時 fail。
        4. keep 可補資料，因此將固定測試成員加入專案。
    """
    app.page.goto(BASE_URL_DEV)
    app.project_member_page.open_to_member_page(project_abbreviation)
    if app.project_member_page.member_exists(PROJECT_MEMBER_SECONDARY_KEYWORD):
        return
    if not create_missing:
        raise AssertionError(
            "Required project member does not exist: "
            f"{PROJECT_MEMBER_SECONDARY_KEYWORD}"
        )
    app.project_member_page.go_to_member_edit_page()
    app.project_member_page.search_member_to_list(PROJECT_MEMBER_SECONDARY_KEYWORD)
    app.project_member_page.adjust_member_level()
    app.project_member_page.search_member_add(PROJECT_MEMBER_SECONDARY_KEYWORD)
    app.page.goto(BASE_URL_DEV)
    app.base_page.wait_loading_disapper()


def create_permission_initialization(app: OmniApp) -> None:
    """
    用途：執行只能做一次的 Permission Init wizard。

    建立內容：
        1. 固定 Scope 資料。
        2. 固定 Role 與 Scope 關聯。
        3. 跳過非必要的 Group／Assign Permission 初始資料。
        4. 建立 Default Permission 後送出初始化。

    此方法只負責建立；是否需要建立由 ensure_permission_initialization 判斷。
    """
    permission_page = app.application_permission_page
    elements = permission_page.elements
    permission_page.open_to_create_permission_page()
    scope_panels = app.page.locator(
        "app-permission-scope p-accordion-panel"
    )
    if scope_panels.count() != 1:
        raise AssertionError(
            f"Expected one initial Scope panel, got {scope_panels.count()}"
        )
    first_scope_panel = scope_panels.nth(0)
    first_scope_panel.locator('[formcontrolname="code"]').fill(
        PERMISSION_SCOPE_CODE
    )
    first_scope_panel.locator('[formcontrolname="name"]').fill(
        PERMISSION_SCOPE_NAME
    )
    first_scope_panel.locator('[formcontrolname="description"]').fill(
        PERMISSION_SCOPE_DESCRIPTION
    )
    elements.btn_permission_add_scope.click()
    scope_panels.nth(1).wait_for(state="attached")
    if scope_panels.count() != 2:
        raise AssertionError(
            f"Expected two Scope panels, got {scope_panels.count()}"
        )
    second_scope_panel = scope_panels.nth(1)
    second_scope_panel.locator('[formcontrolname="code"]').fill(
        PERMISSION_SECOND_SCOPE_CODE
    )
    second_scope_header = second_scope_panel.locator("p-accordion-header")
    if second_scope_header.get_attribute("aria-expanded") != "true":
        second_scope_header.locator(".border-circle").click()
    second_scope_panel.locator('[formcontrolname="name"]').fill(
        PERMISSION_SECOND_SCOPE_NAME
    )
    second_scope_panel.locator('[formcontrolname="description"]').fill(
        PERMISSION_SECOND_SCOPE_DESCRIPTION
    )
    permission_page.click_to_role_next_step()
    permission_page.click_to_extend_role_page()
    role_panels = app.page.locator(
        "app-permission-role p-accordion-panel"
    )
    if role_panels.count() != 1:
        raise AssertionError(
            f"Expected one initial Role panel, got {role_panels.count()}"
        )
    first_role_panel = role_panels.nth(0)
    first_role_panel.locator('[formcontrolname="code"]').fill(
        PERMISSION_ROLE_CODE
    )
    first_role_panel.locator('[formcontrolname="name"]').fill(
        PERMISSION_ROLE_NAME
    )
    first_role_panel.locator('[formcontrolname="description"]').fill(
        PERMISSION_ROLE_DESCRIPTION
    )
    permission_page.select_created_scope()
    elements.btn_permission_add_role.click()
    role_panels.nth(1).wait_for(state="attached")
    if role_panels.count() != 2:
        raise AssertionError(
            f"Expected two Role panels, got {role_panels.count()}"
        )
    second_role_panel = role_panels.nth(1)
    second_role_panel.locator('[formcontrolname="code"]').fill(
        PERMISSION_SECOND_ROLE_CODE
    )
    second_role_header = second_role_panel.locator("p-accordion-header")
    if second_role_header.get_attribute("aria-expanded") != "true":
        second_role_header.locator(".border-circle").click()
    second_role_panel.locator('[formcontrolname="name"]').fill(
        PERMISSION_SECOND_ROLE_NAME
    )
    second_role_panel.locator('[formcontrolname="description"]').fill(
        PERMISSION_SECOND_ROLE_DESCRIPTION
    )
    permission_page.create_scope_in_role_page(
        PERMISSION_SECOND_SCOPE_CODE,
        PERMISSION_SECOND_SCOPE_NAME,
        PERMISSION_THIRD_SCOPE_CODE,
        PERMISSION_THIRD_SCOPE_NAME,
    )
    permission_page.click_to_group_next_step()
    permission_page.click_to_permission_next_step()
    permission_page.click_to_default_permission_next_step()
    permission_page.create_role_for_member()
    permission_page.create_scope_for_member()
    permission_page.verify_permission_creation()


def ensure_permission_initialization(app: OmniApp, create_missing: bool) -> None:
    """
    用途：判斷目前專案是否已完成 Permission Init。

    判斷方式：
        1. 新增 Permission Init 按鈕仍存在，代表尚未初始化。
        2. 按鈕不存在，代表已初始化，直接結束。
        3. isolated 發現未初始化時 fail。
        4. keep 發現未初始化時呼叫 create_permission_initialization 補建。
    """
    if not app.application_permission_page.permission_initialization_available():
        return
    if not create_missing:
        raise AssertionError(
            f"Permission Init is missing from project: {PERMISSION_PROJECT_ABBR}"
        )
    create_permission_initialization(app)


def ensure_permission_scope(app: OmniApp, create_missing: bool) -> None:
    """
    用途：確認固定 Scope 可供 S2S baseline 選取。

    Permission Init 可能已完成但固定 Scope 被人工刪除，因此仍需單獨檢查：
        1. 固定 Scope 存在時直接結束。
        2. isolated 缺少時 fail。
        3. keep 缺少時補建固定 Scope。
    """
    app.operate_page.open_to_permissions_page()
    if app.scope_page.scope_exists(PERMISSION_SCOPE_CODE):
        return
    if not create_missing:
        raise AssertionError(f"Required Scope does not exist: {PERMISSION_SCOPE_CODE}")
    app.scope_page.create_scope(
        PERMISSION_SCOPE_CODE,
        PERMISSION_SCOPE_NAME,
        PERMISSION_SCOPE_DESCRIPTION,
    )


def create_sso_application(app: OmniApp) -> None:
    """
    用途：建立 Scope／Role／Group／Permission 測試依賴的固定 SSO Application。

    此流程使用 settings.py 的固定 provider 與 Application 資料，讓後續測試
    可以用名稱 permission-sso-main 精準確認 baseline，而不是任選一筆 SSO。
    """
    sso_page = app.single_sign_on_page
    sso_page.open_to_create_sso_page()
    app.operate_page.click_to_next_step()
    sso_page.create_provider_entraId()
    sso_page.input_entraId_clientId(PERMISSION_ENTRA_CLIENT_ID)
    sso_page.input_entraId_secret(PERMISSION_ENTRA_SECRET)
    sso_page.input_entraId_tenant(PERMISSION_ENTRA_TENANT)
    sso_page.verify_advanced(PERMISSION_ENTRA_TENANT, PERMISSION_ENTRA_ATTRIBUTE)
    sso_page.verify_dup_create()
    sso_page.create_provider_google()
    sso_page.input_google_clientId(PERMISSION_GOOGLE_CLIENT_ID)
    sso_page.input_google_secret(PERMISSION_GOOGLE_SECRET)
    sso_page.switch_whitelist_active()
    sso_page.input_identify_field(PERMISSION_GOOGLE_IDENTIFY_FIELD)
    sso_page.create_provider_oidc()
    sso_page.input_oidc_setting(PERMISSION_OIDC_VALUE)
    app.operate_page.click_to_next_step()
    sso_page.input_application_name(PERMISSION_SSO_APPLICATION_NAME)
    sso_page.select_tenant()
    sso_page.input_application_redirectUrl(PERMISSION_SSO_REDIRECT_URL)
    sso_page.input_application_logoutUrl(PERMISSION_SSO_LOGOUT_URL)
    sso_page.setting_date()
    sso_page.submit_sso_and_verify_success()


def ensure_sso_application(app: OmniApp, create_missing: bool) -> None:
    """
    用途：確認固定 SSO Application 是否存在。

    isolated 只檢查，缺少時 fail；keep 缺少時呼叫 create_sso_application 補建。
    """
    if app.single_sign_on_page.application_exists(PERMISSION_SSO_APPLICATION_NAME):
        return
    if not create_missing:
        raise AssertionError(
            f"Required SSO Application does not exist: {PERMISSION_SSO_APPLICATION_NAME}"
        )
    create_sso_application(app)


def create_s2s_application(app: OmniApp) -> None:
    """
    用途：建立 Scope／Role／Group／Permission 測試依賴的固定 S2S Application。

    建立時會選取固定 Scope，並相容目前系統可能出現的單頁版與兩步版 S2S UI。
    """
    s2s_page = app.server_to_server_page
    s2s_page.open_to_create_s2s_page()
    s2s_page.input_s2s_application_name(PERMISSION_S2S_APPLICATION_NAME)
    s2s_page.setting_date()
    s2s_page.input_application_description(PERMISSION_S2S_DESCRIPTION)
    s2s_page.continue_to_scope_step()
    s2s_page.create_scope()
    s2s_page.input_scope_description(PERMISSION_S2S_SCOPE_DESCRIPTION)
    s2s_page.submit_s2s_and_verify_success()


def ensure_s2s_application(app: OmniApp, create_missing: bool) -> None:
    """
    用途：確認固定 S2S Application 是否存在。

    isolated 只檢查，缺少時 fail；keep 缺少時呼叫 create_s2s_application 補建。
    """
    if app.server_to_server_page.application_exists(PERMISSION_S2S_APPLICATION_NAME):
        return
    if not create_missing:
        raise AssertionError(
            f"Required S2S Application does not exist: {PERMISSION_S2S_APPLICATION_NAME}"
        )
    create_s2s_application(app)


def ensure_permission_baseline(app: OmniApp, create_missing: bool) -> None:
    """
    用途：提供 Scope／Role／Group／Permission 共用的完整 baseline 入口。

    執行順序：
        1. 確認 project-abbr-main。
        2. 確認 Permission Init 所需的專案成員。
        3. 確認 Permission Init 已完成。
        4. 確認固定 Scope 存在。
        5. 確認固定 SSO Application 存在。
        6. 確認固定 S2S Application 存在。
        7. 最後重新進入主專案，讓呼叫端 fixture 從一致頁面繼續。

    create_missing=False：isolated，只檢查，缺少即 fail。
    create_missing=True：keep，缺少哪一項就補建哪一項。
    """
    ensure_shared_project(app, create_missing)
    ensure_permission_project_member(
        app,
        PERMISSION_PROJECT_ABBR,
        create_missing,
    )
    open_shared_permission_project(app)
    ensure_permission_initialization(app, create_missing)
    ensure_permission_scope(app, create_missing)
    ensure_sso_application(app, create_missing)
    open_shared_permission_project(app)
    ensure_s2s_application(app, create_missing)
    open_shared_permission_project(app)
