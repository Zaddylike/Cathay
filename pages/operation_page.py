from playwright.sync_api import Page, expect
from config.settings import BASE_URL_DEV, DEFAULT_TIMEOUT
from pages.elements import Elements
"""
locator
get_by_placeholder
get_by_role
get_by_text
"""

class OperationPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = Elements(page)

    def verify_delete(self):
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
            self.elements.dialog_btn_checked.click()
        except Exception as e:
            raise  Exception(f'Failed to :{e}')

    def verify_input(self, inputElement, ErrorElement, cases):
        try:
            for input_value, expected_msg in cases:
                inputElement.fill(input_value)

                expect(ErrorElement, f" 輸入 [{input_value}] 後，錯誤訊息應該出現").to_be_visible()
                expect(ErrorElement, f" 輸入 [{input_value}] 後，錯誤訊息應為：{expected_msg}").to_have_text(expected_msg)

                inputElement.fill("")
        except Exception as e:
            raise Exception(f"Failed to verify input : {e}")