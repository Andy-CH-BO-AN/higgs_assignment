from utils.page_base import PageBase
from selenium.webdriver.common.by import By


class GoogleIndexPage(PageBase):
    input_search = (By.ID, "APjFqb")
    button_search = (By.XPATH, '//input[@value="Google 搜尋"]')

    def search_keyword(self, keyword):
        self.find_element(self.input_search).send_keys(keyword)
        self.find_element(self.button_search).click()
