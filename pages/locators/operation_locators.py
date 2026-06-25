from playwright.sync_api import Page


class OperationLocators:
    def __init__(self, page: Page):
        self.page = page


    @property
    def dialog_input_delete(self):
        return self.page.locator('[role="dialog"] app-prompt-delete-dialog .form-dialog__body input')
