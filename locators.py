from selenium.webdriver.common.by import By

class Locators:

    # Главная страница кнопка "Войти в аккаунт"
    LOG_IN_ACCAUNT = (By.XPATH, "//button[text() = 'Войти в аккаунт']")

    # Логотип сайта на главной странице
    LOGO = (By.XPATH, "//header/nav/div")

    # Выход из личного кабинета
    EXIT_BUTTON = (By.XPATH, ".//button[contains(), 'Выход')]")

    # Профиль
    INSCRIPTION_PROFILE = (By.XPATH, '//a[@href="/account/profile"]')

    # Булки
    INSCRIPTION_BUNS = (By.XPATH, './/span[contains(text(), "Булки")]')

    # Раздел булки
    SECTION_BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')

    # Кнопка "Личный Кабинет"
    PERSONAL_AREA_BUTTON = (By.XPATH, './/p[contains(text(), "Личный Кабинет")]')

    # Соусы
    INSCRIPTION_SAUSE = (By.XPATH, './/span[contains(text(), "Соусы")]')

    # Раздел соусы
    SECTION_SAUSE = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')

    # Зарегистрироваться
    INSCRIPTION_LOGIN = (By.CLASS_NAME, "Auth_link__1f0lj")

    # Начинки
    INSCRIPTION_TOPPING = (By.XPATH, './/span[contains(text(), "Начинки")]')

    # Раздел с начинками
    SECTION_TOPPING_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')

    # Такой пользователь уже существует
    INSCRIPTION_ERROR = (By.XPATH, './/p[contains(text(), "Такой пользователь уже существует")]')

    # Некорректный пароль
    INSCRIPTION_PASSWORD_ERROR = (By.XPATH, '//div[contains(@class, "input_status_error")]')

    # Кнопка "Восстановить пароль"
    RESTORE_PASSWORD_BUTTON = (By.XPATH, './/a[@href="/forgot-password"]')

    # Надпись кнопка "Войти"
    INSCRIPTION_ENTRANCE_BUTTON = (By.XPATH, './/a[@href="login"]')

    # "Войти"
    ENTRANCE_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')]")

    # "Оформить заказ"
    ORDER_ARRANGE_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")

    # Зарегистрироваться
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

    # Конструктор
    CONSTACTION_BUTTON = (By.XPATH, ".//a[@href='/']")

    # Поле "Имя"
    NAME_FIELD = (By.XPATH, "//div[label[contains(text(), 'Имя')]]//input")

    # Поле "Email"
    EMAIL_FIELD = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")

    # Поле "Пароль"
    PASSWORD_FIELD = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")