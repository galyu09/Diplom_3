from selenium.webdriver.common.by import By


class SetPasswordPageLocators:

    #  Заголовок Восстановление пароля
    PASSWORD_SET_HEADER = (By.XPATH, '//h2[text() = "Восстановление пароля"]')
    # Поле ввода email
    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="name"]')

    #  Кнопка Восстановить
    PASSWORD_RESET_BUTTON = (By.XPATH, '//button[text() = "Восстановить"]')

