import allure

from locators.forgot_passport_page_locators import SetPasswordPageLocators
from locators.reset_password_locators import ResetPasswordLocators
from pages.forgot_password_page import ForgotPasswortPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswortPage
from tests import data



class TestResetPassword:

    @allure.title('Переход экран Восстановления пароля по кнопке Восстановить')
    @allure.description('Проверка перехода на страницу тапом по кнопке Востановить')
    def test_go_to_paswordset_page_from_forgot_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.click_on_reset_password_button()
        forgot_passport_page = ForgotPasswortPage(driver)
        text = forgot_passport_page.find_element(SetPasswordPageLocators.PASSWORD_SET_HEADER).text
        assert text == data.Data.PASSWORD_RESET_HEADER_TEXT
        assert forgot_passport_page.take_current_url() == data.Urls.FORGOT_PAGE_URL


    @allure.title("Переход по кнопке 'Восстановить' с заполненными данными")
    @allure.description('Проверяем ввод почты и клик по кнопке "Восстановить"')
    def test_reset_password_with_valid_data(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.click_on_reset_password_button()
        forgot_passport_page = ForgotPasswortPage(driver)
        forgot_passport_page.fill_input_login()
        forgot_passport_page.click_on_reset_password_button()
        reset_pasp_page = ResetPasswortPage(driver)
        text = reset_pasp_page.find_element(ResetPasswordLocators.RESET_PASSPORT_HEADER).text
        assert reset_pasp_page.take_current_url() == data.Urls.RESET_PASSWORD_URl
        assert text == data.Data.PASSWORD_RESET_HEADER_TEXT

    @allure.description("Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_password_icon_make_it_active(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_private_acc_button()
        login_page = LoginPage(driver)
        login_page.click_on_reset_password_button()
        forgot_passport_page = ForgotPasswortPage(driver)
        forgot_passport_page.fill_input_login()
        forgot_passport_page.click_on_reset_password_button()
        reset_pasp_page = ResetPasswortPage(driver)
        reset_pasp_page.fill_new_input_password()
        reset_pasp_page.click_on_show_eye()
        assert reset_pasp_page.is_password_field_active()




