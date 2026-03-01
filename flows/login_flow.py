from automation.Pages.login_page import LoginPage
from automation.utilities.screenshot import take_screenshot


class LoginFlow:

    def __init__(self, driver, logger, test_name):
        self.login_page = LoginPage(driver)
        self.driver = driver
        self.log = logger
        self.test_name = test_name

    def login(self, email, password):
        try:
            self.log.info("Starting login flow")

            self.login_page.click_signIn()
            self.login_page.enter_email(email)
            self.login_page.enter_password(password)
            self.login_page.click_submit_button()

            self.log.info("Login successful")

        except Exception as e:
            screenshot = take_screenshot(self.driver, self.test_name)
            self.log.error("Login flow FAILED", exc_info=True)
            self.log.error(f"Screenshot saved at: {screenshot}")
            raise