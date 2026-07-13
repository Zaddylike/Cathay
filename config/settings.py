import os
import sys

print(sys.argv)
print("lksjdflksdjflskdjflakrsjf;lkrg;")

# Testing Basic Parameters

BASE_URL_DEV = "https://dev.omnihubs.cloud/"
DEFAULT_TIMEOUT = 20000
DEFAULT_NAVIGATION_TIMEOUT = 60000
HEADLESS = False




# Acc & Pwd

ACCOUNT_USERNAME = "testuser01"
ACCOUNT_PASSWORD = "testuser01"

ENTRA_USERNAME = "omnitest3@cathlife.symphox.com"
ENTRA_PASSWORD = "Omni168168168"

GOOGLE_USERNAME = ""
GOOGLE_PASSWORD = ""

# Testing data

PROJECT_ABBR = "e2e-project-abbr"
SCOPE_CODE = "e2e-scope-code"
ROLE_CODE = "e2e-role-code"
GROUP_NAME = "e2e-group-name"

# 輸入驗證顆粒度類型

INPUT_BASIC_FIELD_CASES = [
    ("#" * 41, "輸入字數超過限制長度40"),
    ("", "必填欄位"),
]

INPUT_BASIC_DESC_CASES = [
    ("#" * 201, "輸入字數超過限制長度200"),
]