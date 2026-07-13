import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators.elements import GroupElements
from pages.operate_page import OperatePage

from config.settings import (
        GROUP_NAME,
        INPUT_BASIC_FIELD_CASES,
        INPUT_BASIC_DESC_CASES
    )

class GroupPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = GroupElements(page)
        self.base_page = BasePage(page)
        self.operate_page = OperatePage(page)

    #  create

    @allure.step("Open create group page")
    def click_to_create_group_page(self):
        self.base_page.click_expect(self.elements.tab_permission_group, self.elements.btn_create_group)
        self.base_page.click_expect(self.elements.btn_create_group, self.elements.btn_create_more_group)

    @allure.step("Open create group page")
    def open_create_group_page(self):
        self.base_page.click_expect(self.elements.btn_create_more_group, self.elements.input_group_name.first)

    @allure.step("Validate and fill group name")
    def validate_and_fill_group_name(self):
        self.operate_page.verify_input(
            self.elements.input_group_name.first,
            self.elements.msg_field_error,
            INPUT_BASIC_FIELD_CASES,
        )
        self.elements.input_group_name.first.fill(GROUP_NAME)

    @allure.step("Validate and fill group description")
    def validate_and_fill_group_description(self):
        self.operate_page.verify_input(
            self.elements.input_group_description.first,
            self.elements.msg_field_error,
            INPUT_BASIC_DESC_CASES,
        )
        self.elements.input_group_description.first.fill("e2e-group-description")

    @allure.step("Invite group member")
    def invite_group_member(self):
        self.operate_page.select_member_from_advanced_search(
            self.elements.btn_filter_condition_page.first,
            self.elements.input_memberadd_advanced_search,
            self.elements.checkbox_add_member,
            self.elements.btn_memberadd_footer_confirm,
            "testuser01",
        )
        self.base_page.click_expect(self.elements.btn_group_header_add_member)
        self.base_page.wait_fill(self.elements.input_group_description.last, "e2e-group-description")

    @allure.step("Submit group and verify created")
    def submit_and_verify_created(self):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            GROUP_NAME,
            should_exist=False
        )

    #  copy

    @allure.step("Open create group page")
    def click_to_group_page(self):
        self.base_page.click_expect(self.elements.tab_permission_group, self.elements.btn_create_group)

    @allure.step("Open copy group page")
    def open_copy_group_page(self):
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            GROUP_NAME,
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_copy,
        )

    @allure.step("Validate and fill copied group")
    def validate_and_fill_copied_group(self):
        self.operate_page.verify_input_text(self.elements.input_group_name, "copy-")
        self.elements.input_group_name.fill(f"copy-{GROUP_NAME}")
        self.elements.input_group_description.first.fill("copy-e2e-group-description")

    @allure.step("Submit group and verify copied")
    def submit_and_verify_copied(self):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            f"copy-{GROUP_NAME}",
            self.elements.option_cards.last
        )

    #  read

    @allure.step("Search group with no result")
    def search_group_with_no_result(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "xxxxxxxxxxxx",
            self.elements.msg_search_noResult,
        )
        self.elements.btn_filter_clear_noResult.click()

    @allure.step("Search group by name")
    def search_group_by_name(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-group-name",
            self.elements.option_cards.last
        )
        self.elements.input_keyword_search.fill("")

    @allure.step("Filter groups by status")
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

    @allure.step("Sort groups by created time")
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

    @allure.step("Open update group page")
    def open_update_group_page(self):
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            f"copy-{GROUP_NAME}",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_update,
        )

    @allure.step("Validate and update group name")
    def validate_and_update_group_name(self):
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
        self.elements.input_group_name.fill("e2e-group-name-edit")

    @allure.step("Validate and update group description")
    def validate_and_update_group_description(self):
        input_cases = [
            ("#" * 201, "輸入字數超過限制長度200"),
        ]
        self.operate_page.verify_input(
            self.elements.input_group_description.first,
            self.elements.msg_field_error,
            input_cases,
        )
        self.elements.input_group_description.first.fill("e2e-group-description-edit")

    @allure.step("Disable group status")
    def disable_group_status(self):
        self.elements.radio_status_disable.click()

    @allure.step("Submit group and verify updated")
    def submit_and_verify_updated(self):
        self.operate_page.submit_and_confirm()
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-group-name-edit",
            self.elements.option_cards.last
        )

    #  delete

    @allure.step("Open group delete dialog")
    def open_group_delete_dialog(self):
        self.operate_page.open_card_action(
            self.elements.input_keyword_search,
            "e2e-group-name-edit",
            self.elements.btn_card_threepoint_menu,
            self.elements.page_card_threepoint_menu,
            self.elements.btn_card_menu_delete,
        )

    @allure.step("Verify group delete input")
    def verify_deleted_input(self):
        self.operate_page.verify_delete()

    @allure.step("Verify deleted group")
    def verify_group_deleted(self):
        self.operate_page.search_keyword(
            self.elements.input_keyword_search,
            "e2e-group-name-edit",
            self.elements.msg_search_noResult,
            should_exist=True,
        )
