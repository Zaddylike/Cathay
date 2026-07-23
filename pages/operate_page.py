import allure
from playwright.sync_api import Page, expect
from pages.locators.elements import OperationElements
from pages.base_page import BasePage
import re
from config.settings import PERMISSION_PROJECT_ABBR

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
                expect(ErrorElement, f" 輸入 [{input_value}] 後，錯誤訊息應為:{expected_msg}").to_have_text(expected_msg)

                inputElement.fill("")
        except Exception as e:
            raise Exception(f"Failed to verify input : {e}")

    @allure.step("驗證input類型欄位是否預期")
    def verify_input_text(self, inputElement, value):
        # 驗證input類型欄位內容預期
        try:
            expect(inputElement).to_be_visible()

            actual_value = inputElement.input_value()

            if value not in actual_value:
                raise AssertionError(
                    f"Expected input value to contain '{value}', but got '{actual_value}'"
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

    @allure.step("選擇清單選項 [{option_text}]")
    def select_list_by_text(self, list_element, option_element, option_text: str):
        try:
            list_element.click()
            option = option_element.filter(has_text=option_text).first
            expect(option).to_be_visible()
            option.click()
        except Exception as e:
            raise Exception(f"Failed to select list option [{option_text}]: {e}")

    @allure.step("送出表單並確認視窗")
    def submit_and_confirm(self, submit_button=None, dialog=None, confirm_button=None, enabled_timeout=None):
        try:
            submit_button = self.elements.btn_submit if submit_button is None else submit_button
            dialog = self.elements.page_dialog if dialog is None else dialog
            confirm_button = self.elements.btn_dialog_checked if confirm_button is None else confirm_button

            if enabled_timeout is None:
                expect(submit_button).to_be_enabled()
            else:
                expect(submit_button).to_be_enabled(timeout=enabled_timeout)
            self.base_page.click_expect(submit_button, dialog)
            self.base_page.click_expect(confirm_button)
            
        except Exception as e:
            raise Exception(f"Failed to submit and confirm: {e}")

    @allure.step("搜尋關鍵字並驗證結果")
    def search_keyword(self, search_input, keyword, result_locator=None, should_exist=True):
        try:
            result_locator = self.elements.option_cards.first if result_locator is None else result_locator
            search_input.fill(keyword)
            self.base_page.wait_loading_disapper()
            if should_exist:
                expect(result_locator).to_be_visible()
            else:
                expect(result_locator).not_to_be_visible()
        except Exception as e:
            raise Exception(f"Failed to search keyword [{keyword}]: {e}")

    @allure.step("開啟卡片操作選單")
    def open_card_action(self, search_input, keyword, menu_button, menu_page, action_button, action_reclick=False):
        try:
            search_input.fill(keyword)
            self.page.mouse.wheel(0, 500)
            self.base_page.sleep(1)
            self.base_page.click_expect(menu_button.last, menu_page)
            self.base_page.click_expect(action_button, reclick=action_reclick)
            self.base_page.sleep(1)
        except Exception as e:
            raise Exception(f"Failed to open card action for [{keyword}]: {e}")

    @allure.step("若應用端存在則刪除 [{application_name}]")
    def delete_application_card_if_exists(self, application_name: str) -> bool:
        search_input = self.elements.input_keyword_search_id
        search_input.fill(application_name)
        self.base_page.wait_loading_disapper()

        application_card = self.elements.option_cards.filter(
            has=self.page.get_by_text(application_name, exact=True)
        )
        if application_card.count() == 0:
            search_input.fill("")
            return False

        expect(application_card).to_have_count(1)
        menu_button = application_card.locator(".p-splitbutton-dropdown")
        expect(menu_button).to_have_count(1)
        self.base_page.click_expect(
            menu_button,
            self.elements.page_card_threepoint_menu,
        )
        self.base_page.click_expect(
            self.elements.btn_card_menu_delete,
            self.elements.page_dialog,
        )
        self.verify_delete()
        self.base_page.wait_loading_disapper()
        expect(application_card).to_have_count(0)
        search_input.fill("")
        return True

    @allure.step("從進階搜尋選擇成員")
    def select_member_from_advanced_search(
        self,
        search_button,
        search_input,
        checkbox,
        confirm_button,
        keyword,
    ):
        try:
            search_button.click()
            search_input.fill(keyword)
            checkbox.click()
            confirm_button.click()
        except Exception as e:
            raise Exception(f"Failed to select member [{keyword}]: {e}")

    @allure.step("開啟專案權限頁面")
    def go_to_permission_page(
        self,
        project_abbreviation: str = PERMISSION_PROJECT_ABBR,
    ):
        self.elements.input_keyword_search.fill(project_abbreviation)
        self.base_page.wait_loading_disapper()
        expect(self.elements.msg_search_noResult).not_to_be_visible()
        project_card = self.elements.option_cards.filter(
            has=self.page.get_by_text(project_abbreviation, exact=True)
        )
        expect(project_card).to_have_count(1)
        project_card.click()
        self.elements.btn_project_info_permission.click()
        expect(self.elements.page_permission).to_be_visible()
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")

    @allure.step("進入權限設定頁面")
    def open_to_permissions_page(self):
        self.base_page.click_expect(self.elements.tab_permission)
        expect(self.elements.tab_permission).to_have_attribute("aria-selected", "true")

    @allure.step("點擊下一步")    
    def click_to_next_step(self):
        self.elements.btn_next_step.click()
