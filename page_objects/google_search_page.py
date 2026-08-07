from selenium.webdriver.common.by import By

from utils.page_base import PageBase


class GoogleSearchPage(PageBase):
    def open_website(self, website):
        normalized_url = website.rstrip("/")
        result_link = (
            By.XPATH,
            f"//a[starts-with(@href, '{normalized_url}')]",
        )
        self.click(result_link)
