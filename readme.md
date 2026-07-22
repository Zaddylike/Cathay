# Omni Autotest

Cathay OmniHub UI 自動化測試框架，使用 Python、Pytest、Playwright 與 Allure。

## 測試範圍

| 功能 | 測試內容 |
| --- | --- |
| Login | Account、Microsoft Entra ID、Google 登入 |
| Project | Create、Read、Update、Delete |
| Project Member | Create、Read、Update、Delete |
| Application | Permission Init、SSO Init、S2S Init |
| Scope | Create、Copy、Read、Update、Delete |
| Role | Create、Copy、Read、Update、Delete |
| Group | Create、Copy、Read、Update、Delete |
| Assign Permission | Create、Read、Update、Delete |
| Default Permission | Create、Read、Update、Delete |

## 測試設計

### 獨立功能測試

Create、Copy、Read、Update、Delete 分別放在獨立測試檔案中。Read、Update、Delete
等案例會透過 fixture 建立自己的前置資料，不依賴其他測試先執行。

測試資料會加入 UUID，例如 `<prefix>a12b`，避免不同案例使用相同名稱。`isolated`
模式下，fixture 會在測試結束後清除自己建立的資料。

### CRUD Journey

每個 `test_*_journey.py` 都是一個完整 E2E journey，在同一個測試案例內依序執行:

```text
Create -> Read -> Update -> Delete
```

Journey 用來驗證完整操作流程;獨立功能測試則用來確認單一功能可以獨立執行與重跑。

### Page Object 與 Fixture

```text
Test
  -> Feature fixture / test data
  -> OmniApp
  -> Page Object
  -> Locator
  -> OmniHub UI
```

- `OmniApp` 集中提供各功能的 Page Object。
- `pages/` 負責頁面操作與驗證。
- `pages/locators/` 集中管理 Locator。
- 根目錄 `conftest.py` 管理瀏覽器、登入、資料模式與 Permission Project。
- 各 `tests/<feature>/conftest.py` 管理該功能的測試資料與 cleanup。

## 環境需求

- Python 3.13
- Node.js 與 npm
- Java,僅產生或開啟 Allure HTML 報表時需要
- Chrome 或 Playwright Chromium

## 安裝

### Windows

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

執行前請檢查 `config/settings.py`:

- `BASE_URL_DEV`:測試環境網址
- `HEADLESS`:是否使用無頭瀏覽器
- `DELAY_TIME`:Playwright 操作延遲
- `DEFAULT_TIMEOUT`:一般操作 timeout
- 登入帳號與密碼
- 測試資料 prefix
- Permission 共用資料

請勿將正式環境或仍有效的帳密提交至版本控制。

## 執行測試

```bash
# 全部測試
python -m pytest

# 單一功能
python -m pytest tests/project
python -m pytest tests/scope

# 單一檔案
python -m pytest tests/project/test_project_update.py

# 單一案例
python -m pytest tests/project/test_project_update.py::test_project_update_success

# 顯示瀏覽器
python -m pytest tests/project --headed
```

預設瀏覽器、輸出報表及其他共用參數定義於 `pytest.ini`。

## 測試資料模式

使用 `--data-mode` 控制 fixture 建立資料後是否清除。預設為 `isolated`。

| 模式 | 適用情境 | 測試資料 |
| --- | --- | --- |
| `isolated` | 一般執行、CI、重跑 | 建立 UUID 資料並在 teardown 清除 |
| `keep` | 人工除錯、保留資料、準備 baseline | 保留測試資料並補建缺少的共用 baseline |

### isolated

```bash
python -m pytest tests/scope --data-mode=isolated
```

- Project、Application 與 Permission 功能使用各案例專屬的 UUID Project。
- Permission Project 會建立最小 Permission Init 前置資料。
- 測試結束後依資源相依順序執行 cleanup。
- 不會修改 `project-abbr-main`。

### keep

```bash
python -m pytest tests/scope --data-mode=keep
```

- fixture 建立的測試資料會保留。
- Permission 與 Application 使用共用專案 `project-abbr-main`。
- 缺少 Permission Init、Scope、SSO 或其他必要 baseline 時會自動補建。
- 建立共用 baseline 時使用跨程序鎖，避免多個 process 同時建立相同資料。

Permission Init 是一次性流程。`keep` 模式發現共用專案已完成初始化時，對應測試會顯示
`skipped`，避免重複初始化。

## 平行執行

框架已依 Pytest worker ID 分配測試帳號，目前設定兩組帳號，因此最多支援兩個 worker。
平行執行前，需先將 `pytest-xdist` 加入專案依賴;目前預設仍為單程序執行。

啟用後可使用:

```bash
python -m pytest -n 2
```

Worker 數量不可超過 `conftest.py` 中設定的帳號數量。

## 測試報表

Pytest 每次執行會輸出:

```text
reports/report.html
reports/allure-results/
```

產生並開啟 Allure HTML 報表:

```powershell
# Windows
.\shortcut\windows\run_allure.bat
```

```bash
# macOS
./shortcut/mac/run_allure.sh
```

只開啟已產生的報表:

```powershell
# Windows
.\shortcut\windows\open_allure.bat
```

```bash
# macOS
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

## 常見問題

### 找不到瀏覽器

```bash
python -m playwright install chromium
```

### Allure CLI not found

```bash
npm ci
```

### Permission Init 顯示 skipped

`keep` 模式使用共用專案。共用專案已完成一次性 Permission Init 時，測試會自動跳過。

### cleanup 失敗

Cleanup 錯誤會附加到 Allure 結果。可使用 `--data-mode=keep` 保留資料並開啟瀏覽器檢查:

```bash
python -m pytest tests/project/test_project_update.py --data-mode=keep --headed
```

## 專案結構

```text
app/             OmniApp,整合所有 Page Object
config/          環境、帳號與測試資料設定
pages/           Page Object
pages/locators/  Locator
shortcut/        Windows 與 macOS 報表、清理腳本
tests/           測試案例與各功能 fixture
utils/           data mode、Permission baseline 等共用工具
conftest.py      共用 fixture、CLI、登入與瀏覽器設定
pytest.ini       Pytest 預設參數與 marker
pyproject.toml   Ruff 設定
```
