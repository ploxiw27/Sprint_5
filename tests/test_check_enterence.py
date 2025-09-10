from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from data import Credential
from locators import Locators


class TestCheckExitButton:

    def test_check_login_out(self, start_from_login_page):
        driver = start_from_login_page

        # Ожидание загрузки страницы
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.INSCRIPTION_BUNS))

        # Клик "Личный кабинет"
        driver.find_element_by_xpath(Locators.PERSONAL_AREA_BUTTON).click()
        # Загрузка профиль
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.INSCRIPTION_PROFILE))

        # Клик кнопка "Выход"
        driver.find_element_by_xpath(Locators.EXIT_BUTTON).click()

        # Переход на страницу входа
        WebDriverWait(driver, 12).until(EC.url_to_be(login_site))

        # Проверка УРЛ страницы после выхода
        assert driver.current_url == login_site

class TestBigButton:

    def test_check_enterence_by_big_button(self, start_from_site_not_login):
        driver = start_from_site_not_login

        # Клик "Войти в аккаунт"
        driver.find_element(*Locators.INSCRIPTION_ENTRANCE_BUTTON).click()

        # Поиск полей и авторизация
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credential.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credential.password)
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()

        # Ожидание перехода на страницу личного кабинета
        WebDriverWait(driver, 12).until(EC.url_to_be(main_site))

        # Попали на основную страницу
        assert driver.current_url == main_site


class TestRegisterCheck:

    def test_login_pass_recovery(self, start_from_page_recovery):
        driver = start_from_page_recovery

        # Ожидание загрузки страницы
        WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.INSCRIPTION_BUNS))

        # Переход на главную страницу сайта
        assert driver.current_url == main_site

class TestEntranceFromRecoveryCheck:
    def test_button_inscription_login(self, start_from_main_not_login):
        driver = start_from_main_not_login

        # Клик кнопка "Зарегистрироваться"
        driver.find_elements(*Locators.INSCRIPTION_LOGIN).click()

        # Клик "Войти"
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()

        # Поиск полей и авторизация
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credential.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credential.password)
        driver.find_element(*Locators.ENTRANCE_BUTTON).click()

        # Ожидание перехода на главную страницу ЛК
        WebDriverWait(driver, 12).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


