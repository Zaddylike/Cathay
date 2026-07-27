import sys
from datetime import datetime

now = datetime.now()
print(f'Testing Path: {sys.argv}')
print(f'Starting Time: {now.strftime("%Y/%m/%d %H:%M")}')

# Browser settings
HEADLESS = True
DELAY_TIME = 0
BROWSER_ARGS = [
    "--start-maximized",
    "--window-position=0,0",
    "--disable-features=Translate,TranslateUI",
    "--disable-translate",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
    "--disable-blink-features=AutomationControlled",
]

# Testing basic settings
BASE_URL_DEV = "https://dev.omnihubs.cloud/"
# BASE_URL_DEV = "https://dev.omnihubs.cloud/be-upgrade/s/"
DEFAULT_TIMEOUT = 12000
DEFAULT_NAVIGATION_TIMEOUT = 60000
LOGIN_TIMEOUT = 60000


# Acc & Pwd
# 測試permission相關功能腳本(Scope,Role..)時-> 需確認測試帳號是否有已存在且有application資料的專案, user 01現已有資料可直接使用
# 如非permission相關功能(Scope,Role..)腳本-> 可任意切換測試帳號

ACCOUNT_USERNAME = "testuser01"
ACCOUNT_PASSWORD = "testuser01"
ACCOUNT_USERNAME_2 = "testuser02"
ACCOUNT_PASSWORD_2 = "testuser02"
ENTRA_USERNAME = "omnitest3@cathlife.symphox.com"
ENTRA_PASSWORD = "Omni168168168"
GOOGLE_USERNAME = ""
GOOGLE_PASSWORD = ""
# ACCOUNT_USERNAME = "user01"
# ACCOUNT_PASSWORD = "pass1"


# PROJECT prefix
PROJECT_ABBR_PREFIX = "project-abbr"
PROJECT_ZH_NAME_PREFIX = "project-zh"
PROJECT_EN_NAME_PREFIX = "project-en"
PROJECT_DESCRIPTION_PREFIX = "project-description"

# Testing prefix - Scope
SCOPE_CODE_PREFIX = "scope-code"
SCOPE_NAME_PREFIX = "scope-name"
SCOPE_DESCRIPTION_PREFIX = "scope-description"

# Testing prefix - Role
ROLE_CODE = "role-code"
ROLE_NAME_PREFIX = "role-name"
ROLE_DESCRIPTION_PREFIX = "role-description"

# Testing prefix = Group
GROUP_NAME = "group-name"
GROUP_DESCRIPTION_PREFIX = "group-description"


# Stable permission project used by Scope / Role / Group / Permission tests
PERMISSION_PROJECT_ABBR = "project-abbr-main"
PERMISSION_PROJECT_ZH_NAME = "project-zh-main"
PERMISSION_PROJECT_EN_NAME = "project-en-main"
PERMISSION_PROJECT_DESCRIPTION = "project-description-main"

# Stable Application baseline used by permission feature tests
PERMISSION_SSO_APPLICATION_NAME = "permission-sso-main"
PERMISSION_S2S_APPLICATION_NAME = "permission-s2s-main"
PERMISSION_S2S_DESCRIPTION = "permission-s2s-description-main"
PERMISSION_S2S_SCOPE_DESCRIPTION = "s2s-scope-main"

# Stable Permission Init data for the shared permission project
PERMISSION_SCOPE_CODE = "perm-scope-main"
PERMISSION_SCOPE_NAME = "permission-scope-name-main"
PERMISSION_SCOPE_DESCRIPTION = "permission-scope-description-main"
PERMISSION_THIRD_SCOPE_CODE = "perm-scope-3-main"
PERMISSION_THIRD_SCOPE_NAME = "permission-scope-third-name-main"
PERMISSION_ROLE_CODE = "perm-role-main"
PERMISSION_ROLE_NAME = "permission-role-name-main"
PERMISSION_ROLE_DESCRIPTION = "permission-role-description-main"
PERMISSION_GROUP_NAME = "permission-group-main"
PERMISSION_GROUP_DESCRIPTION = "permission-group-description-main"
PERMISSION_GROUP_MEMBER_DESCRIPTION = "permission-group-member-description-main"
PERMISSION_ASSIGNMENT_DESCRIPTION = "permission-assignment-description-main"

# Stable SSO provider data for the shared permission project
PERMISSION_ENTRA_CLIENT_ID = "entra-client-main"
PERMISSION_ENTRA_SECRET = "entra-secret-main"
PERMISSION_ENTRA_TENANT = "entra-tenant-main"
PERMISSION_ENTRA_ATTRIBUTE = "entra-attr-main"
PERMISSION_GOOGLE_CLIENT_ID = "google-client-main"
PERMISSION_GOOGLE_SECRET = "google-secret-main"
PERMISSION_GOOGLE_IDENTIFY_FIELD = "google-id-main"
PERMISSION_OIDC_VALUE = "oidc-main"
PERMISSION_SSO_REDIRECT_URL = "https://e2e/testing/omni/permission-main"
PERMISSION_SSO_LOGOUT_URL = "https://e2e/testing/logout/permission-main"





# Testing references - permission and member
GROUP_MEMBER_KEYWORD = "testuser01"
ASSIGN_PERMISSION_MEMBER = "testuser01"
ASSIGN_PERMISSION_SECOND_MEMBER = "testuser02"
ASSIGN_PERMISSION_DESCRIPTION_PREFIX = "assign-description-"
PROJECT_MEMBER_PRIMARY_KEYWORD = "測試人員3"
PROJECT_MEMBER_SECONDARY_KEYWORD = "測試人員2"
PROJECT_MEMBER_READ_KEYWORDS = (
    "testuser01",
    "OmniHub",
    "數位數據",
    "omnitest3",
)


# input field some wrong data to valid schema
INPUT_BASIC_FIELD_CASES = [
    ("#" * 41, "輸入字數超過限制長度40"),
    ("", "必填欄位"),
]
INPUT_BASIC_DESC_CASES = [
    ("#" * 201, "輸入字數超過限制長度200"),
]
