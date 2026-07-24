ValidationCase = tuple[str, str]
ValidationCases = tuple[ValidationCase, ...]


PERMISSION_CODE_CASES: ValidationCases = (
    ("中文", "只允許半形之英數字及符號：_-."),
    ("", "必填欄位"),
    ("$$$", "只允許半形之英數字及符號：_-."),
    ("ＡＢＣ", "只允許半形之英數字及符號：_-."),
    ("  ", "只允許半形之英數字及符號：_-."),
    ("#" * 21, "輸入字數超過限制長度20"),
)

PERMISSION_CREATE_NAME_CASES: ValidationCases = (
    ("#" * 41, "輸入字數超過限制長度40"),
    ("  ", "必填欄位"),
    ("", "必填欄位"),
)

PERMISSION_EDIT_NAME_CASES: ValidationCases = (
    ("  ", "必填欄位"),
    ("#" * 41, "輸入字數超過限制長度40"),
    ("", "必填欄位"),
)

PERMISSION_DESCRIPTION_CASES: ValidationCases = (
    ("#" * 201, "輸入字數超過限制長度200"),
)


def duplicate_permission_code_cases(code: str) -> ValidationCases:
    return ((code, " 代碼不可重複 "),)
