from automation.base.selenium_driver import SeleniumDriver
from automation.utilities.custom_logger import get_logger
from automation.utilities.screenshot import take_screenshot
class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.log = get_logger(self.__class__.__name__)

    def capture_failure(self, name):
        path = take_screenshot(self.driver, name)
        self.log.error(f"Screenshot saved: {path}")