from app.omni_app import OmniApp
from config.settings import (
    BASE_URL_DEV,
    PERMISSION_ENTRA_ATTRIBUTE,
    PERMISSION_ENTRA_CLIENT_ID,
    PERMISSION_ENTRA_SECRET,
    PERMISSION_ENTRA_TENANT,
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
    PERMISSION_SSO_APPLICATION_NAME,
    PERMISSION_SSO_LOGOUT_URL,
    PERMISSION_SSO_REDIRECT_URL,
    PROJECT_MEMBER_SECONDARY_KEYWORD,
)


"""
用途:確認固定共用專案 project-abbr-main 是否存在。

執行流程:
    1. 回到專案列表並用完整 abbreviation 精準搜尋。
    2. 已存在時直接結束,不重複建立。
    3. 不存在且 create_missing=False 時立即 fail,符合 isolated 規則。
    4. 不存在且 create_missing=True 時建立固定共用專案,符合 keep 規則。
"""
def ensure_shared_project(app: OmniApp, create_missing: bool) -> None:
    app.page.goto(BASE_URL_DEV)
    if app.project_page.project_exists(PERMISSION_PROJECT_ABBR):
        return
    if not create_missing:
        raise AssertionError(f"Required project does not exist: {PERMISSION_PROJECT_ABBR}")
    app.project_page.create_project(
        PERMISSION_PROJECT_ABBR,
        PERMISSION_PROJECT_ZH_NAME,
        PERMISSION_PROJECT_EN_NAME,
        PERMISSION_PROJECT_DESCRIPTION,
    )


def open_shared_permission_project(app: OmniApp) -> None:
    """
    用途:將目前 Page 統一導向 project-abbr-main 的應用程式設定首頁。

    baseline 每完成一段流程後可能回到專案列表或新增頁,因此由此方法
    統一恢復下一個 baseline 檢查所需要的頁面狀態。
    """
    app.page.goto(BASE_URL_DEV)
    app.operate_page.go_to_permission_page(PERMISSION_PROJECT_ABBR)



"""
用途:確認 Permission Init 需要使用的測試成員已加入專案。

執行流程:
    1. 進入指定專案的成員頁。
    2. 成員已存在就直接結束。
    3. isolated 不可修改 baseline,因此缺少時 fail。
    4. keep 可補資料,因此將固定測試成員加入專案。
"""
def ensure_permission_project_member(
    app: OmniApp,
    project_abbreviation: str,
    create_missing: bool,
) -> None:
    app.page.goto(BASE_URL_DEV)
    app.project_member_page.open_to_member_page(project_abbreviation)
    if app.project_member_page.member_exists(PROJECT_MEMBER_SECONDARY_KEYWORD):
        app.page.goto(BASE_URL_DEV)
        return
    if not create_missing:
        raise AssertionError(
            f"Required project member does not exist: {PROJECT_MEMBER_SECONDARY_KEYWORD}"
        )
    app.project_member_page.go_to_member_edit_page()
    app.project_member_page.search_member_to_list(PROJECT_MEMBER_SECONDARY_KEYWORD)
    app.project_member_page.adjust_member_level()
    app.project_member_page.search_member_add(PROJECT_MEMBER_SECONDARY_KEYWORD)
    app.page.goto(BASE_URL_DEV)
    app.base_page.wait_loading_disapper()


"""
用途:執行只能做一次的 Permission Init wizard。

建立內容:
    1. 固定 Scope 資料。
    2. 固定 Role 與 Scope 關聯。
    3. 跳過非必要的 Group/Assign Permission 初始資料。
    4. 建立 Default Permission 後送出初始化。

此方法只負責建立;是否需要建立由 ensure_permission_initialization 判斷。
"""
def create_permission_initialization(app: OmniApp) -> None:
    permission_page = app.application_permission_page
    permission_page.open_to_create_permission_page()
    scope_panels = app.page.locator("app-permission-scope p-accordion-panel")
    if scope_panels.count() != 1:
        raise AssertionError(f"Expected one initial Scope panel, got {scope_panels.count()}")
    first_scope_panel = scope_panels.nth(0)
    first_scope_panel.locator('[formcontrolname="code"]').fill(PERMISSION_SCOPE_CODE)
    first_scope_panel.locator('[formcontrolname="name"]').fill(PERMISSION_SCOPE_NAME)
    first_scope_panel.locator('[formcontrolname="description"]').fill(PERMISSION_SCOPE_DESCRIPTION)
    permission_page.click_to_role_next_step()
    permission_page.click_to_group_next_step()
    permission_page.click_to_permission_next_step()
    permission_page.click_to_default_permission_next_step()
    permission_page.operate_page.submit_and_confirm(enabled_timeout=15_000)

