from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageBase:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator, clickable=True):
        condition = (
            EC.element_to_be_clickable(locator)
            if clickable
            else EC.visibility_of_element_located(locator)
        )
        return self.wait.until(condition)

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def scroll_into_view(self, locator):
        element = self.find_element(locator, clickable=False)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )
        return element

    def wait_for_new_window(self, previous_handles):
        previous_handles = set(previous_handles)
        self.wait.until(lambda driver: len(driver.window_handles) > len(previous_handles))
        return next(
            handle
            for handle in self.driver.window_handles
            if handle not in previous_handles
        )
