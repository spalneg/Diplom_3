from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators as bp
from selenium.webdriver.common.action_chains import ActionChains
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
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(element))

    @allure.step('Ожидание невидимости элемента')
    def wait_for_element_invisible(self, element):
        WebDriverWait(self.driver, 25).until(expected_conditions.invisibility_of_element_located(element))

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_basket(self, ingredient):
        ingredient_select = self.find_element(ingredient)
        order = self.find_element(mp.drop_bun_spot)
        ActionChains(self.driver).click_and_hold(ingredient_select).move_to_element(order).release().perform()