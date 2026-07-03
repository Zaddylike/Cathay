# Omni Autotest
OmniHub UI 自動化測試專案，使用 Python、Pytest、Playwright 和 Allure。


## 環境準備
1. 啟用虛擬環境 or 自行安裝 Python 套件： 
Windows -> .\venv_dev\Scripts\activate
Mac     -> source .venv/bin/activate

2. 安裝 Python 套件： 
pip install -r requirements.txt

3. 如果要產生 Allure HTML 報表，需安裝 Allure CLI：
npm i allure-commandline


## 環境變數
1. 常用設定：
OMNI_BASE_URL
OMNI_DEFAULT_TIMEOUT
OMNI_HEADLESS
OMNI_ACCOUNT_USERNAME
OMNI_ACCOUNT_PASSWORD
OMNI_ENTRA_USERNAME
OMNI_ENTRA_PASSWORD
OMNI_GOOGLE_USERNAME
OMNI_GOOGLE_PASSWORD

2. `OMNI_HEADLESS=true` 代表不開瀏覽器畫面；`false` 代表顯示瀏覽器。


## 執行測試
1. 執行全部測試： 
python -m pytest

2. 執行單一資料夾：
python -m pytest tests\scope
python -m pytest tests\role
python -m pytest tests\project

3. 執行單一檔案：
python -m pytest tests\scope\test_scope_create.py

4. 執行單一 case：
python -m pytest tests\scope\test_scope_create.py::test_scope_create_success


## 測試報表
測試結果會輸出到：
reports/

產生並開啟 Allure 報表：
.\run_allure.bat

只開啟已產生的 Allure 報表：
.\open_allure.bat


## 專案結構
app/        OmniApp負責整合所有test_與pages之間的互動
config/     測試設定
pages/      Page Object 與 locators
reports/    測試報表輸出
tests/      測試案例
utils/      放置外掛plugings
conftest.py 瀏覽器設定, 測試案例Class可以透過此檔案呼叫OmniApp(非自動登入, 自動登入)
