import sys

print(f"Testing Area -> {sys.argv}")

# Browser settings
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
HEADLESS = False


# Testing basic settings
BASE_URL_DEV = "https://dev.omnihubs.cloud/"
DEFAULT_TIMEOUT = 8000
DEFAULT_NAVIGATION_TIMEOUT = 60000


# Acc & Pwd
# 測試permission相關功能腳本(Scope,Role..)時-> 需確認測試帳號是否有已存在且有application資料的專案, testuser01現已有資料可直接使用
# 如非permission相關功能(Scope,Role..)腳本-> 可任意切換測試帳號
ACCOUNT_USERNAME = "testuser01"
ACCOUNT_PASSWORD = "testuser01"
ENTRA_USERNAME = "omnitest3@cathlife.symphox.com"
ENTRA_PASSWORD = "Omni168168168"
GOOGLE_USERNAME = ""
GOOGLE_PASSWORD = ""


# Testing prefix - project
PROJECT_ABBR = "project-abbr-"
PROJECT_ZH_NAME_PREFIX = "project-zh-"
PROJECT_EN_NAME_PREFIX = "project-en-"
PROJECT_DESCRIPTION_PREFIX = "project-description-"


# Testing prefix - Scope
SCOPE_CODE_PREFIX = "scopy-code-"
SCOPE_NAME_PREFIX = "scopy-name-"
SCOPE_DESCRIPTION_PREFIX = "scopy-description-"


# Testing prefix - Role
ROLE_CODE = "role-code-"
ROLE_NAME_PREFIX = "role-name-"
ROLE_DESCRIPTION_PREFIX = "role-description-"


# Testing prefix = Group
GROUP_NAME = "group-name-"
GROUP_DESCRIPTION_PREFIX = "group-description-"


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
