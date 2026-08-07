import logging
import os
from dataclasses import dataclass

import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver


if "ENV" in os.environ:
    load_dotenv(os.environ["ENV"])
else:
    load_dotenv()


@dataclass(frozen=True)
class Domains:
    google: str
    higgs: str


def _required_env(name):
    value = os.getenv(name)
    if not value:
        pytest.fail(f"Required environment variable is missing: {name}")
    return value


@pytest.fixture(scope="session")
def domains():
    return Domains(
        google=_required_env("GOOGLE_DOMAIN"),
        higgs=_required_env("HIGGS_DOMAIN"),
    )


@pytest.fixture(scope="function")
def driver():
    logging.getLogger().setLevel(logging.INFO)

    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS", "false").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
    try:
        yield browser
    finally:
        try:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="Final screenshot",
                attachment_type=AttachmentType.PNG,
            )
        except Exception:
            logging.exception("Unable to capture final browser screenshot")
        browser.quit()
