import allure
from playwright.sync_api import Page, expect
from config.settings import BASE_URL_DEV, DEFAULT_TIMEOUT
from pages.locators.elements import OperationElements
from pages.base_page import BasePage
import re

class OperatePage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = OperationElements(page)
        self.base_page = BasePage(page)

    @allure.step("驗證刪除視窗輸入")
    def verify_delete(self):
        # 驗證刪除視窗輸入
        try:
            input_cases = [
                "delete",
                "   ",
                "ＤＥＬＥＴＥ"
            ]
            input_element  = self.elements.dialog_input_delete

            for input_value in input_cases:
                self.base_page.wait_fill(input_element, input_value)
                expect(self.elements.btn_dialog_delete_confirm).to_be_disabled()
                input_element.clear()
            
            input_element.fill("DELETE")
            self.elements.btn_dialog_delete_confirm.click()
            self.elements.btn_dialog_checked.click()
        except Exception as e:
            raise  Exception(f'Failed to :{e}')

    @allure.step("驗證欄位輸入規範")
    def verify_input(self, inputElement, ErrorElement, cases):
        # 欄位輸入規範驗證
        ErrorElement = self.elements.msg_field_error if ErrorElement is None else ErrorElement
        try:
            for input_value, expected_msg in cases:
                inputElement.fill(input_value)

                expect(ErrorElement, f" 輸入 [{input_value}] 後，錯誤訊息應該出現").to_be_visible()
                expect(ErrorElement, f" 輸入 [{input_value}] 後，錯誤訊息應為：{expected_msg}").to_have_text(expected_msg)

                inputElement.fill("")
        except Exception as e:
            raise Exception(f"Failed to verify input : {e}")

    @allure.step("驗證input類型欄位是否預期")
    def verify_input_text(self, inputElement, value):
        # 驗證input類型欄位內容預期
        try:
            expect(inputElement).to_have_value(
                re.compile(rf".*{re.escape(value)}.*")
            )
        except Exception as e :
            raise Exception(f"Failed to verify input value contains : {e}")
    
    @allure.step("點擊下拉清單")
    def select_list(self, listElement, optionElement, optionIndex, optionValue=None):
        # 點擊下拉選單選項
        try:
            listElement.click()
            expect(optionElement.nth(optionIndex)).to_be_visible()
            optionElement.nth(optionIndex).click()
            if optionValue:
                expect(listElement).to_have_value(
                re.compile(rf".*{re.escape(optionValue)}.*")
            )
        except Exception as e:
            raise Exception(f"Failed to select list : {e}")

    @allure.step("進入專案身分驗證頁面")
    def go_to_permission_page(self):
        expect(self.elements.option_cards.first).to_be_visible()
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
        self.elements.option_cards.first.click()
        self.elements.btn_project_info_permission.click()
        expect(self.elements.page_permission).to_be_visible()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")

    @allure.step("進入權限設定頁面")
    def open_to_permissions_page(self):
        self.base_page.click_expect(self.elements.tab_permission)
        expect(self.elements.tab_permission).to_have_attribute("aria-selected", "true")

    
