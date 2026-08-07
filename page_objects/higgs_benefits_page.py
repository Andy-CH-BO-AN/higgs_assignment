from selenium.webdriver.common.by import By

from utils.page_base import PageBase


class HiggsBenefitsPage(PageBase):
    title_benefits = (By.XPATH, "//h2[text()='Higgs 的員工福利']")

    def is_loaded(self):
        return self.find_element(self.title_benefits, clickable=False).is_displayed()
