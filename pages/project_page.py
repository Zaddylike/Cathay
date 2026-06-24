from playwright.sync_api import Page, expect
from pages.elements import Elements
from pages.base_page import BasePage
from pages.operation_page import OperationPage
import allure

class ProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = Elements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperationPage(page)
    #create
    @allure.step("點擊「新增專案」按鈕")
    def open_create_project_dialog(self):
        self.base_page.click_expect(self.elements.btn_create_project)
        
    @allure.step("驗證「專案縮寫」欄位輸入")
    def validate_and_fill_project_abbreviation(self):
        self.input_abbr_cases = [
            ("中文", "只允許半形之英數字及符號：_-."),
            ("", "必填欄位"),
            ("$$$", "只允許半形之英數字及符號：_-."),
            ("ＡＢＣ", "只允許半形之英數字及符號：_-."),
            ("  ", "只允許半形之英數字及符號：_-."),
            ("#" * 41, "輸入字數超過限制長度40"),
        ]
        element_input = self.elements.input_nameAbbr
        element_error = self.elements.msg_error
        self.operate_page.verify_input(element_input, element_error, self.input_abbr_cases)
        self.elements.input_nameAbbr.fill("e2e-testing-abbr")

    @allure.step("驗證「專案中文」欄位輸入")
    def validate_and_fill_project_zh_name(self):
        self.input_zh_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
            ("  ", "必填欄位"),
        ]
        element_input = self.elements.input_nameZh
        element_error = self.elements.msg_error
        self.operate_page.verify_input(element_input, element_error, self.input_zh_cases)
        self.elements.input_nameZh.fill("e2e-testing-zh")

    @allure.step("輸入「專案英文」欄位")
    def fill_project_en_name(self):
        self.elements.input_nameEn.fill("e2e-testing-en")

    @allure.step("驗證「標籤」欄位新增")
    def validate_and_add_project_tags(self):
        self.input_tag_cases = [
            "中文","$$$","ＡＢＣ"
        ]
        self.elements.input_tag.click()
        self.elements.input_tag.fill("*"*42)
        expect(self.elements.msg_error, f"輸入字數超過限制長度40").to_be_visible()

        for input_msg in self.input_tag_cases:
            self.elements.input_tag.fill(input_msg)
            expect(self.elements.msg_error, f"Failed to fill {input_msg} to tag").not_to_be_visible()
            self.elements.btn_tag.click()

    @allure.step("驗證「狀態」欄位選擇")
    def enable_project_status(self):
        self.elements.btn_status_enable.click()
    
    @allure.step("驗證「專案描述」欄位輸入")
    def validate_and_fill_project_description(self):
        self.input_description_cases = [
            "中文","$$$","ＡＢＣ"
        ]

        self.elements.input_description.fill("*"*201)
        expect(self.elements.msg_error, f"輸入字數超過限制長度200").to_be_visible()    
        self.elements.input_description.fill("input testing description")

    @allure.step("驗證「專案圖示」欄位選擇")
    def select_project_icon(self):
        self.elements.logo_planets.nth(self.base_page.get_random_number(5)).click()
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()    

    @allure.step("送出成功後搜尋專案")
    def submit_project_and_verify_created(self):
        self.base_page.click_expect(self.elements.btn_submit, self.elements.dialog_page_success)
        self.elements.dialog_btn_checked.click()
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()

    #read
    @allure.step("檢視專案總覽")
    def verify_project_cards_visible(self):
        expect(self.elements.cards_project).to_be_visible()

    @allure.step("切換列表模式")
    def switch_to_project_list_view(self):
        self.base_page.click_expect(self.elements.btn_transform_list)
        expect(self.elements.list_transform).to_contain_class("right")

    @allure.step("切換卡片模式")
    def switch_to_project_card_view(self):
        self.base_page.click_expect(self.elements.btn_transform_card)
        expect(self.elements.list_transform).to_contain_class("left")

    @allure.step("搜尋框搜尋不存在專案縮寫")
    def search_project_with_no_result(self):
        self.elements.input_search_field.fill("xxxxxxxxxxxx")
        expect(self.elements.msg_search_nodata).to_be_visible()
        self.elements.btn_clean_nodata.click()

    @allure.step("搜尋框搜尋已存在專案縮寫")
    def search_project_by_abbreviation(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.btn_clean_search.click()

    @allure.step("搜尋框搜尋已存在專案中文")
    def search_project_by_zh_name(self):
        self.elements.input_search_field.fill("e2e-testing-zh")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.btn_clean_search.click(force=True)
        
    @allure.step("進階篩選面板篩選狀態")
    def filter_projects_by_status(self):
                
        self.elements.input_search_field.click()
        self.base_page.click_expect(self.elements.btn_filter_page, self.elements.dialog_page_filter, True)
        self.elements.btn_filter_status_enable.click()
        self.base_page.click_expect(self.elements.btn_filter_search, self.elements.cards_project)

        self.base_page.sleep(1)
        self.elements.input_search_field.click()
        self.base_page.click_expect(self.elements.btn_filter_page, self.elements.dialog_page_filter, True)
        self.elements.btn_filter_status_disable.click()
        self.base_page.click_expect(self.elements.btn_filter_search, self.elements.cards_project)

        self.base_page.sleep(1)
        self.elements.input_search_field.click()
        self.base_page.click_expect(self.elements.btn_filter_page, self.elements.dialog_page_filter, True)
        self.elements.btn_filter_clean_filter.click()

    @allure.step("進階篩選面板排序日期")
    def sort_projects_by_created_time(self):
        self.elements.input_search_field.click()
        self.base_page.click_expect(self.elements.btn_filter_page, self.elements.dialog_page_filter, True)
        self.elements.btn_filter_index_oldtonew.click()
        self.base_page.click_expect(self.elements.btn_filter_search, self.elements.cards_project)

        self.elements.input_search_field.click()
        self.base_page.click_expect(self.elements.btn_filter_page, self.elements.dialog_page_filter, True)
        self.elements.btn_filter_index_newtoold.click()
        self.base_page.click_expect(self.elements.btn_filter_search, self.elements.cards_project)

        self.elements.input_search_field.click()
        self.base_page.click_expect(self.elements.btn_filter_page, self.elements.dialog_page_filter, True)
        self.elements.btn_filter_clean_filter.click()

    @allure.step("檢視專案詳細資訊頁面")
    def open_project_detail_from_search(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.click()

    @allure.step("檢視專案成員頁面")
    def open_project_members(self):
        self.elements.btn_member.click()

    @allure.step("專案成員頁面搜尋成員")
    def search_project_members(self):
        cases = [
            "testuser01","預設公司","OmniHub","預設單位"
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

    @allure.step("專案成員頁面進階搜尋成員權限")
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

    @allure.step("使用專案清單切換專案")
    def return_to_project_overview(self):
        self.elements.arrow_go_back.click()

    #update
    @allure.step("依照縮寫搜尋成功後點擊")
    def open_project_edit_form(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.first.click()
        self.base_page.click_expect(self.elements.btn_edit, self.elements.btn_submit)
        
    @allure.step("[PROJECT-UPDATE-003] Validate and update project Chinese name")
    def validate_and_update_project_zh_name(self):
        self.input_zh_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
            ("  ", "必填欄位"),
        ]
        element_input = self.elements.input_nameZh
        element_error = self.elements.msg_error
        self.operate_page.verify_input(element_input, element_error, self.input_zh_cases)
        self.elements.input_nameZh.fill("e2e-edited-zh")

    @allure.step("[PROJECT-UPDATE-004] Update project English name")
    def update_project_en_name(self):
        self.elements.input_nameEn.fill("e2e-edited-en")

    @allure.step("[PROJECT-UPDATE-005] Update project tag")
    def update_project_tag(self):
        self.page.locator("app-custom-form-field  .cursor-pointer").nth(0).click()
        self.elements.input_tag.fill("編輯")
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()
        self.elements.btn_tag.click()

    @allure.step("[PROJECT-UPDATE-006] Disable project status")
    def disable_project_status(self):
        self.elements.btn_status_disable.click()

    @allure.step("[PROJECT-UPDATE-007] Update project description")
    def update_project_description(self):
        self.elements.input_description.fill("edited testing description")
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()    
    
    @allure.step("[PROJECT-UPDATE-008] Update project icon")
    def update_project_icon(self):
        self.elements.logo_planets.nth(self.base_page.get_random_number(5)).click()
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()    

    @allure.step("[PROJECT-UPDATE-009-011] Submit project update and verify")
    def submit_project_update_and_verify(self):
        self.base_page.click_expect(self.elements.btn_submit, self.elements.dialog_page_success)
        self.elements.dialog_btn_checked.click()
        self.elements.btn_back_to_overview.click()
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()

    #delete
    @allure.step("[PROJECT-DELETE-002] Open project delete dialog")
    def open_project_delete_dialog(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.first.click()
        self.base_page.click_expect(self.elements.btn_delete, self.elements.dialog_delete)

    @allure.step("[PROJECT-DELETE-003] Verify delete confirm is disabled by default")
    def verify_delete_confirm_disabled_by_default(self):
        expect(self.elements.dialog_btn_confirm).to_be_disabled()

    @allure.step("[PROJECT-DELETE-004] Cancel project delete then reopen")
    def cancel_project_delete_then_reopen(self):
        self.base_page.click_expect(self.elements.dialog_btn_cancel)
        self.base_page.click_expect(self.elements.btn_delete)

    @allure.step("[PROJECT-DELETE-005] Confirm project delete")
    def confirm_project_delete(self):
        self.operate_page.verify_delete()

    @allure.step("[PROJECT-DELETE-006] Verify project deleted")
    def verify_project_deleted(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).to_be_visible()
