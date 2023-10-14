import logging
import os
from page_objects.google_index_page import GoogleIndexPage
from page_objects.google_search_page import GoogleSearchPage
from page_objects.higgstar_index_page import HiggstarIndexPage
from page_objects.higgster_benefit_page import HiggstarBenefitPage
import allure


@allure.title("categories")
def test_higgstar_website(driver):
    google_index_page = GoogleIndexPage(driver)
    google_search_page = GoogleSearchPage(driver)
    higgstar_index_page = HiggstarIndexPage(driver)
    higgster_benefit_page = HiggstarBenefitPage(driver)

    google_url = os.getenv('GOOGLE_DOMAIN')
    higgstar_website = os.getenv('HIGGS_DOMAIN')
    driver.get(google_url)

    google_index_page.search_keyword("higgs tec. inc.")
    google_search_page.click_website(higgstar_website)
    higgstar_index_page.go_to_title()
    higgstar_index_page.click_jobs()

    parent = driver.window_handles[0]
    driver.switch_to.window(parent)
    assert driver.current_url == higgstar_website, \
        (logging.info(f"current_url: {driver.current_url} != higgstar_website: {higgstar_website}"))

    higgstar_index_page.click_benefit_page()
    higgster_benefit_page.check_benefit_title()
