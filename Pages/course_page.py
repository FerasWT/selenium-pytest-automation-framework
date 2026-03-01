
from selenium.webdriver.common.by import By

from automation.base.base_page import BasePage




class CoursePage(BasePage):

    NEW_COURSE = (By.XPATH, "//button[contains(text(),'Upload Course')]")
    ADD_COURSE = (By.XPATH, "//button[contains(text(),'+ New Course')]")
    UPLOAD_IMAGE = (By.XPATH, "//input[contains(@accept,'image/*')]")
    TITLE = (By.XPATH, "//label[contains(text(),'Course Title')]/following-sibling::input")
    DROPDOWN_CATEGORY = (By.XPATH, "//label[contains(text(),'Category')]/following-sibling::div/select")
    DESCRIPTION = (By.XPATH, "//label[contains(text(),'Description *')]/following-sibling::textarea")
    PRICE = (By.XPATH,"//label[contains(text(),'Price')]/following-sibling::div/input")
    DISCOUNT = (By.XPATH,"//label[contains(text(),'Discount %')]/following-sibling::div/input")
    STATUS= (By.XPATH,"//label[contains(text(),'Status')]/following-sibling::select")
    ADD_LESION= (By.XPATH, "//button[contains(text(),'+ Add Lesson')]")
    LESION_TITLE = (By.XPATH, "//label[contains(text(),'Lesson Title ')]/following-sibling::input")
    LESION_DES = (By.XPATH,"//label[contains(text(),'Description')]/following-sibling::textarea[@placeholder='What will students learn in this lesson?']")
    SAVE_BTN = (By.XPATH, "//button[contains(text(),'Publish Course')]")
    UV = (By.XPATH,"//input[contains(@accept,'video/*')]")



    def click_new_course(self):
        self.click_element(self.NEW_COURSE)

    def upload_image(self,path):
        self.upload(self.UPLOAD_IMAGE,path)

    def type_title(self,title):
        self.type_input(self.TITLE,title)

    def select_category(self,category_d):
        self.select_text(self.DROPDOWN_CATEGORY,category_d)

    def type_description(self,description):
        self.type_input(self.DESCRIPTION,description)

    def type_price(self,price):
        self.type_input(self.PRICE,price)

    def type_discount(self,discount):
        self.type_input(self.DISCOUNT,discount)

    def type_status(self,status):
        self.select_text(self.STATUS,status)

    def click_add_lesson(self):
        self.click_element(self.ADD_LESION)

    def click_lession_title(self,title):
        self.type_input(self.LESION_TITLE,title)

    def lesion_description(self,description):
        self.type_input(self.LESION_DES,description)

    def upload_vedio(self,vedio_path):
        self.upload(self.UV,vedio_path)

    def click_publish_course(self):
        self.click_element(self.SAVE_BTN)


