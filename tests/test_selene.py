from selene import browser
from selene import by, be
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "ebezgubenko")
@allure.feature("Поиск issue в репозитории")
@allure.story("Тест на чистом selene")
@allure.link("https://github.com", name="Testing")
def test_search_in_github(browser_details):
    browser.open('https://github.com')

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text("#81")).should(be.visible)
