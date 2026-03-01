import pytest
from automation.flows.login_flow import LoginFlow
from automation.flows.course_flow import CourseFlow
from automation.flows.student_flow import StudentFlow
from automation.utilities.custom_logger import get_logger
import os
from pathlib import Path

i_mail = os.getenv("INSTRUCTOR_EMAIL")
i_password = os.getenv("INSTRUCTOR_PASSWORD")

s_mail = os.getenv("STUDENT_EMAIL")
s_password = os.getenv("STUDENT_PASSWORD")
# path = r"D:\Aotumation\Course\automation\test_data\Screenshot 2026-01-12 115516.png"
description = "Agile methodology is an iterative..."
category_s = "Tech & Coding"
title = "Agile Methodology"
price = "100"
discount = "10"
status = "Published"
lesion_title = "Introduction"

# vedio_path = r"D:\Aotumation\Course\automation\test_data\Test.mp4"



# go from automation/tests/test_course_creation.py → project root
BASE_DIR = Path(__file__).resolve().parents[2]

path = str(BASE_DIR / "automation" / "test_data" / "Screenshot 2026-01-12 115516.png")
vedio_path = str(BASE_DIR / "automation" / "test_data" / "Test.mp4")


@pytest.mark.usefixtures("driver")
class Test_course_creation:

    def test_login_flow(self, driver, request):
        logger = get_logger(__name__)
        test_name = request.node.name

        login_flow = LoginFlow(driver, logger, test_name)
        login_flow.login(i_mail, i_password)


    def test_course_creation(self, driver, request):
        logger = get_logger(__name__)
        test_name = request.node.name

        course_flow = CourseFlow(driver, logger, test_name)
        course_flow.create_course(
            path, title, category_s, description,
            price, discount, status, lesion_title, vedio_path
        )

        assert title in driver.page_source


@pytest.mark.usefixtures("driver")
class Test_student:

    def test_login_page(self, driver, request):
        logger = get_logger(__name__)
        test_name = request.node.name

        login_flow = LoginFlow(driver, logger, test_name)
        login_flow.login(s_mail, s_password)

    def test_student_page(self, driver, request):
        logger = get_logger(__name__)
        test_name = request.node.name

        student_flow = StudentFlow(driver, logger, test_name)
        student_flow.enter_student_page()