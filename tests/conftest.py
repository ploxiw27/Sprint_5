import pytest
from selenium import webdriver
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from getpass import EmailPassGeneration
from data import Credential


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def start_from_login_page(driver):
    login_page = login_site
    driver.get(login_page)

    # Ищем поля для авторизации и входим
    driver.find_elements(*Locators.EMAIL_FIELD).send_keys(Credential.email)
    driver.find_elements(*Locators.PASSWORD_FIELD).send_keys(Credential.password)
    driver.find_elements(*Locators.ENTRANCE_BUTTON).click()

    return driver

@pytest.fixture()
def start_from_page_recovery(driver):
    login_page = login_site
    driver.get(login_page)

    # Клик по ссылке "Восстановить пароль"
    driver.find_elements(*Locators.RESTORE_PASSWORD_BUTTON).click()

    # Загрузка "Войти"
    WebDriverWait(driver, 6).until(EC, visibility_of_element_located(Locators.INSCRIPTION_ENTRANCE_BUTTON))

    # Клик по "Войти"
    driver.find_elements(*Locators.INSCRIPTION_ENTRANCE_BUTTON).click()

    # Ищем поля проходим авторизацию
    driver.find_elements(*Locators.EMAIL_FIELD).send_keys(Credential.email)
    driver.find_elements(*Locators.PASSWORD_FIELD).send_keys(Credential.password)
    driver.find_elements(*Locators.ENTRANCE_BUTTON).click()


    return driver

@pytest.fixture()
def start_from_main_page(driver):
    main_page = main_site
    driver.get(main_page)

    # Клик "Личный Кабинет"
    driver.find_elements(*Locators.PERSONAL_AREA_BUTTON).click()

    # Клик "Войти"
    driver.find_elements(*Locators.ENTRANCE_BUTTON).click()

    # Поиск полей авторизация
    driver.find_elements(*Locators.EMAIL_FIELD).send_keys(Credential.email)
    driver.find_elements(*Locators.PASSWORD_FIELD).send_keys(Credential.password)
    driver.find_elements(*Locators.ENTRANCE_BUTTON).click()

    return driver

@pytest.fixture
def start_from_register_page (driver):
    register_page = register_site
    driver.get(register_page)

    # Находим "Войти"
    driver.find_element(*Locators.INSCRIPTION_ENTRANCE_BUTTON).click()

    # Поиск и заполнение полей авторизации
    driver.find_elements(*Locators.EMAIL_FIELD).send_keys(Credential.email)
    driver.find_elements(*Locators.PASSWORD_FIELD).send_keys(Credential.password)
    driver.find_elements(*Locators.ENTRANCE_BUTTON).click()

    return driver

@pytest.fixture
def start_from_main_not_login(driver):
    login_page = login_site
    driver.get(login_page)

    return driver

@pytest.fixture
def start_from_site_not_login(driver):
    login_page = main_site
    driver.get(login_page)

    return driver

@pytest.fixture
def register_new_accaunt(driver):
    login_page = login_site
    driver.get(login_page)

    # Клик на надпись "Зарегистрироваться"
    driver.find_element(*Locators.INSCRIPTION_LOGIN).click()

    # Сгенерировать email и пароль
    generator = EmailPassGeneration()
    email, password = generator.generate()

    # Поиск и заполнение поля "Имя"
    driver.find_element(*Locators.NAME_FIELD).send_keys(Credential.name)

    # Поиск и заполнение поля "Email"
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)

    # Поиск и заполнение поля "Пароль"
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)

    # Клик кнопки "Зарегистрироваться"
    driver.find_elements(*Locators.INSCRIPTION_LOGIN).click()

    # Загрузка Войти
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ENTRANCE_BUTTON))

    return driver, email, password