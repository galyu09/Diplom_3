from selenium.webdriver.common.by import By


class MainPageLocators:
    # кнопка входа в личный кабинет
    PRIVET_ACC = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # кнопка "Лента заказов"
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    # Заголовок на главной
    MAIN_BURGER_HEADER = (By.XPATH, '//h1[text() = "Соберите бургер"]')

    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    # Список ингредиентов
    LIST_OF_INGREDIENTS = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"

    CLOSE_MODAl_BUTTON = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button")

    # Название ингредиента во всплывающем окне
    INGREDIENT_NAME_IN_MODAL = (By.XPATH, '//*[contains(@class, "Modal_modal_opened")]/div/div/p')

    # Модальное окно с деталями ингридиентов
    INGREDIENT_MODAL = (By.XPATH, '//*[contains(@class, "Modal_modal__text")]/p[1]')

    # Элемент конструктора бургера
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")

    # Счетчик ингридиентов
    INGREDIENT_COUNTER = (By.XPATH, "//*[contains(@class, 'counter_counter__num')]")

    # Кнопка Оформить заказ
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Заголовок идентификатор заказа в форме подтверждения заказа
    ORDER_CONFIRM_MODAL_HEADER = (By.XPATH, "//*[contains(@class, 'Modal_modal__text')]/p[1]")

    # Кнопка закрытия окна подтверждения заказа
    ORDER_CONFIRM_MODAL_ClOSE = (By.XPATH, './/button[contains(@class, "Modal_modal__close")]')

    # Номер заказа в модальном окне подтверждения
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'title_shadow')]")

