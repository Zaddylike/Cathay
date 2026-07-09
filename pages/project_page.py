from playwright.sync_api import Page, expect
from pages.locators.elements import ProjectElements
from pages.base_page import BasePage
from pages.operate_page import OperatePage
import allure

class ProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ProjectElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)
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
        element_input = self.elements.input_project_abbr
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_abbr_cases)
        self.elements.input_project_abbr.fill("e2e-project-abbr")

    @allure.step("驗證「專案中文」欄位輸入")
    def validate_and_fill_project_zh_name(self):
        self.input_zh_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
            ("  ", "必填欄位"),
        ]
        element_input = self.elements.input_project_nameZh
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_zh_cases)
        self.elements.input_project_nameZh.fill("e2e-testing-zh")

    @allure.step("輸入「專案英文」欄位")
    def fill_project_en_name(self):
        self.elements.input_project_nameEn.fill("e2e-testing-en")

    @allure.step("驗證「標籤」欄位新增")
    def validate_and_add_project_tags(self):
        self.input_project_tag_cases = [
            "中文","$$$","ＡＢＣ"
        ]
        self.elements.input_project_tag.click()
        self.elements.input_project_tag.fill("*"*42)
        expect(self.elements.msg_field_error, f"輸入字數超過限制長度40").to_be_visible()

        for input_msg in self.input_project_tag_cases:
            self.elements.input_project_tag.fill(input_msg)
            expect(self.elements.msg_field_error, f"Failed to fill {input_msg} to tag").not_to_be_visible()
            self.elements.btn_project_tag.click()

    @allure.step("驗證「狀態」欄位選擇")
    def enable_project_status(self):
        self.elements.radio_status_enable.click()
    
    @allure.step("驗證「專案描述」欄位輸入")
    def validate_and_fill_project_description(self):
        self.input_project_description_cases = [
            "中文","$$$","ＡＢＣ"
        ]

        self.elements.input_project_description.fill("*"*201)
        expect(self.elements.msg_field_error, f"輸入字數超過限制長度200").to_be_visible()    
        self.elements.input_project_description.fill("input testing description")

    @allure.step("驗證「專案圖示」欄位選擇")
    def select_project_icon(self):
        self.elements.img_planets.nth(self.base_page.get_random_number(5)).click()
        expect(self.elements.msg_field_error, f"錯誤訊息").not_to_be_visible()    

    @allure.step("送出成功後搜尋專案")
    def submit_project_and_verify_created(self):
<<<<<<< HEAD
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-project-abbr",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
=======
        self.base_page.click_expect(self.elements.btn_submit, self.elements.page_dialog)
        self.elements.btn_dialog_checked.click()
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
>>>>>>> 80fa955 (update)

    #read
    @allure.step("檢視專案總覽")
    def verify_project_cards_visible(self):
        expect(self.elements.option_cards.first).to_be_visible()

    @allure.step("切換列表模式")
    def switch_to_project_list_view(self):
        self.base_page.click_expect(self.elements.btn_projet_type_list)
        expect(self.elements.dashboard_type_projects).to_contain_class("right")

    @allure.step("切換卡片模式")
    def switch_to_project_card_view(self):
        self.base_page.click_expect(self.elements.btn_projet_type_card)
        expect(self.elements.dashboard_type_projects).to_contain_class("left")

    @allure.step("搜尋框搜尋不存在專案縮寫")
    def search_project_with_no_result(self):
<<<<<<< HEAD
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
=======
        self.elements.input_keyword_search.fill("xxxxxxxxxxxx")
        expect(self.elements.msg_search_noResult).to_be_visible()
>>>>>>> 80fa955 (update)
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("搜尋框搜尋已存在專案縮寫")
    def search_project_by_abbreviation(self):
<<<<<<< HEAD
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-project-abbr",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
=======
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
>>>>>>> 80fa955 (update)
        self.elements.btn_filter_clear_search.click()

    @allure.step("搜尋框搜尋已存在專案中文")
    def search_project_by_zh_name(self):
<<<<<<< HEAD
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-testing-zh",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
=======
        self.elements.input_keyword_search.fill("e2e-testing-zh")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
>>>>>>> 80fa955 (update)
        self.elements.btn_filter_clear_search.click(force=True)
        
    @allure.step("進階篩選面板篩選狀態")
    def filter_projects_by_status(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_enable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_status_disable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.base_page.sleep(1)
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("進階篩選面板排序日期")
    def sort_projects_by_created_time(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_date_reyoung.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_date_grewup.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.first)

        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition, True)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("檢視專案詳細資訊頁面")
    def open_project_detail_from_search(self):
<<<<<<< HEAD
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-project-abbr",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
=======
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
>>>>>>> 80fa955 (update)
        self.elements.option_cards.first.click()

    @allure.step("檢視專案成員頁面")
    def open_project_members(self):
        self.elements.btn_project_edit_member.first.click()

    @allure.step("專案成員頁面搜尋成員")
    def search_project_members(self):
        cases = [
            "testuser01","預設公司","OmniHub","預設單位"
        ]
        inputElement = self.elements.input_keyword_search
        expectElement = self.elements.option_cards_members
        try:
            for input_value in cases:
