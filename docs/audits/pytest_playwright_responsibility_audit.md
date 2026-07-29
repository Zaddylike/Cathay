# Pytest / Playwright 分工稽核

盤點日期：2026-07-29

## 判定原則

### Pytest 責任

- 收集與執行測試。
- fixture dependency injection。
- setup、yield、teardown 與測試資料生命週期。
- parametrization、marker、skip、xfail。
- 使用 `pytest.raises()` 驗證預期的 Python 例外。

### Playwright 責任

- Browser、Context、Page 與 UI 操作。
- Locator 查找與自動等待。
- 使用 Playwright `expect()` 驗證 UI 最終狀態。
- 保留 Playwright assertion 的 call log、locator、timeout 與實際畫面資訊。

### Python 責任

- 使用普通 `assert` 驗證不依賴 UI 的純資料或演算法結果。
- 使用明確例外表達 framework invariant、設定錯誤或不允許的操作。

> Pytest 沒有另一套 `pytest.assert()`。測試中的普通 `assert` 會由 pytest assertion rewriting 強化錯誤資訊。

## 統計摘要

掃描範圍排除 `.git`、`venv_dev`、`node_modules` 與 `__pycache__`。

| 項目 | 數量 | 判定 |
|---|---:|---|
| 專案 Python 檔案 | 99 | 資訊 |
| Pytest 實際收集測試 | 45 | 已用 `pytest --collect-only` 核對 |
| `@pytest.fixture` | 43 | Pytest 已負責主要組裝工作 |
| 使用 `yield` 的 fixture | 9 | 直接管理 setup/teardown |
| 使用 `return` 的 fixture | 34 | 多數是資料、Page Object 或登記器，並非錯誤 |
| Playwright `expect()` | 84 | 全部位於 `pages/` |
| 測試或 fixture 內的 `expect()` | 0 | 分工良好 |
| 普通 `assert` statement | 0 | 目前沒有純資料 assert |
| `pytest.raises()` | 0 | 目前沒有預期例外測試 |
| 即時 UI probe：`is_visible/is_hidden/count` | 19 | 需依用途逐筆判斷 |
| Page method 廣泛攔截 `Exception` | 27 | 其中 10 個包住 `expect()` |
| 測試接收 cleanup fixture | 17 / 45 | 測試仍知道生命週期細節 |
| 測試手動登記 cleanup | 21 次 | 建議移到 fixture setup |
| 測試直接呼叫原生 Playwright | 3 次 | 全在同一支 schema 測試 |
| `pages/` 外直接操作 `page` / locator | 31 次 | 多數在 fixture setup/teardown |

## 整體判定

### 已經分工正確

1. 84 個 UI assertion 全部使用 Playwright `expect()`。
2. 84 個 `expect()` 全部位於 Page Object 層。
3. 一般 CRUD 測試沒有直接呼叫 locator、`click()`、`fill()` 或 `expect()`。
4. pytest fixture 已負責登入、Project、Permission Init、SSO 與 cleanup registry 的生命週期。
5. `CleanupRegistry` 由 pytest `yield` fixture 在 teardown 統一執行。

### 部分分工，需要調整

1. 17 支測試仍需接收 cleanup fixture，並在測試內容中手動登記 21 次。
2. 10 個 Page Object 方法攔截 Playwright assertion，再改丟一般 `Exception` 或 `AssertionError`。
3. 1 個 UI count 驗證以同步 `count()` 加 `AssertionError` 實作，沒有使用 Playwright retry assertion。
4. 1 個 input value 驗證先讀取值，再以 Python 條件與 `AssertionError` 判斷。
5. 1 支 schema 測試直接呼叫 `page.goto()` 三次。
6. fixtures 與 workflow utilities 有 31 次原生 Page 操作；生命週期決策屬於 pytest，但 UI 操作機制可再收回 Page Object。

## 優先調整清單

## P0：UI assertion 應保留 Playwright 語意

### A01 — Permission Init panel 數量

位置：`utils/permission_baseline.py:100`

目前：

```python
if scope_panels.count() != 1:
    raise AssertionError(...)
```

問題：

- `count()` 是立即查詢。
- UI 尚在 render 時可能提早失敗。
- 錯誤沒有 Playwright locator call log。
- 錯誤訊息又呼叫一次 `count()`。

建議：

