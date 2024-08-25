import pytest
import allure
from selenium import webdriver

from tests import data


@allure.step('Открываем окно браузера')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.get(data.Urls.BASE_URL)

    yield driver

    driver.quit()