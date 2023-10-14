import time

from utils.page_base import PageBase
from selenium.webdriver.common.by import By


class HiggstarIndexPage(PageBase):
    title_join_us = (By.XPATH, "//h3//p[text()='加入我們']")
    button_jobs = (By.XPATH, "//main//p[text()='Higgs 職缺']")
    benefit = (By.XPATH, "//main//p[text()='員工福利']")
    title_about = (By.XPATH, "//p[text()='軟體開發客製化的最佳夥伴']")
    element = None

    def go_to_title(self):
        self.element = self.find_element(self.title_about)
        self.scroll_down()
        self.find_element(self.title_join_us)

    def click_jobs(self):
        self.find_element(self.button_jobs).click()

    def click_benefit_page(self):
        self.scroll_to_the_element(self.element)
        time.sleep(1)
        self.find_element(self.benefit).click()
