from playwright.sync_api import Page, expect
from config.settings import BASE_URL_DEV, DEFAULT_TIMEOUT
from pages.locators.elements import OperationElements
import re
"""
locator
get_by_placeholder
get_by_role
get_by_text
"""

class OperationPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = OperationElements(page)

    def verify_delete(self):
        # Delete 完整流程(反向)
        try:
            input_cases = [
                "delete",
                "   ",
                "Delete"
            ]
            input_element  = self.elements.dialog_input_delete

            for input_value in input_cases:
                input_element.fill(input_value)
                expect(self.elements.dialog_btn_confirm).to_be_disabled()
                input_element.clear()
            
            input_element.fill("DELETE")
            self.elements.dialog_btn_confirm.click()
            self.elements.btn_dialog_checked.click()
        except Exception as e:
            raise  Exception(f'Failed to :{e}')

    def verify_input(self, inputElement, ErrorElement, cases):
        # 欄位內容輸入驗證
        try:
            for input_value, expected_msg in cases:
                inputElement.fill(input_value)

                expect(ErrorElement, f" 輸入 [{input_value}] 後，錯誤訊息應該出現").to_be_visible()
                expect(ErrorElement, f" 輸入 [{input_value}] 後，錯誤訊息應為：{expected_msg}").to_have_text(expected_msg)

                inputElement.fill("")
        except Exception as e:
            raise Exception(f"Failed to verify input : {e}")

    def verify_input_text(self,inputElement, value):
        # 驗證input類型欄位內容預期
        try:
            expect(inputElement).to_have_value(
                re.compile(rf".*{re.escape(value)}.*")
            )
        except Exception as e :
            raise Exception(f"Failed to verify input value contains : {e}")
    
    def select_list(self, listElement, optionElement, optionIndex, optionValue=None):
        # 驗證下拉選單選項
        try:
            listElement.click()
            expect(optionElement.nth(optionIndex)).to_be_visible()
            optionElement.nth(optionIndex).click()
            if optionValue:
                expect(listElement).to_have_text(optionValue)
        except Exception as e:
            raise Exception(f"Failed to select list : {e}")