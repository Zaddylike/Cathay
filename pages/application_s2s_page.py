import allure
from playwright.sync_api import Page, expect

from config.settings import PERMISSION_SCOPE_CODE
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
    def continue_to_scope_step(self):
        """相容 S2S 兩步版與單頁版:有下一步就點擊，否則確認新增範圍可用。"""
        if self.elements.btn_next_step.is_visible():
            self.elements.btn_next_step.click()
            return
        expect(self.elements.btn_s2s_add_scope).to_be_visible()

    @allure.step("進入專案身分驗證頁面")
    def open_to_permission_page(self, project_abbreviation: str):
        self.operate_page.go_to_permission_page(project_abbreviation)
        expect(self.elements.page_permission).to_contain_text(" 身份驗證 ")
    
    @allure.step("進入伺服器串接新增頁面")
    def application_exists(self, application_name: str) -> bool:
        """切換到 S2S 頁籤，使用完整 Application 名稱確認 baseline。"""
        self.elements.tab_s2s.click()
        expect(self.elements.tab_s2s).to_have_attribute("aria-selected", "true")
        self.base_page.wait_loading_disapper()
        return self.page.get_by_text(application_name, exact=True).is_visible()

    @allure.step("若伺服器串接應用端存在則刪除 [{application_name}]")
    def delete_application_if_exists(self, application_name: str) -> bool:
        if not self.application_exists(application_name):
            return False
        return self.operate_page.delete_application_card_if_exists(application_name)

    @allure.step("開啟伺服器串接新增頁面")
    def open_to_create_s2s_page(self):
        self.base_page.click_expect(self.elements.tab_s2s, self.elements.btn_permission_add_s2s)
        self.base_page.click_expect(
            self.elements.btn_permission_add_s2s,
            self.elements.input_s2s_application_name,
        )

    @allure.step("驗證輸入應用端名稱新增資料")
    def input_s2s_application_name(self, application_name: str):
        self.input_s2s_application_name_cases = [
            ("  ", "必填欄位"),
            ("", "必填欄位"),
            ("8" * 41, "輸入字數超過限制長度40"),
        ]
        element_input = self.elements.input_s2s_application_name
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_s2s_application_name_cases)
        self.elements.input_s2s_application_name.fill(application_name)

    @allure.step("設定生效日/到期日")
    def setting_date(self):
        self.base_page.click_expect(self.elements.date_picker_endDate, self.elements.date_picker_panel)
        self.base_page.click_expect(self.elements.dete_picker_arrow_previous, self.elements.date_picker_day.nth(12))
        self.base_page.click_expect(self.elements.date_picker_day.nth(12))
    
    @allure.step("輸入驗證描述欄位")
    def input_application_description(self, description: str):
        self.input_s2s_description_name_cases = [
            ("8" * 201, "輸入字數超過限制長度200"),
        ]
        element_input = self.elements.input_s2s_application_description
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_s2s_description_name_cases)
        element_input.fill(description)

    @allure.step("新增範圍")
    def create_scope(self, scope_code: str = PERMISSION_SCOPE_CODE):
        """新增授權範圍並以完整 Scope code 精準選取既有 Scope。"""
        self.elements.btn_s2s_add_scope.click()
        self.elements.list_s2s_scope.click()
        option = self.elements.option_dropdown_list.filter(has_text=scope_code)
        expect(option).to_have_count(1)
        option.click()
        expect(self.elements.list_s2s_scope).to_contain_text(
            scope_code,
        )

    @allure.step("驗證輸入描述")
    def input_scope_description(self, description: str):
        self.elements.input_s2s_scope_description.fill(description)

    @allure.step("新增送出")
    def submit_s2s_and_verify_success(self):
        self.operate_page.submit_and_confirm(
            confirm_button=self.elements.btn_dialog_permission_confirm,
            enabled_timeout=10000,
        )