```python
expect(scope_panels).to_have_count(1)
```

需要在該檔案匯入 Playwright `expect`。

### A02 — Input value 包含文字

位置：`pages/operate_page.py:57`

目前：

```python
actual_value = inputElement.input_value()
if value not in actual_value:
    raise AssertionError(...)
```

問題：

- 這是 UI value assertion，應由 Playwright 自動等待。
- 目前的 `AssertionError` 隨後又被包成一般 `Exception`。

建議：

```python
expect(input_element).to_have_value(re.compile(rf".*{re.escape(value)}.*"))
```

### A03 — 不要吞掉 Playwright assertion

以下 10 個方法在 `expect()` 外包住 `except Exception`：

| 檔案 | 方法 |
|---|---|
| `pages/application_sso_page.py:147` | `input_oidc_setting` |
| `pages/login_page.py:36` | `user_login_google` |
| `pages/login_page.py:66` | `verify_title` |
| `pages/operate_page.py:15` | `verify_delete` |
| `pages/operate_page.py:39` | `verify_input` |
| `pages/operate_page.py:57` | `verify_input_text` |
| `pages/operate_page.py:72` | `select_list` |
| `pages/operate_page.py:86` | `select_list_by_text` |
| `pages/operate_page.py:99` | `submit_and_confirm` |
| `pages/operate_page.py:116` | `search_keyword` |

問題：

- Playwright `AssertionError`、timeout 與操作錯誤被轉成一般 `Exception`。
- 測試報告較難判斷是 selector、timeout、assertion 或程式錯誤。
- Allure 已有 `@allure.step` 提供業務情境，多數方法不需要再包一次。

建議原則：

```python
@allure.step("搜尋關鍵字並驗證結果")
def search_keyword(...):
    search_input.fill(keyword)
    ...
    expect(result_locator).to_be_visible()
```

若一定要補充 domain context，只捕捉明確例外並保留 cause：

```python
except PlaywrightError as error:
    raise ScopeOperationError(...) from error
```

不要使用沒有區分錯誤類型的 `except Exception`。

### A04 — Cleanup 失敗目前不會使測試失敗

位置：`utils/resource_cleanup.py:33`

目前 `CleanupRegistry.cleanup()`：

1. 捕捉每一個 cleanup exception。
2. 附加到 Allure。
3. 不重新拋出或彙總錯誤。

結果是測試可能顯示成功，但測試資料仍殘留。

建議：

1. 繼續執行所有 cleanup actions。
2. 收集全部 cleanup errors。
3. 全部執行後拋出一個彙總 teardown error。

這是 pytest 生命週期責任，應由 `cleanup_registry` fixture teardown 呈現失敗。

## P1：測試不應手動管理 cleanup 登記

17 支測試接收 cleanup fixture，共手動登記 21 次。

### Scope

- `tests/scope/test_scope_create.py:6`
- `tests/scope/test_scope_copy.py:6`
- `tests/scope/test_scope_journey.py:6`

### Role

- `tests/role/test_role_create.py:6`
- `tests/role/test_role_copy.py:6`
- `tests/role/test_role_journey.py:7`

### Group

- `tests/group/test_group_create.py:6`
- `tests/group/test_group_copy.py:6`
- `tests/group/test_group_update.py:6`
- `tests/group/test_group_journey.py:6`

### Project

- `tests/project/test_project_create.py:6`
- `tests/project/test_project_journey.py:6`

### Assign Permission

- `tests/assign_permission/test_assign_permission_create.py:6`
- `tests/assign_permission/test_assign_permission_journey.py:6`

### Default Permission

- `tests/default_permission/test_default_permission_create.py:6`
- `tests/default_permission/test_default_permission_update.py:6`
- `tests/default_permission/test_default_permission_journey.py:6`

目前的 `CleanupRegistry` teardown 已由 pytest 管理，方向正確；跨界點是測試仍要執行：

```python
scope_cleanup(scope_data.code)
```

建議讓 case fixture 在 setup 階段自動登記：

```python
@pytest.fixture
def scope_create_case(scope_data, scope_cleanup):
    scope_cleanup(scope_data.code)
    return scope_data
```

測試改成：

```python
def test_scope_create_success(permission_settings_app, scope_create_case):
    data = scope_create_case
    ...
```

如此：

