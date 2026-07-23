from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
from config.settings import DEFAULT_TIMEOUT, LOGIN_TIMEOUT
from pages.locators.elements import BaseElements
import random
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = BaseElements(page)

    def sleep(self, seconds: int):
        try:
            self.page.wait_for_timeout(seconds * 1000)
        except Exception as e:
            raise Exception(f"Failed to sleep, Because of {e}")
    
    def take_screenshot(self, photo_name):
        allure.attach(
            self.page.screenshot(),
            name=f"{photo_name}",
            attachment_type=allure.attachment_type.PNG
        )


    def click_expect(self, locator, expected_value=None, reclick=False):
        try:
            locator.wait_for(state="visible", timeout=DEFAULT_TIMEOUT)
            locator.scroll_into_view_if_needed(timeout=DEFAULT_TIMEOUT)
            locator.click(timeout=DEFAULT_TIMEOUT)
            self.elements.icon_loading.wait_for(state="hidden", timeout=DEFAULT_TIMEOUT)

        except PlaywrightTimeoutError as e:
            raise TimeoutError(f"Failed to find element, Because {e}")
        except Exception as e:
            raise Exception(f"Failed to click, Because {e}")

        if expected_value is not None:
            try:
                expected_value.wait_for(state='visible', timeout=DEFAULT_TIMEOUT)
            except PlaywrightTimeoutError as e:
                if reclick:
                    self.click_expect(locator, expected_value, False)
                else:
                    raise TimeoutError(f"Expect element timed out, Because of {expected_value}: {e}")
            except Exception as e:
                raise Exception(f"Click passed, but fail to expected element {expected_value} is not visible: {e}")

    def wait_fill(self, locator, value: str):
        try:
            locator.wait_for(state="visible", timeout=DEFAULT_TIMEOUT)
            locator.fill(value)
        except Exception as e:
            raise Exception(f"Failed to fill value, Because of {e}")

    def wait_loading_disapper(self):
        try:
            self.page.wait_for_selector(".loading__main", state="hidden", timeout=DEFAULT_TIMEOUT)
            self.sleep(1)
        except PlaywrightTimeoutError as e:
            raise TimeoutError(f"Waiting for loading to disappear timed out, Because of {e}")
        except Exception as e:
            raise Exception(f"Failed while waiting for loading to disappear, Because of {e}")
            
    def get_random_number(self, value) -> int:
        try:
            return random.randint(0, value)
        except Exception as e:
            raise Exception(f"Failed to generate random number: {e}")
