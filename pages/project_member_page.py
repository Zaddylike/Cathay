from playwright.sync_api import Page, expect
from pages.elements import Elements
from pages.base_page import BasePage
from pages.operation_page import OperationPage
import allure

class ProjectMemberPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = Elements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperationPage(page)
    #create
    @allure.step("進入編輯成員頁面")
    def open_to_member_page(self):
        expect(self.elements.cards_project).to_be_visible()
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.click()
        self.base_page.click_expect(self.elements.btn_member, self.elements.btn_edit_member)
        self.base_page.click_expect(self.elements.btn_edit_member, self.elements.btn_add_member)

    @allure.step("透過搜尋新增成員")
    def add_member_to_list(self):
        self.elements.btn_filter_add_member_page.click()
        self.elements.input_add_member_search.fill("測試人員3")
        self.elements.checkbox_add_member.click()
        self.elements.btn_add_member_confirm.click()

    # @allure.step("")