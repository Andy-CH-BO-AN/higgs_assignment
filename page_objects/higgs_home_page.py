from selenium.webdriver.common.by import By

from utils.page_base import PageBase


class HiggsHomePage(PageBase):
    title_about = (By.XPATH, "//p[text()='軟體開發客製化的最佳夥伴']")
    title_join_us = (By.XPATH, "//h3//p[text()='加入我們']")
    link_jobs = (By.XPATH, "//main//p[text()='Higgs 職缺']")
    link_benefits = (By.XPATH, "//main//p[text()='員工福利']")

    def wait_until_loaded(self):
        return self.find_element(self.title_about, clickable=False)

    def open_jobs(self):
        previous_handles = self.driver.window_handles
        self.scroll_into_view(self.link_jobs)
        self.click(self.link_jobs)
        return self.wait_for_new_window(previous_handles)

    def open_benefits(self):
        self.scroll_into_view(self.title_join_us)
        self.click(self.link_benefits)