- pytest fixture 決定何時登記與何時清理。
- 測試只描述 Scope Create 行為。
- Page Object 繼續執行實際 UI 刪除操作。

Journey 或 Delete 測試中的 `delete_scope()` 是被測行為，不是 teardown，不應為了分工而移除。

## P1：測試直接操作原生 Page

只有一支測試直接呼叫 Playwright Page：

| 位置 | 呼叫 |
|---|---|
| `tests/verify_fields/test_schema_input_validation.py:371` | `app.page.goto(...)` |
| `tests/verify_fields/test_schema_input_validation.py:408` | `app.page.goto(...)` |
| `tests/verify_fields/test_schema_input_validation.py:483` | `app.page.goto(...)` |

建議統一改走既有：

```python
app.operate_page.reset_to_anchor(BASE_URL_DEV)
```

或使用語意更明確的 workflow/navigation method。

## P2：fixtures 直接操作 Page

`pages/` 外共有 31 次原生 Page 或 locator 操作：

| 檔案 | 次數 |
|---|---:|
| `conftest.py` | 2 |
| `tests/application/conftest.py` | 9 |
| `tests/assign_permission/conftest.py` | 2 |
| `tests/default_permission/conftest.py` | 2 |
| `tests/group/conftest.py` | 1 |
| `tests/role/conftest.py` | 2 |
| `tests/scope/conftest.py` | 1 |
| `tests/verify_fields/test_schema_input_validation.py` | 7 |
| `utils/permission_baseline.py` | 5 |

這不代表 pytest 不能呼叫 Playwright。正確切法是：

- fixture 決定「現在要回首頁、建立資料、登記清理」。
- Page Object 或 navigation helper 執行「如何按 Escape、如何 goto、如何等待頁面穩定」。

優先把重複的：

```python
page.keyboard.press("Escape")
page.goto(BASE_URL_DEV)
```

收斂到：

```python
operate_page.reset_to_anchor(BASE_URL_DEV)
```

## P2：即時 UI probes

專案共有 19 次：

- `is_visible()`
- `is_hidden()`
- `count()`

不是全部都需要改成 `expect()`。

### 可以保留的用途

- `*_exists()` 回傳布林值，供 fixture 決定是否建立資料。
- `delete_*_if_exists()` 判斷是否需要刪除。
- 頁面有兩種合法結構，依目前可見元件選擇不同操作。

### 應改成 `expect()` 的用途

- 測試或 workflow 要求 UI 最終必須達成某個狀態。
- count、visible、hidden 的結果直接決定 pass/fail。
- 頁面 render 有延遲，立即 probe 可能造成 race condition。

目前已確認需要調整的是：

- `utils/permission_baseline.py:100`

其餘 18 次先依「探測」或「斷言」逐筆確認，不建議機械式全部替換。

## 建議調整順序

1. A01：將 Permission Init panel count 改為 `expect().to_have_count()`。
2. A02：將 input value Python 判斷改為 `expect().to_have_value()`。
3. A03：移除 10 個包住 `expect()` 的 broad exception wrappers。
4. A04：讓 cleanup registry 彙總後回報 teardown failure。
5. 先以 Scope Create 移除測試本體的 cleanup 登記。
6. 依序套用 Scope → Role → Group → Project → Assign → Default Permission。
7. 收斂 schema 測試與 fixtures 的直接 `page.goto()`。
8. 最後逐筆審查剩餘 18 個 UI probes。

## Scope Create 目前狀態

### 正確

- 測試沒有直接使用 locator。
- 測試沒有直接使用普通 `assert` 驗證 UI。
- UI 驗證在 `pages/scope_page.py` 使用 Playwright `expect()`。
- cleanup 最終由 pytest `cleanup_registry` teardown 執行。

### 待調整

- `tests/scope/test_scope_create.py:11` 手動呼叫 `scope_cleanup(scope_data.code)`。
- `tests/scope/conftest.py:21` fixture 直接操作 `page.keyboard.press("Escape")`。
- `pages/scope_page.py` 的 UI assertions 本身分工正確，暫時不用搬動。

Scope Create 適合作為第一個調整樣板，因為只需要先處理 cleanup 登記責任，不必重寫測試 assertion。

## 驗證方式

統計核對命令：

```powershell
.\venv_dev\Scripts\python.exe -m pytest --collect-only -q --video=off
```

結果：

```text
45 tests collected
```
