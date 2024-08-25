from selenium.webdriver.common.by import By


class OrdersHistoryLocators:

    # Список номеров заказов в Истории
    ORDER_NUMBERS_LIST = (By.XPATH, '//*[contains(text(), "#")]')

    # Кнопка История заказов
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    # Первый заказ в истории
    FIRST_ORDER_ID = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[1]/a/div/p[1]")