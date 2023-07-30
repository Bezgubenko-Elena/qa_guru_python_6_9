from selene import browser
from selene import by, be
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ebezgubenko")
@allure.feature("Поиск issue в репозитории")
@allure.story("Тест с лямбда шагами")
@allure.link("https://github.com", name="Testing")
def test_search_in_github(browser_details):
    with allure.step("Открываем главую страницу GitHub"):
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий с текстом eroshenkoam/allure-example"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Переходим по ссылке в репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим на вкладку issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие issue с текстом '81'"):
        browser.element(by.partial_text("#81")).should(be.visible)
