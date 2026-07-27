from playwright.sync_api import Page


class ElementsBase:
    def __init__(self, page: Page):
        self.page = page
