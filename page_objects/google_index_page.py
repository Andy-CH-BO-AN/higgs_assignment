from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.page_base import PageBase


class GoogleIndexPage(PageBase):
    input_search = (By.NAME, "q")

    def search_keyword(self, keyword):
        search_box = self.find_element(self.input_search)
        search_box.clear()
        search_box.send_keys(keyword, Keys.ENTER)
