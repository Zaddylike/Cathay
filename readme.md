# Omni Autotest

Cathay OmniHub UI 自動化測試專案，使用 **Python、Pytest、Playwright** 與 **Allure**。

## 主要功能

- 測試 Login、Project、Application、Scope、Role、Group 與 Permission。
- 使用 Page Object 管理頁面操作與 Locator。
- 使用 Pytest fixtures 建立測試前置資料與執行 cleanup。
- 使用 UUID 建立每次測試的專屬資料，降低案例互相影響。
- 支援 `isolated` 與 `keep` 兩種測試資料模式。
- 自動產生 HTML 與 Allure 測試結果。

### 測試範圍

| 功能           | 測試內容                                                        |
| -------------- | --------------------------------------------------------------- |
| Login          | Account、Entra ID、Google 登入                                  |
| Project        | Create、Read、Update、Delete                                    |
| Project Member | Create、Read、Update、Delete                                    |
| Application    | Permission Init、SSO Init、S2S Init                             |
| Permission     | Scope、Role、Group、Assign Permission、Default Permission(CRUD) |

## 測試設計

### UUID 測試資料

測試資料會以 `settings.py` 的 prefix 加上 UUID，例如:

```text
project-abbr-a12b
scopy-code-c34d
role-code-e56f
```

### Permission Baseline

Scope、Role、Group、Assign Permission 與 Default Permission 使用固定專案:

```text
project-abbr-main
```

此專案需要具備 Permission Init、固定 Scope、SSO 與 S2S Application。

`keep` 模式會補建缺少的 baseline;`isolated` 模式只檢查，缺少時直接失敗。

建立 baseline 時會使用跨程序鎖，避免多個 pytest process 同時建立相同資料。

## 環境需求

- Python 3.13
- Node.js 與 npm
- Java（產生 Allure 報表時需要）

## 快速開始

### Windows Venv

```powershell
python -m venv venv_dev
.\venv_dev\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
npm ci
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
npm ci
chmod +x shortcut/mac/*.sh
```

## 測試設定

執行前請確認 `config/settings.py`:

- 測試環境 URL
- 登入帳號
- Timeout
- 測試資料 prefix
- Permission baseline 固定資料

請勿將有效的正式環境帳密提交至版本控制。

## 執行測試

```bash
# 全部測試
python -m pytest

# 單一功能
python -m pytest tests/scope

# 單一檔案
python -m pytest tests/scope/test_scope_create.py

# 單一案例
python -m pytest tests/scope/test_scope_create.py::test_scope_create_success

# 顯示瀏覽器
python -m pytest tests/scope --headed
```

預設使用 Chromium，其他共用參數設定於 `pytest.ini`。

## 測試資料模式

| 模式       | 用途                                     | 測試後資料                  |
| ---------- | ---------------------------------------- | --------------------------- |
| `isolated` | CI、重複執行、隔離測試                   | 自動清除 fixture 建立的資料 |
| `keep`     | 人工檢查除錯、建立資料後續運行permission | 保留 fixture 建立的資料     |

### isolated（預設）

```bash
python -m pytest tests/scope --data-mode=isolated
```

- Project、Project Member 與 Application 使用 UUID 專案。
- 測試結束後自動刪除 fixture 建立的資料。
- Permission 功能要求 `project-abbr-main` baseline 已存在。

適合 CI、重複執行與一般隔離測試。

### keep

```bash
python -m pytest tests/application/test_application_s2s_init.py --data-mode=keep
```

- Project 與 Project Member 的 UUID 專案會保留。
- Application 使用或建立 `project-abbr-main`，新增的 UUID Application 會保留。
- Permission 功能會補建缺少的 baseline，UUID 測試資料也會保留。

適合除錯、檢查新增結果或準備共用 baseline。

## 測試報表

每次執行 pytest 會產生:

```text
reports/report.html
reports/allure-results/
```

### Windows

```powershell
# 產生並開啟 Allure HTML 報表
.\shortcut\windows\run_allure.bat

# 開啟已產生的報表
.\shortcut\windows\open_allure.bat
```

### macOS

```bash
# 產生並開啟 Allure HTML 報表
./shortcut/mac/run_allure.sh

# 開啟已產生的報表
./shortcut/mac/open_allure.sh
```

## 程式檢查

```bash
# Lint
python -m ruff check .

# 檢查格式
python -m ruff format --check .

# 自動修正與格式化
python -m ruff check . --fix
python -m ruff format .
```

## 常見狀況

### isolated 執行 Permission 測試時立即失敗

通常代表 `project-abbr-main` 或 Application baseline 不完整。先以 `keep` 模式執行一次 Permission 測試補建資料。

### Permission Init 測試顯示 skipped

Permission Init 是一次性流程。`keep` 模式發現 `project-abbr-main` 已完成初始化時會跳過測試，避免重複初始化。

### 找不到瀏覽器

```bash
python -m playwright install chromium
```

## 專案結構

```text
app/          OmniApp 與 Page Object 整合
config/       測試環境與測試資料設定
pages/        Page Objects 與 Locators
shortcut/     Windows 與 macOS 工具腳本
tests/        Pytest 測試案例與功能 fixtures
utils/        資料模式、baseline 與共用工具
conftest.py   共用 fixtures、CLI 與瀏覽器設定
pytest.ini    Pytest 預設執行參數
```

allure-reports

allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report