from playwright.sync_api import Page, expect
from config.settings import BASE_URL_DEV, DEFAULT_TIMEOUT

"""
locator
get_by_placeholder
get_by_role
get_by_text
"""

class OperationPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.todo_input = page.get_by_placeholder("What needs to be done?")
        self.todo_items = page.locator(".todo-list li")

    def filling_field(self, todo_name: str):
        try:
            self.todo_input.fill(todo_name)
            self.todo_input.press("Enter")
        except Exception as e:
            raise Exception(f"Add todo failed: {e}")

    def verify_todo_visible(self, todo_name: str):
        try:
            expect(self.page.get_by_text(todo_name)).to_be_visible()
        except Exception as e:
            raise AssertionError(f"Verify todo visible failed: {e}")

    def verify_todo_count(self, count: int):
        try:
            expect(self.todo_items).to_have_count(count)
        except Exception as e:
            raise AssertionError(f"Verify todo count failed: {e}")

    def complete_first_todo(self):
        try:
            self.page.locator(".todo-list li .toggle").first.click()
        except Exception as e:
            raise Exception(f"Complete first todo failed: {e}")