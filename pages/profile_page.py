from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
import allure


class ProfilePage(BasePage):
    @allure.step('Переход к истории заказа')
    def go_to_order_history(self):
        self.wait_for_element_to_be_clickable(ProfilePageLocators.ORDER_HISTOTY_BUTTON)
        self.click_on_element(ProfilePageLocators.ORDER_HISTOTY_BUTTON)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.wait_for_element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Ждем прогрузки страницы профиля по заголовку')
    def wait_for_profile_page_header(self):
        self.wait_for_visibility_of_element(ProfilePageLocators.PROFILE_TITLE)

    @allure.step('Получаем текст заголовка страницы профиля')
    def get_profile_page_header_text(self):
        return self.find_element(ProfilePageLocators.PROFILE_TITLE).text
