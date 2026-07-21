# 非 Login 全套測試錯誤紀錄

- 日期:2026-07-17
- 模式:`isolated`（headless）
- 指令:`.\venv_dev\Scripts\pytest.exe tests --ignore=tests\login --data-mode=isolated -q --tb=short`
- 執行時間:1:18:19
- 結果:44 collected / 37 passed / 3 failed / 4 errors
- 原始輸出:`reports/all_non_login_isolated_20260717.log`

## 異常摘要

| 類別 | 測試 | 階段 | 錯誤摘要 |
| --- | --- | --- | --- |
| Application SSO | `test_application_sso_init.py::test_single_sign_on_init_success` | 測試本體 | `[role="dialog"]` 同時匹配日期選擇器與確認 Dialog，造成 Playwright strict mode violation。 |
| Assign Permission | `test_assign_permission_create.py::test_assign_permission_create_success` | 測試本體 | 等待進階搜尋結果的 member checkbox 30 秒後逾時;找不到 `[role="treeitem"] p-checkbox .p-checkbox-input`。 |
| Assign Permission | `test_assign_permission_crud_flow.py::test_assign_permission_crud_journey` | 測試本體 | 同上，選取 `testuser02` 時找不到 member checkbox。 |
| Assign Permission | `test_assign_permission_delete.py::test_assign_permission_delete_success` | Fixture setup | `created_assign_permission` 建立前置資料時，選取 `testuser02` 的 member checkbox 逾時。 |
| Assign Permission | `test_assign_permission_read.py::test_assign_permission_read_success` | Fixture setup | `created_assign_permission` 建立前置資料時，選取 `testuser02` 的 member checkbox 逾時。 |
| Assign Permission | `test_assign_permission_update.py::test_assign_permission_update_success` | Fixture setup | `created_assign_permission` 建立前置資料時，選取 `testuser02` 的 member checkbox 逾時。 |
| Group | `test_group_read.py::test_group_read_success` | Fixture setup | 登入後使用者 avatar 未出現，頁面仍停在 Auth Login;此案例尚未進入 Group 測試步驟。 |

## 根因群組

1. **SSO Dialog locator 過廣**:日期選擇器與提交確認視窗皆使用 `role="dialog"`。
2. **Assign Permission member 搜尋/locator**:五支測試都卡在同一個 tree item checkbox locator，需確認搜尋結果是否改版、資料不存在，或 selector 已失效。
3. **Group Read 登入異常**:單次登入未成功或導頁未完成，與 Group read 功能本身無直接錯誤證據。

## 通過範圍

- Application:all flow、Permission Init、S2S 通過。
- Default Permission:5/5 通過。
- Group:除 read 外，其餘 5/6 通過。
- Project:5/5 通過。
- Project Member:5/5 通過。
- Role:6/6 通過。
- Scope:6/6 通過。

## 執行備註

- 沒有案例因長時間卡住而被手動中止。
- Pytest 完整跑完全部 44 個案例。
- 本輪僅執行與記錄，未修改測試程式。
