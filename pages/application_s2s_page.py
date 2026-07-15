import allure
from playwright.sync_api import Page, expect

from config.settings import PROJECT_ABBR
from pages.base_page import BasePage
from pages.locators.elements import ApplicationS2sElements
from pages.operate_page import OperatePage


class ApplicationServerToServerPage:
    def __init__(self, page: Page):
            self.page = page
            self.elements = ApplicationS2sElements(page)
            self.base_page = BasePage(page)
            self.operate_page = OperatePage(page)
    
    @allure.step("點擊下一步")    
    def click_to_next_step(self):
        self.elements.btn_next_step.click()

    @allure.step("進入專案身分驗證頁面")
    def open_to_permission_page(self):
        expect(self.elements.option_cards.first).to_be_visible()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            PROJECT_ABBR,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.option_cards.first.click()
        self.base_page.click_expect(self.elements.btn_project_info_permission, self.elements.page_permission)
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
    
    @allure.step("進入伺服器串接新增頁面")
    def open_to_create_s2s_page(self):
        self.base_page.click_expect(self.elements.tab_s2s, self.elements.btn_permission_add_s2s)
        self.base_page.click_expect(self.elements.btn_permission_add_s2s, self.elements.btn_next_step)

    @allure.step("驗證輸入應用端名稱新增資料")
    def input_s2s_application_name(self):
        self.input_s2s_application_name_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 41, "輸入字數超過限制長度40"),
        ]
        element_input = self.elements.input_s2s_application_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_s2s_application_name_cases)
        self.elements.input_s2s_application_name.fill("e2e-testing-s2s-name")

    @allure.step("設定生效日/到期日")
    def setting_date(self):
        self.base_page.click_expect(self.elements.date_picker_endDate, self.elements.date_picker_panel)
        self.base_page.click_expect(self.elements.dete_picker_arrow_previous, self.elements.date_picker_day.nth(12))
        self.base_page.click_expect(self.elements.date_picker_day.nth(12))
    
    @allure.step("輸入驗證描述欄位")
    def input_application_description(self):
        self.input_s2s_description_name_cases = [
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_s2s_application_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_s2s_description_name_cases)
        self.elements.input_s2s_application_description.fill("e2e-testing-s2s-description")

    @allure.step("新增範圍")
    def create_scope(self):
        self.elements.btn_s2s_add_scope.click()
        self.operate_page.select_list(self.elements.list_s2s_scope, self.elements.option_dropdown_list, 0)

    @allure.step("驗證輸入描述")
    def input_scope_description(self):
        self.elements.input_s2s_application_description.fill("e2e-s2s-scope-des")

    @allure.step("新增送出")
    def submit_s2s_and_verify_success(self):
        self.operate_page.submit_and_confirm(
            confirm_button=self.elements.btn_dialog_permission_confirm,
            enabled_timeout=10000,
        )

