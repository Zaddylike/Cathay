from playwright.sync_api import Page, expect
from pages.elements import Elements
from pages.base_page import BasePage
import allure

class ProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = Elements(page)
        self.base_page = BasePage(page)

    #create
    @allure.step("點擊「新增專案」按鈕")
    def project_create_002(self):
        self.base_page.click_expect(self.elements.btn_create_project)
        
    @allure.step("驗證「專案縮寫」欄位輸入")
    def project_create_003(self):
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
        self.base_page.verify_input(element_input, element_error, self.input_abbr_cases)
        self.elements.input_nameAbbr.fill("e2e-testing-abbr")

    @allure.step("驗證「專案中文」欄位輸入")
    def project_create_004(self):
        self.input_zh_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
            ("  ", "必填欄位"),
        ]
        element_input = self.elements.input_nameZh
        element_error = self.elements.msg_error
        self.base_page.verify_input(element_input, element_error, self.input_zh_cases)
        self.elements.input_nameZh.fill("e2e-testing-zh")

    @allure.step("輸入「專案英文」欄位")
    def project_create_005(self):
        self.elements.input_nameEn.fill("e2e-testing-en")

    @allure.step("驗證「標籤」欄位新增")
    def project_create_006(self):
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
    def project_create_007(self):
        self.elements.btn_status_enable.click()
    
    @allure.step("驗證「專案描述」欄位輸入")
    def project_create_008(self):
        self.input_description_cases = [
            "中文","$$$","ＡＢＣ"
        ]

        self.elements.input_description.fill("*"*201)
        expect(self.elements.msg_error, f"輸入字數超過限制長度200").to_be_visible()    
        self.elements.input_description.fill("input testing description")

    @allure.step("驗證「專案圖示」欄位選擇")
    def project_create_009(self):
        self.elements.logo_planets.nth(self.base_page.get_random_number(5)).click()
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()    

    @allure.step("送出成功後搜尋專案")
    def project_create_010_011(self):
        self.base_page.click_expect(self.elements.btn_submit, self.elements.dialog_page_success)
        self.elements.dialog_btn_checked.click()
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()

    #read
    @allure.step("檢視專案總覽")
    def project_read_002(self):
        expect(self.elements.cards_project).to_be_visible()

    @allure.step("切換列表模式")
    def project_read_003(self):
        self.base_page.click_expect(self.elements.btn_transform_list)
        expect(self.elements.list_transform).to_contain_class("right")

    @allure.step("切換卡片模式")
    def project_read_004(self):
        self.base_page.click_expect(self.elements.btn_transform_card)
        expect(self.elements.list_transform).to_contain_class("left")

    @allure.step("搜尋框搜尋不存在專案縮寫")
    def project_read_005(self):
        self.elements.input_search_field.fill("xxxxxxxxxxxx")
        expect(self.elements.msg_search_nodata).to_be_visible()
        self.elements.btn_clean_nodata.click()

    @allure.step("搜尋框搜尋已存在專案縮寫")
    def project_read_006(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.btn_clean_search.click()

    @allure.step("搜尋框搜尋已存在專案中文")
    def project_read_007(self):
        self.elements.input_search_field.fill("e2e-testing-zh")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.btn_clean_search.click(force=True)
    @allure.step("進階篩選面板篩選狀態")
    def project_read_008(self):
                
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
    def project_read_009(self):
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
    def project_read_010(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.click()

    @allure.step("檢視專案成員頁面")
    def project_read_011(self):
        self.elements.btn_member.click()

    @allure.step("專案成員頁面搜尋成員")
    def project_read_012(self):
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
    def project_read_013(self):
        self.elements.btn_filter_page.click()
        expect(self.elements.dialog_page_filter).to_be_visible()
        self.elements.btn_filter_level_editor.click()
        self.elements.btn_filter_search.click()
        expect(self.elements.list_project_member).not_to_be_visible()

        self.elements.btn_filter_page.click()
        expect(self.elements.dialog_page_filter).to_be_visible()
        self.elements.btn_filter_level_viwer.click()
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
    def project_read_014(self):
        self.elements.arrow_go_back.click()

    #update
    @allure.step("依照縮寫搜尋成功後點擊")
    def project_update_002(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.first.click()
        self.base_page.click_expect(self.elements.btn_edit, self.elements.btn_submit)
        
    def project_update_003(self):
        self.input_zh_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            ("", "必填欄位"),
            ("  ", "必填欄位"),
        ]
        element_input = self.elements.input_nameZh
        element_error = self.elements.msg_error
        self.base_page.verify_input(element_input, element_error, self.input_zh_cases)
        self.elements.input_nameZh.fill("e2e-edited-zh")

    def project_update_004(self):
        self.elements.input_nameEn.fill("e2e-edited-en")

    def project_update_005(self):
        self.page.locator("app-custom-form-field  .cursor-pointer").nth(0).click()
        self.elements.input_tag.fill("編輯")
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()
        self.elements.btn_tag.click()

    def project_update_006(self):
        self.elements.btn_status_disable.click()

    def project_update_007(self):
        self.elements.input_description.fill("edited testing description")
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()    
    
    def project_update_008(self):
        self.elements.logo_planets.nth(self.base_page.get_random_number(5)).click()
        expect(self.elements.msg_error, f"錯誤訊息").not_to_be_visible()    

    def project_update_009_011(self):
        self.base_page.click_expect(self.elements.btn_submit, self.elements.dialog_page_success)
        self.elements.dialog_btn_checked.click()
        self.elements.btn_back_to_overview.click()
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()

    #delete
    def project_delete_002(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).not_to_be_visible()
        self.elements.cards_project.first.click()
        self.base_page.click_expect(self.elements.btn_delete, self.elements.dialog_delete)

    def project_delete_003(self):
        expect(self.elements.dialog_btn_confirm).to_be_disabled()

    def project_delete_004(self):
        self.base_page.click_expect(self.elements.dialog_btn_cancel)
        self.base_page.click_expect(self.elements.btn_delete)

    def project_delete_005(self):
        self.base_page.verify_delete()

    def project_delete_006(self):
        self.elements.input_search_field.fill("e2e-testing-abbr")
        expect(self.elements.msg_search_nodata).to_be_visible()