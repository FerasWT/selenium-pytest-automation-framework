import time
from selenium.webdriver.common.by import By
from automation.base.base_page import BasePage

class StudentPage(BasePage):

    BROWSE_COURSE = (By.XPATH,"//button[contains(text(),'Browse Courses')]")
    HOME = (By.XPATH,"//div[contains(text(),'Home')]")

    time.sleep(5)

    def click_browse_course(self):
        self.click_element(self.BROWSE_COURSE)

    def click_home(self):
        self.click_element(self.HOME)

    time.sleep(5)