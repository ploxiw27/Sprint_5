import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from locators import Locators
from tests.conftest import driver, start_from_main_not_login

class TestSectionBunsChek:
    def test_section_buns_chek(self, start_from_login_page):
        driver = start_from_login_page

        # Клик на соусы
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.INSCRIPTION_SAUSE)).click()

        # Клик булки
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.INSCRIPTION_BUNS)).click()

        # Проверка что раздел стал активным
        new_element = WebDriverWait(driver, 12).until(EC.presence_of_element_located(Locators.SECTION_BUNS))
        assert new_element.is_displayed()

        # Проверка активной вкладки Булки
        activ_tab = WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.SECTION_BUNS))
        assert "Булки" in activ_tab.text


class TestSectionToppingCheck:
    def test_section_topping_check(self, start_from_login_page):
        driver = start_from_login_page

        # Клик начинка
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.SECTION_FILLINGS)).click()

        # Проверка что раздел активный
        new_element = WebDriverWait(driver, 12).until(EC.presence_of_element_located(Locators.SECTION_FILLINGS))

        # Проверка активной вкладки Начинки
        activ_tab = WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.SECTION_FILLINGS))
        assert "Начинки" in activ_tab.text


class TestSectionSauceCheck:
    def test_section_sauce_check(self, start_from_login_page):
        driver = start_from_login_page

        # Клик соус
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.SECTION_FILLINGS)).click()

        # Проверка что раздел активный
        new_element = WebDriverWait(driver, 12).until(EC.presence_of_element_located(Locators.SECTION_SAUSE))

        # Проверка активной вкладки Соус
        activ_tab = WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.SECTION_SAUSE))
        assert "Соус" in activ_tab.text