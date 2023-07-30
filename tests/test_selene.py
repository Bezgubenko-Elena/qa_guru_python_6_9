import os
from selene import browser
from selene import have


def test_success_registration(browser_open):
    browser.open('/eroshenkoam/allure-example')
    browser.element('[.header-search-button]').type('eroshenkoam/allure-example').press_enter()
    browser.all('data-testid="results-list" class="Box-sc-g0xbh4-0 hKtuLA"').element_by(have.exact_text('/eroshenkoam/allure-example')).click()

    browser.element('#href="/eroshenkoam/allure-example"').click()
    browser.element('[id="js-issues-search"]').type('81').press_enter()
