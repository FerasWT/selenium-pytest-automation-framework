import time
from automation.Pages.course_page import CoursePage
from automation.utilities.screenshot import take_screenshot


class CourseFlow:

    def __init__(self, driver, logger, test_name):
        self.course_page = CoursePage(driver)
        self.driver = driver
        self.log = logger
        self.test_name = test_name

    def create_course(
        self, path, title, category_d, description,
        price, discount, status, lesion_title, vedio_path
    ):
        try:
            self.log.info("Creating course")
            time.sleep(5)
            self.course_page.click_new_course()
            self.course_page.upload_image(path)
            self.course_page.type_title(title)
            self.course_page.select_category(category_d)
            self.course_page.type_description(description)
            self.course_page.type_price(price)
            self.course_page.type_discount(discount)
            self.course_page.type_status(status)
            self.course_page.click_add_lesson()
            self.course_page.click_lession_title(lesion_title)
            self.course_page.lesion_description(description)
            self.course_page.upload_vedio(vedio_path)
            self.course_page.click_publish_course()

            self.log.info("Course created successfully")
            time.sleep(3)

        except Exception as e:
            screenshot = take_screenshot(self.driver, self.test_name)
            self.log.error("Course creation FAILED", exc_info=True)
            self.log.error(f"Screenshot saved at: {screenshot}")
            raise