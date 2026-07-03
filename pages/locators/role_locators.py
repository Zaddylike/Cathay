from playwright.sync_api import Page


class RoleLocators:
    def __init__(self, page: Page):
        self.page = page
