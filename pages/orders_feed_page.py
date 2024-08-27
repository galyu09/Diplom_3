from locators.orders_feed_locators import OrdersFeedLocators
from pages.base_page import BasePage
import allure


class OrdersFeedPage(BasePage):

    @allure.step('Тап на первый заказ на странице заказов')
    def click_on_first_order_in_order_list(self):
        self.wait_for_element_to_be_clickable(OrdersFeedLocators.FIRST_ORDER_IN_ORDER_FEED)
        self.click_on_element(OrdersFeedLocators.FIRST_ORDER_IN_ORDER_FEED)

    @allure.step('Проверяем наличие модального окна с деталями заказа')
    def get_modal_with_orders_details(self):
        return self.check_element_is_displayed(OrdersFeedLocators.ORDER_DETAILS_MODAL)


    @allure.step('Ищем заказ с нужным номером в списке "В работе"')
    def get_orders_in_process(self, order_id):
        locator = self.format_locator(OrdersFeedLocators.ORDERS_IN_PROCESS, order_id)
        return self.find_element(locator, 30).text

    @allure.step('Получаем текущий счетчик заказов За все время')
    def get_current_counter(self):
        self.wait_for_visibility_of_element(OrdersFeedLocators.CURRENT_COUNTER)
        return self.find_element(OrdersFeedLocators.CURRENT_COUNTER).text

    @allure.step('Получаем текущий счетчик заказов За сегодня')
    def get_current_counter_today(self):
        self.wait_for_visibility_of_element(OrdersFeedLocators.CURRENT_COUNTER_TODAY)
        return self.find_element(OrdersFeedLocators.CURRENT_COUNTER_TODAY).text

    @allure.step('Переход на главную тапом на Конструктор')
    def go_to_main(self):
        self.wait_for_element_to_be_clickable(OrdersFeedLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(OrdersFeedLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получаем список заказов в Ленте заказов')
    def get_orders_feed_list(self):
        orders_feed_list = list(order_number.text for order_number in self.get_visible_elements(
            OrdersFeedLocators.ORDER_NUMBERS_LIST))
        return orders_feed_list

    @allure.step('Получаем текст хэдера в ленте заказов')
    def get_orders_feed_header_text(self):
        self.wait_for_visibility_of_element(OrdersFeedLocators.ORDERS_FEED_HEADER)
        return self.find_element(OrdersFeedLocators.ORDERS_FEED_HEADER).text




