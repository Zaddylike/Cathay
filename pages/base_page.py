from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
from config.settings import BASE_URL_DEV, DEFAULT_TIMEOUT
import random
import allure
from allure_commons.types import AttachmentType

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def sleep(self, seconds: int):
        try:
            self.page.wait_for_timeout(seconds * 1000)
        except Exception as e:
            raise Exception(f"Failed to sleep: {e}")
    
    def take_screenshot(self, photo_name):
        allure.attach(
            self.page.screenshot(),
            name=f"{photo_name}",
            attachment_type=allure.attachment_type.PNG
        )

    def click_expect(self, locator, expected_after_click=None, double=False):
        try:
            locator.click()
        except PlaywrightTimeoutError as e:
            raise AssertionError(f"Timeout: {e}")
        except Exception as e:
            raise Exception(f"Failed to click: {e}")

        if expected_after_click is not None:
            try:
                expect(expected_after_click).to_be_visible()
            except PlaywrightTimeoutError as e:
                if double:
                    self.click_expect(locator, expected_after_click, False)
                else:
                    raise AssertionError(f"Timeout: {e}")
            except Exception as e:
                raise Exception(f"Click passed, but expected element is not visible: {e}")
        
        self.wait_loading_disapper()

    def fill(self, locator, value: str):
        try:
            locator.fill(value)
        except Exception as e:
            raise Exception(f"Failed to fill value: {e}")

    def verify_visible(self, locator, action_name: str = "Verify visible"):
        try:
            expect(locator).to_be_visible()
        except Exception as e:
            raise AssertionError(f"{action_name} failed: {e}")
        
    def wait_loading_disapper(self):
        try:
            self.page.wait_for_selector(".loading__main", state="hidden", timeout=DEFAULT_TIMEOUT)
        except PlaywrightTimeoutError as e:
            raise AssertionError(f"Timeout while waiting for loading to disappear: {e}")
        except Exception as e:
            raise Exception(f"Failed while waiting for loading to disappear: {e}")
            
    def get_random_number(self, value) -> int:
        try:
            return random.randint(0, value)
        except Exception as e:
            raise Exception(f"Failed to generate random number: {e}")
