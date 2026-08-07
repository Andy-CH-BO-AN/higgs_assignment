import allure

from page_objects.google_index_page import GoogleIndexPage
from page_objects.google_search_page import GoogleSearchPage
from page_objects.higgs_benefits_page import HiggsBenefitsPage
from page_objects.higgs_home_page import HiggsHomePage


@allure.title("Search Higgs from Google and verify jobs and benefits")
def test_higgs_website(driver, domains):
    google_index_page = GoogleIndexPage(driver)
    google_search_page = GoogleSearchPage(driver)
    higgs_home_page = HiggsHomePage(driver)
    higgs_benefits_page = HiggsBenefitsPage(driver)

    driver.get(domains.google)
    google_index_page.search_keyword("higgs tec. inc.")
    google_search_page.open_website(domains.higgs)
    higgs_home_page.wait_until_loaded()

    home_window = driver.current_window_handle
    jobs_window = higgs_home_page.open_jobs()
    assert jobs_window != home_window, "Jobs link did not open a new browser window"

    driver.switch_to.window(home_window)
    assert driver.current_url.rstrip("/") == domains.higgs.rstrip("/"), (
        f"Unexpected Higgs URL: {driver.current_url}"
    )

    higgs_home_page.open_benefits()
    assert higgs_benefits_page.is_loaded(), "Benefits page title is not visible"
