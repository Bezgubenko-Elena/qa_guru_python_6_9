from selene import browser
from selene import by, be
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ebezgubenko")
@allure.feature("Поиск issue в репозитории")
@allure.story("Тест с декоратором")
@allure.link("https://github.com", name="Testing")
def test_search_in_github(browser_details):
    open_main_page('https://github.com')
    search_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    go_to_issues()
    should_issue(81)


@allure.step("Открываем главую страницу GitHub")
def open_main_page(url):
    browser.open(url)


@allure.step("Ищем репозиторий {name_repo}")
def search_repository(name_repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys(name_repo)
    browser.element("#query-builder-test").submit()


@allure.step("Переходим по ссылке в репозиторий {name_repo}")
def go_to_repository(name_repo):
    browser.element(by.link_text(name_repo)).click()


@allure.step("Переходим на вкладку issues")
def go_to_issues():
    browser.element('#issues-tab').click()


@allure.step("Проверяем наличие issue {number_issue}")
def should_issue(number_issue):
    browser.element(by.partial_text("#" + str(number_issue))).should(be.visible)
