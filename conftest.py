import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="function")
def driver():
    # set log
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # set driver
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
