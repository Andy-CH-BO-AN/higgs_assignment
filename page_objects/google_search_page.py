from utils.page_base import PageBase
from selenium.webdriver.common.by import By


class GoogleSearchPage(PageBase):
    def click_website(self, website):
        element = self.find_element((By.XPATH, f"//a[@href='{website}']"))
        element.click()
