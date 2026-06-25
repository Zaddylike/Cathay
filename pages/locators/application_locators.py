from playwright.sync_api import Page


class ApplicationLocators:
    def __init__(self, page: Page):
        self.page = page


    @property
    def btn_user_permission(self):
        return self.page.locator(".sidebar__item").get_by_text(" 身份認證 ")

    @property
    def tab_permissions_all(self):
        return self.page.locator('.p-tablist-content [role="tablist"] p-tab')

    @property
    def tab_permissions_last(self):
        return self.page.locator('.p-tablist-content [role="tablist"] p-tab').last
