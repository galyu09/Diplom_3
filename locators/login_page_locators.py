from selenium.webdriver.common.by import By


class LoginPageLocators:

    # Кнопка востановить пароль на странице /login
    SET_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # Заголовок Вход на странице Личный кабинет
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[contains(text(),'Вход')]")

    # поле ввода email
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    # поле ввода пароля
    PASSWORD_FIELD = (By.XPATH, './/input[@name="Пароль"]')
    # поле ввода пароля
    ENTER_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    # Кнопка История заказов
    ORDERS_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')







