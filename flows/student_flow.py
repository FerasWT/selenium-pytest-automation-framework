import time
from automation.Pages.Student_page import StudentPage
from automation.utilities.screenshot import take_screenshot


class StudentFlow:

    def __init__(self, driver, logger, test_name):
        self.student_page = StudentPage(driver)
        self.driver = driver
        self.log = logger
        self.test_name = test_name

    def enter_student_page(self):
        try:
            self.log.info("Entering student page")
            time.sleep(5)
            self.student_page.click_browse_course()
            # time.sleep(2)
            self.student_page.click_home()
            # time.sleep(3)

            self.log.info("Student page entered successfully")

        except Exception as e:
            screenshot = take_screenshot(self.driver, self.test_name)

            self.log.error("Student flow FAILED", exc_info=True)
            self.log.error(f"Screenshot saved at: {screenshot}")

            raise