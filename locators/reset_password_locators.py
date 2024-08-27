from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    # Заголовок Восстановление пароля
    RESET_PASSPORT_HEADER = (By.XPATH, '//h2[text() = "Восстановление пароля"]')
    # Поле "Пароль"
    NEW_PASSWORD_FIELD = (By.XPATH, '//input[@name="Введите новый пароль"]')
    # Кнопка показать/скрыть пароль
    EYE_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    # Элемент div, в котором лежит поле "Введите новый пароль"
    NEW_PASSWORD_ELEMENT_DIV = (By.XPATH, '//div[input[@name="Введите новый пароль"]]')

