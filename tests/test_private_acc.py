
import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from tests import data



class TestPrivate:
    @allure.title('Переход по кнопке Личный кабинет')
    @allure.description('Проверка перехода в личный кабинет НЕавторизованным пользователем')
    def test_click_on_private_acc_button_without_auth(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        title = login_page.get_login_page_header_text()
        assert title == data.Data.TITLE_LOGIN_PAGE_TEXT
        assert login_page.take_current_url() == data.Urls.LOGIN_PAGE_URL

    @allure.title('Переход по кнопке Личный кабинет')
    @allure.description('Проверка перехода в личный кабинет авторизованным пользователем')
    def test_click_on_private_acc_button_by_auth_user(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.click_on_private_acc_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_page_header()
        text = profile_page.get_profile_page_header_text()
        assert profile_page.take_current_url() == data.Urls.PROFILE_PAGE_URL
        assert text == data.Data.PROFILE_TITLE_TEXT

    @allure.title('Переход к Истории заказа')
    @allure.description('Проверяем, что по тапу на Историю заказов оказываемся на нужном экране')
    def test_go_to_order_hystory(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.click_on_private_acc_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_page_header()
        profile_page.go_to_order_history()
        assert profile_page.take_current_url() == data.Urls.ORDER_HISTORY_URL

    @allure.title('Выход из Аккаунта')
    @allure.description('Проверяем, что по тапу на кнопку Выход переводит на экран авторизации')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.fill_user_data_fields()
        login_page.click_on_enter_button()
        main_page = MainPage(driver)
        main_page.wait_for_main_header()
        main_page.click_on_private_acc_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_page_header()
        profile_page.logout()
        login_page = LoginPage(driver)
        text = login_page.get_login_page_header_text
        assert login_page.take_current_url() == data.Urls.LOGIN_PAGE_URL
        assert text == data.Data.TITLE_LOGIN_PAGE_TEXT
