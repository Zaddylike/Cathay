import os
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
DEFAULT_TIMEOUT = 20000
DEFAULT_NAVIGATION_TIMEOUT = 60000


# Acc & Pwd
ACCOUNT_USERNAME = "testuser01"
ACCOUNT_PASSWORD = "testuser01"
ENTRA_USERNAME = "omnitest3@cathlife.symphox.com"
ENTRA_PASSWORD = "Omni168168168"
GOOGLE_USERNAME = ""
GOOGLE_PASSWORD = ""


# Testing prefix - project
PROJECT_ABBR = "project-abbr-"


# Testing prefix - Scope
SCOPE_CODE_PREFIX = "scopy-code-"
SCOPE_NAME_PREFIX = "scopy-name-"
SCOPE_DESCRIPTION_PREFIX = "scopy-description-"


# Testing prefix - Role
ROLE_CODE = "role-code-"


# Testing prefix = Group
GROUP_NAME = "group-name-"


# 輸入驗證顆粒度類型
INPUT_BASIC_FIELD_CASES = [
    ("#" * 41, "輸入字數超過限制長度40"),
    ("", "必填欄位"),
]
INPUT_BASIC_DESC_CASES = [
    ("#" * 201, "輸入字數超過限制長度200"),
]
