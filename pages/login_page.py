from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from tests.data import Data
import allure

class LoginPage(BasePage):

    @allure.step("Тап на кнопку Восстановить пароль на экране авторизации")
    def click_on_reset_password_button(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.SET_PASSWORD_BUTTON)
        self.click_on_element(LoginPageLocators.SET_PASSWORD_BUTTON)

    @allure.step("Заполнение полей для авторизации")
    def fill_user_data_fields(self):
        self.wait_for_visibility_of_element(LoginPageLocators.TITLE_LOGIN_PAGE)
        self.fill_input_field(LoginPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.fill_input_field(LoginPageLocators.PASSWORD_FIELD, Data.PASSWORD)

    @allure.step("Тап на кнопку Войти")
    def click_on_enter_button(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.ENTER_BUTTON)
        self.click_on_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Переход к истории заказов")
    def go_to_orders_history(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.ORDERS_HISTORY_BUTTON)
        self.click_on_element(LoginPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Получаем текст заголовка страницы авторизации')
    def get_login_page_header_text(self):
        self.wait_for_visibility_of_element(LoginPageLocators.TITLE_LOGIN_PAGE)
        return self.find_element(LoginPageLocators.TITLE_LOGIN_PAGE).text

