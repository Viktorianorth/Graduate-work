from config import URL_kinopoisk, token
import requests
import allure

X_API_KEY = token


class Poisk:
    def __init__(self, url=URL_kinopoisk):
        self.url = url

    @allure.step("поиск  ФИО актера, режиссера, оператора и т.п. на кирилице")
    def search_kiril(self, headers, params):
        params = {'page': '1', 'limit': '3', 'query': 'Роберт Дауни мл.'}
        headers = {'X_API_KEY': token}
        response = requests.get(
            self.url + '/person' + '/search ', params=params, headers=headers)
        return response.json()

    @allure.step("поиск актера, режиссера, оператора и т.п. по id")
    def search_by_id(self, headers, params):
        params = {'id': '10096'}
        headers = {'X_API_KEY': token}
        response = requests.get(
            self.url + '/person', params=params, headers=headers)
        return response.json()

    @allure.step("поиск  ФИО актера, режиссера, оператора и т.п. на латинице")
    def search_lat(self, headers, params):
        params = {'page': '1', 'limit': '3', 'query': 'Lee Kwang-Soo'}
        headers = {'X_API_KEY': token}
        response = requests.get(
            self.url + '/person' + '/search ', params=params, headers=headers)
        return response.json()

    @allure.step("поиск актера, режиссера, оператора и т.п. по году рождения")
    def search_by_year(self, headers, params):
        params = {
            'page': '1', 'limit': '3', 'birthday': '01.01.1995-31.12.1995'}
        headers = {'X_API_KEY': token}
        response = requests.get(
            self.url + '/person', params=params, headers=headers)
        return response.json()

    @allure.step("поиск актера, режиссера, оператора и т.п. по гендеру(Женский, Мужской)")
    def search_by_gender(self, headers, params):
        params = {'page': '1', 'limit': '3', 'sex': 'Мужской'}
        headers = {'X_API_KEY': token}
        response = requests.get(
            self.url + '/person', params=params, headers=headers)
        return response.json()