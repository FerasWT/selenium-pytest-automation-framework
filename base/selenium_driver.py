from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find_element(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_input(self,locator,text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def upload(self,locator,path):

        by, value = locator
        self.driver.find_element(by, value).send_keys(path)

    def select_text(self,locator,text):
        Select(self.wait.until(EC.presence_of_element_located(locator))).select_by_visible_text(text)

    def is_text_present(self,text):
        return text in self.driver.page_source
