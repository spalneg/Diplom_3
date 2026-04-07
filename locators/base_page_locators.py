from selenium.webdriver.common.by import By


class BasePageLocators:
    base_constructor_button = [By.XPATH, '//p[text()="Конструктор"]']
    base_feed_button = [By.XPATH, '//p[text()="Лента Заказов"]']