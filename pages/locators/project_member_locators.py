from playwright.sync_api import Page


class ProjectMemberLocators:
    def __init__(self, page: Page):
        self.page = page


    @property
    def input_member_search(self):
        return self.page.get_by_placeholder("請輸入關鍵字", exact=True)   

    @property
    def list_project_member_add_editor(self):
        return self.page.locator('.p-select-list-container .p-select-list [aria-label="EDITOR"]')
