from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
from config.settings import DEFAULT_TIMEOUT
import random
import allure

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

    def click_expect(self, locator, expected_value=None, reclick=False):
        try:
            locator.wait_for(state="visible", timeout=DEFAULT_TIMEOUT)
            locator.click()
            self.page.wait_for_selector(".loading__main", state="hidden", timeout=DEFAULT_TIMEOUT)
        except PlaywrightTimeoutError as e:
            raise AssertionError(f"Failed to find this element: {e}")
        except Exception as e:
            raise Exception(f"Failed to click this element: {e}")

        if expected_value is not None:
            try:
                expect(expected_value).to_be_visible()
            except PlaywrightTimeoutError as e:
                if reclick:
                    self.click_expect(locator, expected_value, False)
                else:
                    raise AssertionError(f"Failed to find expected element: {e}")
            except Exception as e:
                raise Exception(f"Click passed, but expected element is not visible: {e}")

    def wait_fill(self, locator, value: str):
        try:
            locator.wait_for(state="visible", timeout=DEFAULT_TIMEOUT)
            locator.fill(value)
        except Exception as e:
            raise Exception(f"Failed to fill value: {e}")
        
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
