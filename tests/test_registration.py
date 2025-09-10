import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from data import Credential
from generation_ep import EmailPassGeneration
from locators import Locators
from tests.conftest import driver, start_from_main_not_login


@pytest.mark.usefixtures("register_new_accaunt")
class TestRegistrationCheckNew:                       # Тест на успешную регистрацию
    def test_registration_new(self):
        driver, email, password = register_new_accaunt

        # Поиск и заполнение поля "Email"
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)

        # Поиск и заполнение поля "Пароль"
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)

        # Клик "Войти"
        driver.find_element(*Locators.INSCRIPTION_ENTRANCE_BUTTON).click()

        # Ожидание перехода на главную страницу ЛК
        WebDriverWait(driver, 12).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCreationExistingAccountCheckin:
    def test_accaunt_existing(self):
        driver = start_from_main_not_login

    # Поиск
    driver.find_element(*Locators.INSCRIPTION_LOGIN).click()

    # Поиск и заполнение поля "Имя"
    driver.find_element(*Locators.NAME_FIELD).send_keys(Credential.name)

    # Поиск и заполнение поля "Email"
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credential.email)

    # Поиск и заполнение поля "Пароль"
    driver.find_elements(*Locators.PASSWORD_FIELD).send_keys(Credential.password)

    # Клик "Зарегистрироваться"
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Ожидаем ошибку регистрации
    assert WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.INSCRIPTION_ERROR))


@pytest.mark.usefixtures("start_from_main_not_login")
class TestNoNameRegisterCheck:
    def test_no_name_register(self):
        driver = start_from_main_not_login

        # Клик "Зарегистрироваться"
        driver.find_element(*Locators.INSCRIPTION_LOGIN).click()

        # Генерация рандомных данных email и пароль
        generator = EmailPassGeneration()
        email, password = generator.generate()

        # Поиск и заполнение поля "Email"
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)

        # Поиск и заполнение поля "Пароль"
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)

        # Клик "Зарегистрироваться"
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Проверяем что остались на странице регистрации
        assert driver.currnt_url == register_site


@pytest.mark.usefixtures("start_from_main_not_login")
class TestPasswordError:
    def test_password_error(self):
        driver = start_from_main_not_login

        driver.find_element(*Locators.INSCRIPTION_LOGIN).click()

        # Поиск и заполнение поля "Имя"
        driver.find_element(*Locators.NAME_FIELD).send_keys(Credential.name)

        # Поиск и заполнение поля "Email"
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credential.email)

        # Поиск и заполнение поля "Пароль"
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credential.password_error)

        # Клик "Зарегистрироваться"
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Ожидаем ошибку некоректный пароль
        assert WebDriverWait(driver, 12).until(EC.visibility_of_element_located(Locators.INSCRIPTION_PASSWORD_ERROR))


@pytest.mark.usefixtures("start_from_main_not_login")
class TestNoPasswordCheck:
    def test_no_password(self):
        driver = start_from_main_not_login
        email = 'vadimmiloserdov28007@yandex.ru'

        driver.find_element(*Locators.INSCRIPTION_LOGIN).click()

        # Поиск и заполнение поля "Имя"
        driver.find_element(*Locators.NAME_FIELD).send_keys(Credential.name)

        # Поиск и заполнение поля "Email"
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)

        # Клик "Зарегистрироваться"
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Проверка УРЛ остаемся на странице регистрации
        assert driver.current_url == register_site

