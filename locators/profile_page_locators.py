from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Заголовок Профиль
    PROFILE_TITLE = (By.XPATH, './/a[contains(@class, "Account_link") and text()="Профиль"]')
    # Кнопка История заказов
    ORDER_HISTOTY_BUTTON = (By.XPATH, '//a[@href = "/account/order-history"][text() = "История заказов"]')

    # Кнопка Выйти
    LOGOUT_BUTTON = (By.XPATH, '//button[text() = "Выход"]')