<<<<<<< HEAD
                self.operate_page.search_keyword(inputElement, input_value, expectElement)
=======
                inputElement.fill(input_value)
                expect(expectElement).to_be_visible()
>>>>>>> 80fa955 (update)
                inputElement.fill("")
        except Exception as e:
            raise Exception(f"Failed to verify input : {e}")

    @allure.step("專案成員頁面進階搜尋成員權限")
    def filter_project_members_by_role(self):
        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_memberadd_filter_level_editor.click()
        self.elements.btn_filter_footer_search.click()
        expect(self.elements.option_cards_members).not_to_be_visible()

        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_memberadd_filter_level_viewer.click()
        self.elements.btn_filter_footer_search.click()
        expect(self.elements.option_cards_members).not_to_be_visible()

        self.base_page.click_expect(self.elements.btn_filter_condition_page, self.elements.page_filter_condition)
        self.elements.btn_memberadd_filter_level_owner.click()
        self.elements.btn_filter_footer_search.click()
        expect(self.elements.option_cards_members).to_be_visible()
        
        self.elements.btn_filter_condition_page.click()
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("使用專案清單切換專案")
    def return_to_project_overview(self):
        self.elements.arrow_go_back.click()

    #update
    @allure.step("依照縮寫搜尋成功後點擊")
    def open_project_edit_form(self):
<<<<<<< HEAD
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-project-abbr",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
=======
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
>>>>>>> 80fa955 (update)
        self.elements.option_cards.first.click()
        self.base_page.click_expect(self.elements.btn_edit_project, self.elements.btn_submit)
        
    @allure.step("編輯並驗證專案中文欄位")
    def validate_and_update_project_zh_name(self):
        self.input_zh_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
            ("  ", "必填欄位"),
        ]
        element_input = self.elements.input_project_nameZh
        element_error = self.elements.msg_field_error
        self.operate_page.verify_input(element_input, element_error, self.input_zh_cases)
        self.elements.input_project_nameZh.fill("e2e-edited-zh")

    @allure.step("編輯並驗證專案英文欄位")
    def update_project_en_name(self):
        self.elements.input_project_nameEn.fill("e2e-edited-en")

    @allure.step("編輯並驗證專案標籤")
    def update_project_tag(self):
        self.page.locator("app-custom-form-field  .cursor-pointer").nth(0).click()
        self.elements.input_project_tag.fill("編輯")
        expect(self.elements.msg_field_error, f"錯誤訊息").not_to_be_visible()
        self.elements.btn_project_tag.click()

    @allure.step("編輯專案狀態")
    def disable_project_status(self):
        self.elements.radio_status_disable.click()

    @allure.step("編輯專案描述")
    def update_project_description(self):
        self.elements.input_project_description.fill("edited testing description")
        expect(self.elements.msg_field_error, f"錯誤訊息").not_to_be_visible()    
    
    @allure.step("編輯專案圖示")
    def update_project_icon(self):
        self.elements.img_planets.nth(self.base_page.get_random_number(5)).click()
        expect(self.elements.msg_field_error, f"錯誤訊息").not_to_be_visible()    

    @allure.step("提交專案編輯及驗證")
    def submit_project_update_and_verify(self):
<<<<<<< HEAD
        self.operate_page.submit_and_confirm()
        self.elements.btn_back_to_overview.click()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-project-abbr",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
=======
        self.base_page.click_expect(self.elements.btn_submit, self.elements.page_dialog)
        self.elements.btn_dialog_checked.click()
        self.elements.btn_back_to_overview.click()
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
>>>>>>> 80fa955 (update)

    #delete
    @allure.step("開啟刪除視窗")
    def open_project_delete_dialog(self):
<<<<<<< HEAD
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-project-abbr",
            self.elements.msg_search_noResult,
            should_exist=False,
        )
=======
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).not_to_be_visible()
>>>>>>> 80fa955 (update)
        self.elements.option_cards.first.click()
        self.base_page.click_expect(self.elements.btn_delete_project, self.elements.page_dialog)

    @allure.step("驗證無內容時不可點確認")
    def verify_delete_confirm_disabled_by_default(self):
        expect(self.elements.btn_dialog_delete_confirm).to_be_disabled()

    @allure.step("重新開啟視窗驗證專案沒有誤刪")
    def cancel_project_delete_then_reopen(self):
        self.base_page.click_expect(self.elements.btn_dialog_delete_cancel)
        self.base_page.click_expect(self.elements.btn_delete_project)

    @allure.step("輸入DELETE並驗證輸入欄位")
    def confirm_project_delete(self):
        self.operate_page.verify_delete()

    @allure.step("驗證刪除成功")
    def verify_project_deleted(self):
<<<<<<< HEAD
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-project-abbr",
            self.elements.msg_search_noResult,
        )
=======
        self.elements.input_keyword_search.fill("e2e-project-abbr")
        expect(self.elements.msg_search_noResult).to_be_visible()
>>>>>>> 80fa955 (update)
