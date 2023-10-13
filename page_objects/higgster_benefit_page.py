from utils.page_base import PageBase
from selenium.webdriver.common.by import By


class HiggstarBenefitPage(PageBase):
    title_higgs_benefit = (By.XPATH, "//h2[text()='Higgs 的員工福利']")

    def check_benefit_title(self):
        self.find_element(self.title_higgs_benefit)
