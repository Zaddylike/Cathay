from playwright.sync_api import Page, expect
from pages.locators.elements import ProjectMemberElements
from pages.base_page import BasePage
from pages.operation_page import OperationPage
import allure

class ProjectMemberPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ProjectMemberElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperationPage(page)
    #create
    @allure.step("進入專案成員頁面")
    def open_to_member_page(self):
        expect(self.elements.list_projects).to_be_visible()
        self.elements.input_search_project.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
        self.elements.list_projects.click()
        self.base_page.click_expect(self.elements.btn_project_edit_member, self.elements.btn_project_member_edit)

    @allure.step("進入編輯頁面")
    def go_to_member_edit_page(self):
        self.base_page.click_expect(self.elements.btn_project_member_edit, self.elements.btn_project_member_add)
    
    @allure.step("搜索新增成員")
    def search_member_to_list(self):
        self.elements.btn_project_member_add_filter.click()
        self.elements.input_add_member_search.fill("測試人員3")
        self.elements.checkbox_add_member.click()
        self.elements.btn_project_member_add_filter_confirm.click()
        
    @allure.step("調整新增成員權限")
    def adjust_member_level(self):
        self.base_page.click_expect(self.elements.btn_project_member_add_levellist, self.elements.list_project_member_add_levellist)
        self.elements.list_project_member_add_viewer.click()
        self.elements.btn_project_member_add.click()

    @allure.step("搜尋新增成員")
    def search_member_add(self):
        self.elements.btn_submit.click()
        self.elements.btn_dialog_checked.click()
        self.elements.input_member_search.fill("測試人員3")
        expect(self.elements.btn_clear_noResult).not_to_be_visible()
    
    #read
    @allure.step("搜尋成員")
    def search_members(self):
        cases = [
            "testuser01","OmniHub","數位數據","omnitest3"
        ]
        inputElement = self.elements.input_search_project
        expectElement = self.elements.list_project_members
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
        self.elements.btn_filter_search.click()
        expect(self.elements.dialog_project_filter).to_be_visible()
        self.elements.btn_filter_level_editor.click()
        self.elements.btn_dialog_project_filter_search.click()
        expect(self.elements.list_project_members).not_to_be_visible()

        self.elements.btn_filter_search.click()
        expect(self.elements.dialog_project_filter).to_be_visible()
        self.elements.btn_filter_level_viewer.click()
        self.elements.btn_dialog_project_filter_search.click()
        expect(self.elements.list_project_members).not_to_be_visible()

        self.elements.btn_filter_search.click()
        expect(self.elements.dialog_project_filter).to_be_visible()
        self.elements.btn_filter_level_owner.click()
        self.elements.btn_dialog_project_filter_search.click()
        expect(self.elements.list_project_members).to_be_visible()
        
        self.elements.btn_filter_search.click()
        self.elements.btn_filter_clean_filter.click()

    #update
    @allure.step("新增第二個成員")
    def add_another_member(self):
        self.elements.btn_project_member_add_filter.click()
        self.elements.input_add_member_search.fill("測試人員2")
        self.elements.checkbox_add_member.click()
        self.elements.btn_project_member_add_filter_confirm.click()
        self.base_page.click_expect(self.elements.btn_project_member_add_levellist, self.elements.list_project_member_add_levellist)
        self.elements.list_project_member_add_viewer.click()
        self.elements.btn_project_member_add.click()
        
    @allure.step("調整舊成員權限")
    def adjust_previous_member_level(self):
        self.elements.list_editmember_tester3.locator("app-select p-select").click()
        expect(self.elements.list_project_member_add_levellist).to_be_visible()
        self.elements.list_project_member_add_editor.click()
        self.elements.btn_submit.click()
        self.elements.btn_dialog_checked.click()

    #delete
    @allure.step("刪除成員")
    def delete_member(self):
        self.elements.list_editmember_tester3.locator("app-icon img").click()
        expect(self.elements.list_editmember_tester3).not_to_be_visible()
        self.elements.btn_submit.click()
        self.elements.btn_dialog_checked.click()
