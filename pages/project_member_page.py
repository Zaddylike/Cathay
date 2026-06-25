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
    @allure.step("進入專案成員頁面")
    def open_to_member_page(self):
        expect(self.elements.cards_project).to_be_visible()
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.click()
        self.base_page.click_expect(self.elements.btn_member, self.elements.btn_edit_member)

    @allure.step("進入編輯頁面")
    def go_to_member_edit_page(self):
        self.base_page.click_expect(self.elements.btn_edit_member, self.elements.btn_add_member)
    
    @allure.step("搜索新增成員")
    def search_member_to_list(self):
        self.elements.btn_member_add_filter_page.click()
        self.elements.input_add_member_search.fill("測試人員3")
        self.elements.checkbox_add_member.click()
        self.elements.btn_memberadd_filter_page_confirm.click()
        
    @allure.step("調整新增成員權限")
    def adjust_member_level(self):
        self.base_page.click_expect(self.elements.btn_editmember_levellist, self.elements.list_member_level)
        self.elements.list_member_level_viewer.click()
        self.elements.btn_editmember_addmember.click()
    
    @allure.step("搜尋新增成員")
    def search_member_add(self):
        self.elements.btn_submit.click()
        self.elements.dialog_btn_checked.click()
        self.elements.input_member_search.fill("測試人員3")
        expect(self.elements.btn_clear_nodata).not_to_be_visible()
    
    #read
    @allure.step("搜尋成員")
    def search_members(self):
        cases = [
            "testuser01","OmniHub","數位數據","omnitest3"
        ]
        inputElement = self.elements.input_search_field
        expectElement = self.elements.list_project_member
        try:
            for input_value in cases:
                inputElement.fill(input_value)
                expect(expectElement).to_be_visible()
                inputElement.fill("")
        except Exception as e:
            raise Exception(f"Failed to verify input : {e}")
        
        self.elements.btn_clear_search.click()
    
    @allure.step("成員頁面進階搜尋成員權限")
    def filter_project_members_by_role(self):
        self.elements.btn_filter_page.click()
        expect(self.elements.dialog_page_filter).to_be_visible()
        self.elements.btn_filter_level_editor.click()
        self.elements.btn_filter_search.click()
        expect(self.elements.list_project_member).not_to_be_visible()

        self.elements.btn_filter_page.click()
        expect(self.elements.dialog_page_filter).to_be_visible()
        self.elements.btn_filter_level_viewer.click()
        self.elements.btn_filter_search.click()
        expect(self.elements.list_project_member).not_to_be_visible()

        self.elements.btn_filter_page.click()
        expect(self.elements.dialog_page_filter).to_be_visible()
        self.elements.btn_filter_level_owner.click()
        self.elements.btn_filter_search.click()
        expect(self.elements.list_project_member).to_be_visible()
        
        self.elements.btn_filter_page.click()
        self.elements.btn_filter_clean_filter.click()

    #update
    @allure.step("新增第二個成員")
    def add_another_member(self):
        self.elements.btn_member_add_filter_page.click()
        self.elements.input_add_member_search.fill("測試人員2")
        self.elements.checkbox_add_member.click()
        self.elements.btn_memberadd_filter_page_confirm.click()
        self.base_page.click_expect(self.elements.btn_editmember_levellist, self.elements.list_member_level)
        self.elements.list_member_level_viewer.click()
        self.elements.btn_editmember_addmember.click()
        
    @allure.step("調整舊成員權限")
    def adjust_previous_member_level(self):
        self.elements.list_editmember_tester3.locator("app-select p-select").click()
        expect(self.elements.list_member_level).to_be_visible()
        self.elements.list_member_level_editor.click()
        self.elements.btn_submit.click()
        self.elements.dialog_btn_checked.click()

    #delete
    @allure.step("刪除成員")
    def delete_member(self):
        self.elements.list_editmember_tester3.locator("app-icon img").click()
        expect(self.elements.list_editmember_tester3).not_to_be_visible()
        self.elements.btn_submit.click()
        self.elements.dialog_btn_checked.click()