"""
用途:判斷目前專案是否已完成 Permission Init。

判斷方式:
    1. 新增 Permission Init 按鈕仍存在,代表尚未初始化。
    2. 按鈕不存在,代表已初始化,直接結束。
    3. isolated 發現未初始化時 fail。
    4. keep 發現未初始化時呼叫 create_permission_initialization 補建。
"""
def ensure_permission_initialization(app: OmniApp, create_missing: bool) -> None:
    if not app.application_permission_page.permission_initialization_available():
        return
    if not create_missing:
        raise AssertionError(f"Permission Init is missing from project: {PERMISSION_PROJECT_ABBR}")
    create_permission_initialization(app)


"""
用途:確認固定 Scope 可供 S2S baseline 選取。

Permission Init 可能已完成但固定 Scope 被人工刪除,因此仍需單獨檢查:
    1. 固定 Scope 存在時直接結束。
    2. isolated 缺少時 fail。
    3. keep 缺少時補建固定 Scope。
"""
def ensure_permission_scope(app: OmniApp, create_missing: bool) -> None:
    """
    用途:確認固定 Scope 可供 S2S baseline 選取。

    Permission Init 可能已完成但固定 Scope 被人工刪除,因此仍需單獨檢查:
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


"""
用途:建立 Scope/Role/Group/Assign Permission 測試依賴的固定 SSO Application。
"""
def create_sso_application(app: OmniApp) -> None:
    sso_page = app.single_sign_on_page
    elements = sso_page.elements
    sso_page.open_to_create_sso_page()
    app.operate_page.click_to_next_step()
    sso_page.create_provider_entraId()
    elements.input_entra_clientId.fill(PERMISSION_ENTRA_CLIENT_ID)
    elements.input_entra_client_secret.fill(PERMISSION_ENTRA_SECRET)
    elements.input_entra_tenant_id.fill(PERMISSION_ENTRA_TENANT)
    sso_page.base_page.click_expect(
        elements.btn_entra_advanced_setting,
        elements.input_entra_authorization_uri,
    )
    elements.input_entra_user_name_attribute_name.fill(PERMISSION_ENTRA_ATTRIBUTE)
    app.operate_page.click_to_next_step()
    elements.input_application_name.fill(PERMISSION_SSO_APPLICATION_NAME)
    sso_page.select_tenant()
    elements.input_application_redirectUrl.fill(PERMISSION_SSO_REDIRECT_URL)
    elements.input_application_logoutUrl.fill(PERMISSION_SSO_LOGOUT_URL)
    sso_page.setting_date()
    sso_page.submit_sso_and_verify_success()
    app.base_page.click_expect(elements.btn_dialog_iknow, elements.btn_dialog_iknow)
    app.base_page.click_expect(elements.btn_dialog_iknow)


"""
用途:確認固定 SSO Application 是否存在。    
"""
def ensure_sso_application(app: OmniApp, create_missing: bool) -> None:
    if app.single_sign_on_page.application_exists(PERMISSION_SSO_APPLICATION_NAME):
        return
    if not create_missing:
        raise AssertionError(
            f"Required SSO Application does not exist: {PERMISSION_SSO_APPLICATION_NAME}"
        )
    create_sso_application(app)



"""
用途:建立 Scope/Role/Group/Permission 測試依賴的固定 S2S Application。

建立時會選取固定 Scope,並相容目前系統可能出現的單頁版與兩步版 S2S UI。
"""
def create_s2s_application(app: OmniApp) -> None:
    s2s_page = app.server_to_server_page
    s2s_page.open_to_create_s2s_page()
    s2s_page.input_s2s_application_name(PERMISSION_S2S_APPLICATION_NAME)
    s2s_page.setting_date()
    s2s_page.input_application_description(PERMISSION_S2S_DESCRIPTION)
    s2s_page.continue_to_scope_step()
    s2s_page.create_scope()
    s2s_page.input_scope_description(PERMISSION_S2S_SCOPE_DESCRIPTION)
    s2s_page.submit_s2s_and_verify_success()



"""
用途:確認固定 S2S Application 是否存在。

isolated 只檢查,缺少時 fail;keep 缺少時呼叫 create_s2s_application 補建。
"""
def ensure_s2s_application(app: OmniApp, create_missing: bool) -> None:
    if app.server_to_server_page.application_exists(PERMISSION_S2S_APPLICATION_NAME):
        return
    if not create_missing:
        raise AssertionError(
            f"Required S2S Application does not exist: {PERMISSION_S2S_APPLICATION_NAME}"
        )
    create_s2s_application(app)


"""
用途:提供 Scope/Role/Default Permission 共用的核心 baseline 入口。

執行順序:
    1. 確認 project-abbr-main。
    2. 確認 Permission Init 已完成。
    3. 最後重新進入主專案,讓呼叫端 fixture 從一致頁面繼續。

Assign Permission 的第二位成員與 Group 的 SSO 由各自 fixture 額外準備,
避免 Scope/Role/Default Permission 被迫建立不需要的 baseline。
"""
def ensure_permission_baseline(app: OmniApp, create_missing: bool) -> None:
    ensure_shared_project(app, create_missing)
    open_shared_permission_project(app)
    ensure_permission_initialization(app, create_missing)
    open_shared_permission_project(app)
