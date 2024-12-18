from selenium import webdriver
from classUI import search_main
import allure


@allure.epic("poisk")
@allure.severity(severity_level="critical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на кирилице")
@allure.feature('Тест 4')
def test_search_kiril():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
        kiril = search_main(driver)
    with allure.step("Сделать поиск на кирилице"):
        kiril.search_kiril()
    with allure.step("Нажать на лупу"):
        kiril.click_loupe()
    with allure.step("Результат поиска не пустой"):
        assert kirillica is not None
    with allure.step("Закрыть браузер"):
        kiril._driver.quit()

@allure.epic("poisk")
@allure.severity(severity_level="critical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на латинице")
@allure.feature('Тест 4')
def test_search_lat():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
        latinnica = search_main(driver)
    with allure.step("Сделать поиск на латинце"):
        latinnica.search_lat()
    with allure.step("Нажать на лупу"):
        latinnica.click_loupe()
    with allure.step("Результат поиска не пустой"):
        assert latinnica is not None
    with allure.step("Закрыть браузер"):
        latinnica._driver.quit()


@allure.epic("poisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск  фильма, сериала и т.п. по году выпуска")
@allure.description("Сделать поиск  фильма, сериала и т.п. по году выпуска")
@allure.feature('Тест 4')
def test_search_reliz():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
        year = search_main(driver)
    with allure.step("Нажать на расширеный поиск"):
        year.full_search()
    with allure.step("Ввести год создание фильма"):
        year.search_reliz()
    with allure.step("Нажать на поиск"):
        year.click_search()
    with allure.step("Результат поиска не пустой"):
        assert year is not None
    with allure.step("Закрыть браузер"):
        year._driver.quit()

@allure.epic("poisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п. по году рождения")
@allure.description("Сделать поиск актера, режиссера, оператора и т.п. по году рождения")
@allure.feature('Тест 4')
def test_search_birthday():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
        year = search_main(driver)
    with allure.step("Нажать на расширеный поиск"):
        year.full_search()
    with allure.step("Ввести год рождения актера"):
        year.search_birthday()
    with allure.step("Нажать на поиск"):
        year.click_search()
    with allure.step("Результат поиска не пустой"):
        assert year is not None
    with allure.step("Закрыть браузер"):
        year._driver.quit()

@allure.epic("poisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п. по месту рождения")
@allure.description("Сделать поиск актера, режиссера, оператора и т.п. по месту рождения")
@allure.feature('Тест 4')
def test_search_birthplace():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
        year = search_main(driver)
    with allure.step("Нажать на расширеный поиск"):
        year.full_search()
    with allure.step("Ввести место рождения актера"):
        year.search_birthplace()
    with allure.step("Нажать на поиск"):
        year.click_search()
    with allure.step("Результат поиска не пустой"):
        assert year is not None
    with allure.step("Закрыть браузер"):
        year._driver.quit()