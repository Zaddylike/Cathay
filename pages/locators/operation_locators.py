from playwright.sync_api import Page


class OperationLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def dialog_input_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__body input')

    @property
    def page_permission(self):
        # 身分驗證頁面_logo
        return self.page.locator(".text-type--content-title")

    @property
    def btn_project_info_permission(self):
        # 專案資訊頁面_身分認證按鈕
        return self.page.locator(".sidebar__list", has=self.page.get_by_text(" 身份認證 ", exact=True))