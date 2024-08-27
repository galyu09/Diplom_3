import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.orders_history_page import OrdersHistoryPage



class TestOrderList:
    @allure.title('Переход к деталям заказа')
    @allure.description('Клик на заказ в ленте заказов открывает модальное окно с детальной информацией')
    def test_click_to_order_move_to_detail_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        # залогин юзером
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        # оформление заказа
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(2)
        main_page.click_on_order_button()
        # подтверждение заказа
        main_page.wait_order_confirm_header()
        main_page.close_order_confirm_modal()
        # переход в ленту заказов
        main_page.move_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.click_on_first_order_in_order_list()
        assert orders_feed_page.get_modal_with_orders_details()

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('Оформляем заказ, и проверяем наличие его номера в блоке В работе')
    def test_order_number_is_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        # залогин юзером
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        # оформление заказа
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(2)
        main_page.click_on_order_button()
        main_page.wait_order_confirm_header()
        order_id = main_page.get_order_id()
        main_page.close_order_confirm_modal()
        # переход в ленту заказов
        main_page.move_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        assert order_id in orders_feed_page.get_orders_in_process(order_id)


    @allure.title('Отображение заказов пользователя в «Лента заказов»')
    @allure.description('Проверяем, что заказ пользователя присутствует и в Истории заказа, и в  Ленте заказа')
    def test_user_order_exist_in_feed_and_history(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        # залогин юзером
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        # оформление заказа
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(2)
        main_page.click_on_order_button()
        main_page.wait_order_confirm_header()
        main_page.close_order_confirm_modal()
        # переход к истории заказов
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.go_to_orders_history()
        # получаем список заказов юзера в Истории
        orders_history_page = OrdersHistoryPage(driver)
        order_from_history = orders_history_page.get_first_order_id()
        # переход в ленту заказов
        orders_history_page.move_to_orders_feed()
        # получаем список заказов в ленте
        orders_feed_page = OrdersFeedPage(driver)
        feed_orders_list = orders_feed_page.get_orders_feed_list()
        assert order_from_history in feed_orders_list


    @allure.title('Увеличение счетчика Выполнено за все время»')
    @allure.description('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа')
    def test_total_count(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        # залогин юзером
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        # получение исходного значение счётчика
        main_page = MainPage(driver)
        main_page.move_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        total_counter1 = orders_feed_page.get_current_counter()
        orders_feed_page.go_to_main()
        # оформление заказа
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(2)
        main_page.click_on_order_button()
        main_page.wait_order_confirm_header()
        main_page.close_order_confirm_modal()
        main_page.move_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        total_counter2 = orders_feed_page.get_current_counter()
        assert total_counter1 < total_counter2

    @allure.title('Увеличение счетчика "Выполнено за сегодня"')
    @allure.description('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_total_count_today(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        # залогин юзером
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        # получение исходного значение счётчика
        main_page = MainPage(driver)
        main_page.move_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        today_counter1 = orders_feed_page.get_current_counter_today()
        orders_feed_page.go_to_main()
        # оформление заказа
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(2)
        main_page.click_on_order_button()
        # Закрываем модалку, переходим к ленте заказов
        main_page.wait_order_confirm_header()
        main_page.close_order_confirm_modal()
        main_page.move_to_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        today_counter2 = orders_feed_page.get_current_counter_today()
        assert today_counter1 < today_counter2








