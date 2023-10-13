import logging
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import allure
from allure_commons.types import AttachmentType


@pytest.fixture(scope="function")
def driver():
    # set log
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # set driver
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
