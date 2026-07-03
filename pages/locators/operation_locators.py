from playwright.sync_api import Page

class OperationLocators:
    def __init__(self, page: Page):
        self.page = page

    # Permission Navigation

    @property
    # 專案資訊頁面_身分認證按鈕
    def btn_project_info_permission(self):
        return self.page.locator(".sidebar__list", has=self.page.get_by_text(" 身份認證 ", exact=True))

    @property
    # 身分驗證頁面_logo
    def page_permission(self):
        return self.page.locator(".text-type--content-title")

    # Delete Dialog

    @property
    def dialog_input_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__body input')
