import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.locators.elements import GroupElements
from pages.operate_page import OperatePage

from config.settings import (
        INPUT_BASIC_FIELD_CASES,
        INPUT_BASIC_DESC_CASES
    )

class GroupPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = GroupElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    @allure.step("新增群組 [{group_name}]")
    def create_group(self, group_name: str, group_description: str, member_keyword: str):
        self.click_to_create_group_page()
        self.open_create_group_page()
        self.elements.input_group_name.first.fill(group_name)
        self.elements.input_group_description.first.fill(group_description)
        self.invite_group_member(member_keyword, group_description)
        self.operate_page.submit_and_confirm()
        self.search_group_by_name(group_name)

    #  create

    @allure.step("進入群組功能並開啟新增頁面")
    def click_to_create_group_page(self):
        self.base_page.click_expect(self.elements.tab_permission_group, self.elements.btn_create_group)
        self.base_page.click_expect(self.elements.btn_create_group, self.elements.btn_create_more_group)

    @allure.step("開啟另一筆群組新增表單")
    def open_create_group_page(self):
        self.base_page.click_expect(self.elements.btn_create_more_group, self.elements.input_group_name.first)

    @allure.step("驗證並填寫群組名稱")
    def validate_and_fill_group_name(self, group_name: str):
        self.operate_page.verify_input(
            self.elements.input_group_name.first,
            self.elements.msg_field_error,
            INPUT_BASIC_FIELD_CASES,
        )
        self.elements.input_group_name.first.fill(group_name)

    @allure.step("驗證並填寫群組描述")
    def validate_and_fill_group_description(self, group_description: str):
        self.operate_page.verify_input(
            self.elements.input_group_description.first,
            self.elements.msg_field_error,
            INPUT_BASIC_DESC_CASES,
        )
        self.elements.input_group_description.first.fill(group_description)

    @allure.step("邀請群組成員")
    def invite_group_member(self, member_keyword: str, group_description: str):
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.first,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            member_keyword,
        )
        self.base_page.click_expect(self.elements.btn_group_add_member)
        self.base_page.wait_fill(self.elements.input_group_description.last, group_description)

    @allure.step("送出群組並驗證新增成功")
    def submit_and_verify_created(self, group_name: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            group_name,
            should_exist=False
        )

    #  copy

    @allure.step("開啟群組清單")
    def click_to_group_page(self):
        self.base_page.click_expect(self.elements.tab_permission_group, self.elements.btn_create_group)

    @allure.step("開啟複製群組頁面")
    def open_copy_group_page(self, source_group_name: str):
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            source_group_name,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_copy,
        )

    @allure.step("驗證並填寫複製後的群組資料")
    def validate_and_fill_copied_group(
        self,
        copied_group_name: str,
        copied_group_description: str,
    ):
        self.operate_page.verify_input_text(self.elements.input_group_name, "copy-")
        self.elements.input_group_name.fill(copied_group_name)
        self.elements.input_group_description.first.fill(copied_group_description)

    @allure.step("送出群組並驗證複製成功")
    def submit_and_verify_copied(self, copied_group_name: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            copied_group_name,
            self.elements.option_cards.last
        )

    #  read

    @allure.step("搜尋不存在的群組並驗證無結果")
    def search_group_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("依群組名稱搜尋")
    def search_group_by_name(self, group_name: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            group_name,
            self.elements.option_cards.last
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("依狀態篩選群組")
    def filter_groups_by_status(self):
        self.elements.input_keyword_search.click()
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_status_enable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.sleep(1)
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_status_disable.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.sleep(1)
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_footer_clearfilter.click()

    @allure.step("依建立時間排序群組")
    def sort_groups_by_created_time(self):
        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_date_reyoung.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_date_grewup.click()
        self.base_page.click_expect(self.elements.btn_filter_footer_search, self.elements.option_cards.last)

        self.base_page.click_expect(self.elements.btn_filter_condition_page.last, self.elements.page_filter_condition)
        self.elements.btn_filter_footer_clearfilter.click()

    #  update

    @allure.step("開啟編輯群組頁面")
    def open_update_group_page(self, group_name: str):
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            group_name,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
        )

    @allure.step("驗證並更新群組名稱")
    def validate_and_update_group_name(self, updated_group_name: str):
        input_cases = [
            ("#" * 41, "輸入字數超過限制長度40"),
            # ("  ", "必填欄位"),
            ("", "必填欄位"),
        ]
        self.operate_page.verify_input(
            self.elements.input_group_name,
            self.elements.msg_field_error,
            input_cases,
        )
        self.elements.input_group_name.fill(updated_group_name)

    @allure.step("驗證並更新群組描述")
    def validate_and_update_group_description(self, updated_group_description: str):
        input_cases = [
            ("#" * 201, "輸入字數超過限制長度200"),
        ]
        self.operate_page.verify_input(
            self.elements.input_group_description.first,
            self.elements.msg_field_error,
            input_cases,
        )
        self.elements.input_group_description.first.fill(updated_group_description)

    @allure.step("停用群組狀態")
    def disable_group_status(self):
        self.elements.radio_status_disable.click()

    @allure.step("送出群組並驗證更新成功")
    def submit_and_verify_updated(self, updated_group_name: str):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            updated_group_name,
            self.elements.option_cards.last
        )

    #  delete

    @allure.step("開啟刪除群組視窗")
    def open_group_delete_dialog(self, group_name: str):
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            group_name,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
        )

    @allure.step("驗證群組刪除確認欄位")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("刪除群組 [{group_name}]")
    def delete_group(self, group_name: str):
        self.click_to_group_page()
        self.open_group_delete_dialog(group_name)
        self.verify_deleted_input()

    @allure.step("若群組存在則刪除 [{group_name}]")
    def delete_group_if_exists(self, group_name: str) -> bool:
        self.click_to_group_page()
        self.elements.input_keyword_search.fill(group_name)
        self.base_page.wait_loading_disapper()
        if self.elements.msg_search_noResult.is_visible():
            self.elements.input_keyword_search.fill("")
            return False
        self.open_group_delete_dialog(group_name)
        self.verify_deleted_input()
        return True

    @allure.step("驗證群組已刪除 [{group_name}]")
    def verify_group_deleted(self, group_name: str):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            group_name,
            self.elements.msg_search_noResult,
            should_exist=True,
        )
