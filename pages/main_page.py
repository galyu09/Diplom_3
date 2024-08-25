from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    @allure.step("Переход в 'Личный кабинет' тапом на кнопку с главной")
    def click_on_private_acc_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.PRIVET_ACC)
        self.click_on_element(MainPageLocators.PRIVET_ACC)

    @allure.step('Переходна страницу "Лента заказов" тапом на заголовок')
    def move_to_orders_feed(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDERS_FEED_BUTTON)
        self.click_on_element(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step('Переходим на главную страницу по кнопке в хедере')
    def move_to_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получаем название ингредиента')
    def get_ingredient_name_by_index(self, index):
        ingredients = self.get_visible_elements(MainPageLocators.LIST_OF_INGREDIENTS)
        return ingredients[index].text.split('\n')[2]

    @allure.step('Получаем ингредиент по индексу')
    def get_ingredient_by_index(self, index):
        ingredients = self.get_visible_elements(MainPageLocators.LIST_OF_INGREDIENTS)
        return ingredients[index]

    @allure.step('Выбираем ингредиент')
    def click_on_ingredient(self, index):
        ingredients = self.get_visible_elements(MainPageLocators.LIST_OF_INGREDIENTS)
        ingredients[index].click()

    @allure.step('Получаем название ингредиента в модальном окне с деталями')
    def get_ingredient_name_in_modal(self):
        return self.find_element(MainPageLocators.INGREDIENT_NAME_IN_MODAL).text

    @allure.step('Закрываем модальное окно')
    def close_popup_window(self):
        self.click_on_element(MainPageLocators.CLOSE_MODAl_BUTTON)

    @allure.step('Наличие всплывающего окна с деталями ингредиента')
    def find_ingredient_modal(self):
        return self.is_element_exist(MainPageLocators.INGREDIENT_MODAL)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self, index):
        ingredients = self.get_visible_elements(MainPageLocators.LIST_OF_INGREDIENTS)
        print(ingredients)
        basket = self.find_element(MainPageLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop(ingredients[index], basket)

    @allure.step('Получаем счетсик ингридиентов')
    def get_ingredients_counter(self, index):
        counters = self.get_visible_elements(MainPageLocators.INGREDIENT_COUNTER)
        return int(counters[index].text)

    @allure.step('Тап на кнопку Оформить заказ')
    def click_on_order_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Наличие модального окна с подтверждением заказа")
    def wait_visibility_of_modal(self):
        self.wait_for_visibility_of_element(MainPageLocators.INGREDIENT_MODAL)

    @allure.step('Ждем появления заголовка подтверждения заказа в модальном окне')
    def wait_order_confirm_header(self):
        self.wait_for_visibility_of_element(MainPageLocators.ORDER_CONFIRM_MODAL_HEADER)

    @allure.step('Получаем текст из окна подтверждения заказа')
    def get_order_status(self):
        return self.find_element(MainPageLocators.INGREDIENT_MODAL).text


    @allure.step('Закрытие окна подтверждения заказа по крестику')
    def close_order_confirm_modal(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDER_CONFIRM_MODAL_ClOSE)
        self.click_on_element(MainPageLocators.ORDER_CONFIRM_MODAL_ClOSE)


    @allure.step('Получаем id заказа')
    def get_order_id(self):
        return self.wait_real_order_id(MainPageLocators.ORDER_NUMBER)









