from locators.orders_history_locators import OrdersHistoryLocators
from pages.base_page import BasePage
import allure


class OrdersHistoryPage(BasePage):
    @allure.step('Получаем список заказов пользователя в Истории заказов')
    def get_orders_history_list(self):
        orders_list = list(order_number.text for order_number in self.get_visible_elements(
            OrdersHistoryLocators.ORDER_NUMBERS_LIST))
        return orders_list

    @allure.step('Переход на страницу "Лента заказов" тапом на заголовок')
    def move_to_orders_feed(self):
        self.wait_for_element_to_be_clickable(OrdersHistoryLocators.ORDERS_FEED_BUTTON)
        self.click_on_element(OrdersHistoryLocators.ORDERS_FEED_BUTTON)

    @allure.step('Получаем номер первого заказа из истории')
    def get_first_order_id(self):
        return self.find_element(OrdersHistoryLocators.FIRST_ORDER_ID).text

