from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Дождаться загрузки элемента')
    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Дождаться, когда элемент станет кликабельным')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))

    @allure.step('Проскроллить до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Заполнить поле значением')
    def fill_input_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Берем текущий адрес страницы')
    def take_current_url(self):
        return self.driver.current_url

    # @allure.step('Переключаемся на другую вкладку')
    # def switch_to_window(self, tab_count):
    #     self.driver.switch_to.window(self.driver.window_handles[tab_count])

    @allure.step('Получаем значение атрибута элемента')
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @allure.step('Получаем список элементов ')
    def get_visible_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Проверяем нашличие элемента на странице')
    def is_element_exist(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        finally:
            return False

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, ingredient_element, target_element):
        drag_and_drop(self.driver, ingredient_element, target_element)

    @allure.step("Проверяем наличие элемента на странице")
    def check_element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def wait_real_order_id(self, locator):
        WebDriverWait(self.driver, 30).until_not(
            lambda driver: driver.find_element(*locator).text == "9999"
        )
        return self.find_element(locator).text

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)




