import allure
import pytest

from locators.main_page_locators import MainPageLocators
from locators.orders_feed_locators import OrdersFeedLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from tests import data
import time


class TestOrderConstructor:
    @allure.title('Переход по кнопке Конструктор')
    @allure.description('Проверка загрузки главной страницы при клике на Конструктор')
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.move_to_constructor()
        main_page.wait_for_visibility_of_element(MainPageLocators.MAIN_BURGER_HEADER)
        assert main_page.find_element(MainPageLocators.MAIN_BURGER_HEADER).text == data.Data.MAIN_BURGER_HEADER_TEXT

    @allure.title('Переход по кнопке лента Заказов')
    @allure.description('Проверяем переход на экран Ленты заказов тапом по кнопке')
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.move_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.wait_for_visibility_of_element(OrdersFeedLocators.ORDERS_FEED_HEADER)
        assert orders_feed_page.find_element(OrdersFeedLocators.ORDERS_FEED_HEADER).text == data.Data.ORDERS_FEED_HEADER_TEXT
        assert orders_feed_page.take_current_url() == data.Urls.ORDER_FEED_URL

    @allure.title('Детали ингридиента')
    @allure.description('Проверяем, что по клику на ингридиент открывается модальное окно с детальной информацией')
    def test_click_on_ingredient_move_to_modal_with_details(self, driver):
        main_page = MainPage(driver)
        ingredient_name = main_page.get_ingredient_name_by_index(0)
        main_page.click_on_ingredient(0)
        assert main_page.get_ingredient_name_in_modal() == ingredient_name

    @allure.title('Закрытие модального окна с деталями ингридиентов')
    @allure.description('Проверяем, что тапом на крестик модальное окно с деталями ингридиентов закрывается')
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient(1)
        main_page.close_popup_window()
        assert not main_page.find_ingredient_modal()

    @allure.title('Увеличение каунтера ингредиента')
    @allure.description('Проверяем, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @pytest.mark.parametrize('ingredient_index, counter', [(0, 2), (2, 1)])
    def test_ingredient_counter(self, driver, ingredient_index, counter):
        main_page = MainPage(driver)
        default_counter = main_page.get_ingredients_counter(ingredient_index)
        main_page.add_ingredient_to_order(ingredient_index)
        counter_past = main_page.get_ingredients_counter(ingredient_index)
        assert counter_past == default_counter + counter

    @allure.title('Оформление заказа залогиненным юзером')
    @allure.description('Проверка возможности оформления заказа залогиненным пользователем')
    def test_get_order_by_auth_user(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        main_page = MainPage(driver)
        main_page.wait_for_visibility_of_element(MainPageLocators.MAIN_BURGER_HEADER)
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(2)
        main_page.click_on_order_button()
        time.sleep(5)
        main_page.wait_visibility_of_modal()
        time.sleep(5)
        assert main_page.get_order_status == data.Data.ORDER_CONFIRM_MODAL_HEADER_TEXT
