from playwright.sync_api import Page, expect
from pages.locators.elements import ApplicationElements
from pages.base_page import BasePage
from pages.operation_page import OperationPage
import allure

class ApplicationPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ApplicationElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperationPage(page)

    @allure.step("進入專案成員頁面")
    def open_to_member_page(self):
        expect(self.elements.list_projects).to_be_visible()
        self.elements.input_search_project.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
        self.elements.list_projects.click()
        self.base_page.click_expect(self.elements.btn_project_edit_member, self.elements.btn_project_member_edit)
    
    @allure.step("進入身分驗證頁面")
    def open_to_permission_page(self):
        self.base_page.click_expect(self.elements.btn_user_permission, self.elements.tab_permissions_last)
        self.elements.tab_permissions_all.get_by_text(" 權限設定 ").click()
