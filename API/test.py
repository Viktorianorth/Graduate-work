from API.unit import Poisk
from config import URL_kinopoisk, token
import allure


poisk = Poisk(URL_kinopoisk)
token = token


@allure.epic("poisk")
@allure.severity(severity_level="critical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на кирилице")
@allure.feature('Тест 3')
def test_search_kiril():
    params = {'page': '1', 'limit': '3', 'query': 'Роберт Дауни мл.'}
    headers = {'X_API_KEY': token}
    kiril = poisk.search_kiril(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert kiril is not None


@allure.epic("poisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. по id")
@allure.feature('Тест 3')
def test_search_by_id():
    params = {'id': '10096'}
    headers = {'X_API_KEY': token}
    by_id = poisk.search_by_id(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert by_id is not None


@allure.epic("poisk")
@allure.severity(severity_level="critical")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. на латинице")
@allure.feature('Тест 3')
def test_search_lat():
    params = {'page': '1', 'limit': '3', 'query': 'Lee Kwang-Soo'}
    headers = {'X_API_KEY': token}
    lat = poisk.search_lat(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert lat is not None


@allure.epic("poisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. по году рождения")
@allure.feature('Тест 3')
def test_search_by_year():
    params = {'page': '1', 'limit': '3', 'birthday': '01.01.1995-31.12.1995'}
    headers = {'X_API_KEY': token}
    by_year = poisk.search_by_year(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert by_year is not None


@allure.epic("poisk")
@allure.severity(severity_level="normal")
@allure.title("Поиск актера, режиссера, оператора и т.п.")
@allure.description("Сделать поиск  ФИО актера, режиссера, оператора и т.п. по по гендеру(Женский, Мужской)")
@allure.feature('Тест 3')
def test_search_by_gender():
    params = {'page': '1', 'limit': '3', 'sex': 'Мужской'}
    headers = {'X_API_KEY': token}
    by_gender = poisk.search_by_gender(headers=headers, params=params)
    with allure.step("Результат поиска не пустой"):
        assert by_gender is not None
