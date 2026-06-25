from playwright.sync_api import Page


class ProjectLocators:
    def __init__(self, page: Page):
        self.page = page


    @property
    def arrow_go_back(self):
        return self.page.locator('[class="go-back-btn__icon"]')
    

    @property
    def btn_back_to_overview(self):
        return self.page.get_by_text(" 返回專案總覽 ")

    @property
    def btn_card_transtfer_list(self):
        return self.page.locator('.function-bar .btn div').nth(1)

    @property
    def btn_create_project(self):
        return self.page.locator(".function-bar").get_by_role("button", name="新增專案", exact=True)

    @property
    def btn_dialog_project_fileter_status_disable(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="停用", exact=True)

    @property
    def btn_dialog_project_fileter_status_enable(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').first.get_by_role("button", name="啟用", exact=True)

    @property
    def btn_dialog_project_filter_newtoold(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由新至舊 ", exact=True)

    @property
    def btn_dialog_project_filter_oldtonew(self):
        return self.page.locator('[role="dialog"] .p-popover-content .search-popover__option').last.get_by_role("button", name=" 由舊至新 ", exact=True)

    @property
    def btn_edit_project(self):
        return self.page.get_by_text("編輯專案")

    @property
    def btn_list_transtfer_card(self):
        return self.page.locator('.function-bar .btn div').nth(0)

    @property
    def dialog_btn_cancel(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__footer').get_by_text(" 取消 ")
    

    @property
    def dialog_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog')

    @property
    def radio_status_disable(self):
        return self.page.get_by_text("停用")

    @property
    def radio_status_enable(self):
        return self.page.get_by_text("啟用")
