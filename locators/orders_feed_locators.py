from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    # Заголовок Лента заказов
    ORDERS_FEED_HEADER = (By.XPATH, '//h1[text() = "Лента заказов"]')
    # Первый заказ в ленте заказов
    FIRST_ORDER_IN_ORDER_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    # Модальное окно с деталями заказа
    ORDER_DETAILS_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                     '"Modal_orderBox")]')
    # Список заказов В работе
    ORDERS_IN_PROCESS = (By.XPATH, '//*[contains(@class, "_orderListReady")]/li[contains(@class, "digits")]')

    # Значение счётчика "Выполнено за все время"
    CURRENT_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class, "OrderFeed_number")]')
    # Значение счётчика "Выполнено за сегодня"
    CURRENT_COUNTER_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "OrderFeed_number")]')

    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    # Список заказов В ленте
    ORDER_NUMBERS_LIST = (By.XPATH, "//*[contains(text(), '#')]")


