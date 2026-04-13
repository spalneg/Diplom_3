from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators as mp
from urls import *
import allure


class BasePage:
    
    def __init__(self, driver):

        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Клик по элементу')
    def click_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Найти элемент')
    def find_the_element(self, element):
        return self.driver.find_element(*element)
    
    @allure.step('Получение текста элемента')
    def get_text(self, element):
        return self.driver.find_element(*element).text
    
    @allure.step('Ожидание загрузки видимости элемента')
    def wait_for_element_visible(self, element):
        return WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Ожидание невидимости элемента')
    def wait_for_element_invisible(self, element):
        return WebDriverWait(self.driver, 25).until(expected_conditions.invisibility_of_element_located(element))
    
    @allure.step('Ожидание загрузки кликабельности элемента')
    def wait_for_element_clickable(self, element):
        return WebDriverWait(self.driver, 25).until(expected_conditions.element_to_be_clickable(element))

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_basket(self, ingredient):
        ingredient_select = self.find_the_element(ingredient)
        order = self.find_the_element(mp.drop_bun_spot)
        self.driver.execute_script("""
            function simulateDragDrop(source, target) {
                var evt = new DragEvent('dragstart', {bubbles: true, cancelable: true});
                source.dispatchEvent(evt);
                var evt2 = new DragEvent('dragover', {bubbles: true, cancelable: true});
                target.dispatchEvent(evt2);
                var evt3 = new DragEvent('drop', {bubbles: true, cancelable: true});
                target.dispatchEvent(evt3);
                var evt4 = new DragEvent('dragend', {bubbles: true, cancelable: true});
                source.dispatchEvent(evt4);
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """, ingredient_select, order)

    @allure.step('Ввод данных в выбранный элемент')
    def send_keys_to_element(self, element, keys):
        self.driver.find_element(*element).send_keys(keys)
    
    @allure.step('Ожидание изменения текста')
    def wait_until_text_changes(self, element, text):
        WebDriverWait(self.driver, 25).until(lambda x: x.find_element(*element).text != text)

    @allure.step('Ожидание появления текста в элементе')
    def wait_until_text_contains(self, element, text):
        return WebDriverWait(self.driver, 25).until(lambda x: text in x.find_element(*element).text)