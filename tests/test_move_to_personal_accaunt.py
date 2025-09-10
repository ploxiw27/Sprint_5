import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from data import Credential
from generation_ep import EmailPassGeneration
from locators import Locators
from tests.conftest import driver, start_from_main_not_login

class TestTransitByConstructor:
    def test_transit_by_constructor(self, start_from_main_page):
        driver = start_from_main_page

        # Ожидаем переход на главную страницу
        WebDriverWait(driver, 12).until(EC.url_to_be(main_site))

        # Клик "Личный Кабинет"
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()

        # Ожидание загрузки страницы с надписью конструктор
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTACTION_BUTTON))

        # Клик "Конструктор"
        driver.find_element(*Locators.CONSTACTION_BUTTON).click()

        # Ожидаем переход на главную страницу
        WebDriverWait(driver, 12).until(EC.url_to_be(main_site))

        # Проверка должны попасть на основную страницу
        assert driver.current_url == main_site


class TestTransitByLogo:
    def test_transit_by_logo(self, start_from_main_page):
        driver = start_from_main_page

        # Ожидаем загрузки профиля
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.PERSONAL_AREA_BUTTON))

        # Клик "Личный Кабинет"
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()

        # Ожидание загрузки профиля
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.INSCRIPTION_PROFILE))

        # Клик на логотип
        driver.find_element(*Locators.LOGO).click()

        # Ожидаем переход на главную страницу
        WebDriverWait(driver, 12).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


class TestProfilePageCheck:
    def test_transit_before_profile(self, start_from_login_page):
        driver = start_from_login_page

        # Ожидаем загрузки "Булки"
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.INSCRIPTION_BUNS))

        # Клик личный кабинет
        driver.find_element(*Locators.PERSONAL_AREA_BUTTON).click()

        # Ожидаем переход на страницу профиля
        WebDriverWait(driver, 12).until(EC.url_to_be(profile_site))

        assert driver.current_url == profile_site