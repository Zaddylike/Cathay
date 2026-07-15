from playwright.sync_api import Page, expect
from pages.locators.elements import ProjectMemberElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage
import allure

class ProjectMemberPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ProjectMemberElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)
    #create
    @allure.step("進入專案成員頁面")
    def open_to_member_page(self, project_abbreviation: str):
        expect(self.elements.option_cards.first).to_be_visible()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            project_abbreviation,
            self.elements.msg_search_noResult,
            should_exist=False,
        )
        self.elements.option_cards.first.click()
        self.base_page.click_expect(self.elements.btn_project_edit_member.first, self.elements.btn_member_edit_member)

    @allure.step("進入編輯頁面")
    def go_to_member_edit_page(self):
        self.base_page.click_expect(self.elements.btn_member_edit_member, self.elements.btn_memberadd_add_member)
    
    @allure.step("搜索新增成員")
    def search_member_to_list(self, member_keyword: str):
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.first,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            member_keyword,
        )
        
    @allure.step("調整新增成員權限")
    def adjust_member_level(self):
        self.base_page.click_expect(self.elements.btn_memberadd_add_member_levellist, self.elements.page_members_level_list_select)
        self.elements.option_members_level_list_viewer.click()
        self.elements.btn_memberadd_add_member.click()

    @allure.step("搜尋新增成員")
    def search_member_add(self, member_keyword: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            member_keyword,
            self.elements.btn_filter_clear_noResult,
            should_exist=False,
        )
    
    #read
    @allure.step("搜尋成員")
    def search_members(self, cases: tuple[str, ...]):
        inputElement = self.elements.input_keyword_search
        expectElement = self.elements.option_cards_members
        try:
            for input_value in cases:
                self.operate_page.search_keyword(inputElement, input_value, expectElement)
                inputElement.fill("")
        except Exception as e:
            raise Exception(f"Failed to verify input : {e}")
        
    @allure.step("成員頁面進階搜尋成員權限")
    def filter_project_members_by_role(self):
        expect(self.elements.page_filter_condition).not_to_be_visible()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_memberadd_filter_level_editor.click()
        self.elements.btn_filter_footer_search.click()
        expect(self.elements.option_cards_members).not_to_be_visible()

        expect(self.elements.page_filter_condition).not_to_be_visible()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_memberadd_filter_level_viewer.click()
        self.elements.btn_filter_footer_search.click()
        expect(self.elements.option_cards_members).to_be_visible()

        expect(self.elements.page_filter_condition).not_to_be_visible()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_memberadd_filter_level_owner.click()
        self.elements.btn_filter_footer_search.click()
        expect(self.elements.option_cards_members).to_be_visible()
        
        expect(self.elements.page_filter_condition).not_to_be_visible()
        self.elements.btn_filter_condition_page.click()
        self.elements.btn_filter_footer_clearfilter.click()

    #update
    @allure.step("新增第二個成員")
    def add_another_member(self, member_keyword: str):
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.first,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            member_keyword,
        )
        self.base_page.click_expect(self.elements.btn_memberadd_add_member_levellist, self.elements.page_members_level_list_select)
        self.elements.option_members_level_list_viewer.click()
        self.elements.btn_memberadd_add_member.click()
        
    @allure.step("調整舊成員權限")
    def adjust_previous_member_level(self):
        self.elements.list_editmember_tester3.locator("app-select p-select").click()
        expect(self.elements.page_members_level_list_select).to_be_visible()
        self.elements.option_cards_member_as_editor.click()
        self.operate_page.submit_and_confirm()

    #delete
    @allure.step("刪除成員")
    def delete_member(self):
        self.elements.list_editmember_tester3.locator("app-icon img").click()
        expect(self.elements.list_editmember_tester3).not_to_be_visible()
        self.operate_page.submit_and_confirm()
