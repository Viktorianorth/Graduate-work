from selenium.webdriver.common.by import By
from config import URL_main
import allure


class search_main():

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(URL_main)
        self._driver.implicitly_wait(300)


    @allure.step("Сделать поиск на кирилице")
    def search_kiril(self):
        self._driver.find_element(By.TAG_NAME, "input").send_keys("бойцовский клуб")

    @allure.step("Нажать на лупу")
    def click_loupe(self):
        self._driver.find_element(By.XPATH, "(//*[name()='path'][@fill-rule='evenodd'])[3]").click()

    @allure.step("Сделать поиск на латинице")
    def search_lat(self):
        self._driver.find_element(By.TAG_NAME, "input").send_keys("fight club")

    @allure.step("Нажать на расширенный поиск")
    def full_search(self):
        self._driver.find_element(By.CSS_SELECTOR, ".c1wHrX0nYR4Zk_nNlgHG").click()

    @allure.step("Сделать поиск по году создание фильма")
    def search_reliz(self):
        self._driver.find_element(By.ID, "year").send_keys("1997")

    @allure.step("Нажать на поиск")
    def click_search(self):
        self._driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/input[11]").click()

    @allure.step("Сделать поиск по году рождения актера")
    def search_birthday(self):
        self._driver.find_element(By.ID, "birthday").send_keys("1995")

    @allure.step("Сделать поиск по месту рождения актера")
    def search_birthplace(self):
        self._driver.find_element(By.XPATH, "(//input[@id='location'])[1]").send_keys("Ирландия")