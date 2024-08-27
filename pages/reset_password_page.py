from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage
from tests.data import Data
import allure

class ResetPasswortPage(BasePage):
    @allure.step('Клик на поле ввода пароля')
    def click_on_password_field(self):
        self.wait_for_visibility_of_element(ResetPasswordLocators.NEW_PASSWORD_FIELD)
        self.click_on_element(ResetPasswordLocators.NEW_PASSWORD_FIELD)

    @allure.step('Вводим новый пароль')
    def fill_new_input_password(self):
        self.wait_for_visibility_of_element(ResetPasswordLocators.NEW_PASSWORD_FIELD)
        # test_data = helpers.get_user_data()
        self.fill_input_field(ResetPasswordLocators.NEW_PASSWORD_FIELD, Data.PASSWORD)

    @allure.step('Клик на кнопку показа/скрытия пароля')
    def click_on_show_eye(self):
        self.wait_for_visibility_of_element(ResetPasswordLocators.EYE_BUTTON)
        self.click_on_element(ResetPasswordLocators.EYE_BUTTON)

    @allure.step('Проверяем активно (подсвечивается) ли поле ввода нового пароля')
    def is_password_field_active(self):
        return 'input_status_active' in self.get_attribute(ResetPasswordLocators.NEW_PASSWORD_ELEMENT_DIV, 'class')

    @allure.step('Ждем загрузки страницы по хедеру')
    def wait_for_rp_header(self):
        return self.find_element(ResetPasswordLocators.RESET_PASSPORT_HEADER).text
