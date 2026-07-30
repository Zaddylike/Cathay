# Omni Autotest

OmniHub UI 自動化測試框架，使用 Python、Pytest、pytest-playwright、Playwright
與 Allure。

目前涵蓋 Login、Project、Project Member、Application、Scope、Role、Group、
Assign Permission 與 Default Permission，包括 CRUD、Copy、Journey 與欄位驗證。

## 快速開始

### 1. 安裝

Windows：

```powershell
python -m venv venv_dev
.\venv_dev\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
npm ci
```

macOS：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
npm ci
chmod +x shortcut/mac/*.sh
```

`npm ci` 安裝 Allure CLI。產生 Allure HTML 時還需要 Java。

### 2. 設定

執行前檢查 `config/settings.py`：

- `BASE_URL_DEV`：測試環境網址。
- `ACCOUNT_USERNAME*` / `ACCOUNT_PASSWORD*`：測試帳號。
- `HEADLESS`：是否使用無頭瀏覽器。
- `DELAY_TIME`：Playwright 操作延遲。
- `DEFAULT_TIMEOUT` / `LOGIN_TIMEOUT`：一般操作與登入 timeout。
- 各功能 prefix 與 `PERMISSION_*`：測試資料及共用 baseline。

只使用測試環境帳號，不要提交正式環境或個人帳號憑證。

### 3. 執行

```powershell
# 全部測試
python -m pytest

# 單一功能
python -m pytest tests/scope

# 單一檔案
python -m pytest tests/scope/test_scope_create.py

# 單一案例
python -m pytest tests/scope/test_scope_create.py::test_scope_create_success

# 顯示瀏覽器
python -m pytest tests/scope/test_scope_create.py --headed
```

預設使用 Chromium，並產生錄影、HTML report 與 Allure results。共用參數位於
`pytest.ini`。

## 框架分工

```text
Test
  -> Feature fixture / Test data
  -> OmniApp
  -> Page Object
  -> Locator
  -> OmniHub UI
```

| 位置 | 責任 |
|---|---|
| `tests/test_*.py` | 描述測試情境 |
| `tests/<feature>/conftest.py` | 功能前置資料與 cleanup 登記 |
| 根目錄 `conftest.py` | Browser、登入、data mode、Permission lifecycle |
| `app/omni_app.py` | 組裝並提供 Page Object |
| `pages/` | UI 操作、流程與 Playwright assertion |
| `pages/locators/` | Locator 定義 |
| `data/factories/` | UUID 測試資料 |
| `data/schema/` | 欄位驗證案例 |
| `utils/` | Cleanup、data mode、Permission baseline |

### Pytest 與 Playwright

- Pytest 管理 fixture、setup、yield、teardown 與測試收集。
- Playwright 管理 Browser、Page、Locator、UI 操作與等待。
- UI 結果使用 Playwright `expect()`。
- 普通 Python `assert` 只用於不依賴 UI 的程式邏輯。
- Test 不直接操作 locator；操作細節放在 Page Object。

## 測試生命週期

一般 Permission 測試：

```text
建立 Browser / Context / Page
  -> 登入
  -> 準備 Permission Project
  -> 完成 Permission Init
  -> 建立功能前置資料
  -> 執行測試
  -> 反向清除測試資料
  -> 清除 baseline
  -> 刪除 isolated Project
```

### Permission fixtures

| Fixture | 提供的狀態 |
|---|---|
| `permission_project_context` | 已登入並取得 Permission Project |
| `permission_initialized_context` | 已完成 Permission Init |
| `permission_settings_app` | 已進入 Permission 設定頁 |
| `permission_sso_context` | 已建立 SSO 前置 |
| `permission_sso_app` | 已建立 SSO 並進入 Permission 設定頁 |

Scope、Role、Default Permission 通常使用 `permission_settings_app`；Group、Assign
Permission 使用 `permission_sso_app`。

### Data mode

預設為 `isolated`：

| 模式 | 用途 | 測試後 |
|---|---|---|
| `isolated` | 一般執行、CI、重跑 | 清除 UUID 資料與臨時 Project |
| `keep` | 人工除錯、保留資料 | 保留測試資料 |

```powershell
python -m pytest tests/role --data-mode=isolated
python -m pytest tests/role --data-mode=keep --headed
```

- `isolated` 使用測試專屬 Project，不修改 `project-abbr-main`。
- `keep` 使用共用 Project，缺少 baseline 時自動補建。
- 共用 baseline 使用跨程序 lock，避免同時重複建立。

## 測試設計

- CRUD 功能分開測試，可單獨執行與重跑。
- Read、Update、Delete 透過 fixture 建立自己的前置資料。
- `test_*_journey.py` 在同一案例驗證 `Create -> Read -> Update -> Delete`。
- `test_*_validation.py` 驗證必填、格式、長度與重複資料。
- 測試資料由 factory 加入 UUID，避免重跑或平行執行時撞名。

## 新增測試

1. 在 `data/factories/` 增加測試資料。
2. 在 `pages/locators/` 增加 locator。
3. 在 `pages/` 增加 UI 操作與 `expect()`。
4. 在功能 `conftest.py` 建立前置資料並登記 cleanup。
5. 在 `tests/<feature>/` 撰寫測試。
6. 單跑案例，確認 teardown 沒有殘留資料。
7. 執行 Ruff 與該功能目錄測試。

## 報表與錄影

預設輸出：

```text
reports/report.html
reports/allure-results/
reports/playwright/
```

單次調整錄影模式：

```powershell
python -m pytest --video=on
python -m pytest --video=retain-on-failure
python -m pytest --video=off
```

產生並開啟 Allure：

```powershell
.\shortcut\windows\run_allure.bat
```

```bash
./shortcut/mac/run_allure.sh
```

影片可能包含帳號與頁面資料，不要提交或公開 `reports/`。

## 程式檢查

```powershell
python -m ruff check .
python -m ruff format --check .
```

需要自動修正時：

```powershell
python -m ruff check . --fix
python -m ruff format .
```

## 專案結構

```text
app/             OmniApp 與 Page Object 組裝
config/          環境、帳號與 timeout
data/            測試資料 factory 與 schema
pages/           Page Object
pages/locators/  Locator
tests/           測試案例與功能 fixtures
utils/           lifecycle、cleanup、Permission baseline
shortcut/        報表與清理指令
conftest.py      共用 pytest fixtures
pytest.ini       Pytest 預設參數
pyproject.toml   Ruff 設定
```

## 常見問題

### 找不到 Chromium

```powershell
python -m playwright install chromium
```

### 找不到 Allure

執行 `npm ci`，並確認電腦已安裝 Java。

### 測試資料沒有清除

1. 確認沒有使用 `--data-mode=keep`。
2. 查看 Allure teardown 與 `cleanup failed` 附件。
3. 使用 `--headed --data-mode=keep` 重跑並人工檢查。

### Permission Init 被 skipped

`keep` 模式的共用 Project 若已完成一次性 Permission Init，初始化測試會跳過，
避免重複建立。

## 交接檢查

- 測試環境 URL 與測試帳號仍有效。
- `python -m pytest --collect-only` 能成功收集案例。
- Login、Project Journey 與 Permission Journey 可以單獨通過。
- `isolated` 執行後沒有殘留 UUID 資料。
- HTML、Allure 與 Playwright 錄影可正常產生。
- 新增設定或 marker 時同步更新 `pytest.ini` 與本文件。
