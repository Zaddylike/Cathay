# Omni Autotest

OmniHub UI 自動化測試專案，使用 Python、Pytest、Playwright 與 Allure。

## 環境準備

### Windows

```powershell
python -m venv venv_dev
.\venv_dev\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install
npm ci
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install
npm ci
chmod +x shortcut/mac/*.sh
```

## 環境變數

常用設定：

```text
OMNI_BASE_URL
OMNI_DEFAULT_TIMEOUT
OMNI_HEADLESS
OMNI_ACCOUNT_USERNAME
OMNI_ACCOUNT_PASSWORD
OMNI_ENTRA_USERNAME
OMNI_ENTRA_PASSWORD
OMNI_GOOGLE_USERNAME
OMNI_GOOGLE_PASSWORD
```

`OMNI_HEADLESS=true` 代表不顯示瀏覽器；`false` 代表顯示瀏覽器。

## 執行測試

```powershell
# 全部測試
python -m pytest

# 單一資料夾
python -m pytest tests\scope

# 單一檔案
python -m pytest tests\scope\test_scope_create.py

# 單一案例
python -m pytest tests\scope\test_scope_create.py::test_scope_create_success
```

macOS 請將路徑分隔符號改為 `/`，例如 `python -m pytest tests/scope`。

## 測試報表

Pytest 產生的結果位於 `reports/`。

Windows：

```powershell
# 產生並開啟 Allure 報表
.\shortcut\windows\run_allure.bat

# 只開啟既有 Allure 報表
.\shortcut\windows\open_allure.bat
```

macOS：

```bash
# 產生並開啟 Allure 報表
./shortcut/mac/run_allure.sh

# 只開啟既有 Allure 報表
./shortcut/mac/open_allure.sh
```

## Lint 與 Format

安裝開發工具：

```bash
python -m pip install -r requirements-dev.txt
```

執行檢查：

```bash
python -m ruff check .
python -m ruff format --check .
```

自動修正與格式化：

```bash
python -m ruff check . --fix
python -m ruff format .
```

## 專案結構

```text
app/          OmniApp 與頁面物件整合
config/       測試與環境設定
pages/        Page Objects 與 locators
reports/      測試結果與 Allure 報表
shortcut/     Windows 與 macOS 工具腳本
tests/        Pytest 測試案例
utils/        共用工具
conftest.py   共用 Pytest fixtures 與瀏覽器設定
```
