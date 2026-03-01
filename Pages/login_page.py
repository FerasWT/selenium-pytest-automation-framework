from selenium.webdriver.common.by import By
from automation.base.base_page import BasePage

class LoginPage(BasePage):

    SIGN_IN = (By.XPATH, "//button[contains(text(),'Sign In')]")
    EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD = (By.XPATH, "//label[contains(text(),'Password')]/following-sibling::input")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@type,'submit')]")
    MY_COURSES = (By.XPATH, "//div[contains(text(),'My Courses')]")


    def enter_email(self,email):
        self.type_input(self.EMAIL,email)

    def enter_password(self,password):
        self.type_input(self.PASSWORD,password)

    def click_signIn(self):
        self.click_element(self.SIGN_IN)

    def click_submit_button(self):
        self.click_element(self.SUBMIT_BUTTON)

