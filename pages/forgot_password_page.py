from locators.forgot_passport_page_locators import SetPasswordPageLocators
from pages.base_page import BasePage
from tests.data import Data
import allure

class ForgotPasswortPage(BasePage):

    @allure.step('Заполнить поле Email')
    def fill_input_login(self):
        self.wait_for_visibility_of_element(SetPasswordPageLocators.PASSWORD_SET_HEADER)
        # test_data = helpers.get_user_data()
        self.fill_input_field(SetPasswordPageLocators.EMAIL_INPUT_FIELD, Data.EMAIL)

    @allure.step('Тап на кнопку Восстановить пароль')
    def click_on_reset_password_button(self):
        self.wait_for_visibility_of_element(SetPasswordPageLocators.PASSWORD_RESET_BUTTON)
        self.click_on_element(SetPasswordPageLocators.PASSWORD_RESET_BUTTON)

    @allure.step('Тап на поле ввода Email')
    def click_on_input_login(self):
        self.wait_for_visibility_of_element(SetPasswordPageLocators.PASSWORD_SET_HEADER)
        self.click_on_element(SetPasswordPageLocators.EMAIL_INPUT_FIELD)

    @allure.step('Ищем заголовок страницы восстановления пароля')
    def get_passport_header_text(self):
        self.wait_for_visibility_of_element(SetPasswordPageLocators.PASSWORD_SET_HEADER)
        return self.find_element(SetPasswordPageLocators.PASSWORD_SET_HEADER).text





