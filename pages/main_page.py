from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators as mp
from locators.base_page_locators import BasePageLocators as bp
from locators.feed_page_locators import FeedPageLocators as fp
from pages.base_page import BasePage

import allure
from urls import *


class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие главной страницы и ожидание загрузки страницы')       
    def open_main_page(self):
        self.open_page(BASE_URL) 
        self.wait_for_element_visible(mp.burger_header)   

    @allure.step('Клик по ингредиенту "Флюоресцентная булка" и ожидание загрузки деталей ингредиента')
    def click_bun_button(self):
        self.click_element(mp.bun_ingredient)
        return self.wait_for_element_visible(mp.details_close_button)

    @allure.step('Клик по кнопке "Лента заказов" и ожидание загрузки страницы')
    def click_feed_button(self):
        self.click_element(bp.base_feed_button)
        return self.wait_for_element_visible(fp.feed_header)

    @allure.step('Клик по кнопке закрытия окна с деталями ингредиента и ожидание закрытия окна')
    def click_ingredient_close_button(self):
        self.click_element(mp.details_close_button)
        return self.wait_for_element_invisible(mp.ingredient_details)

    @allure.step('Добавить булку в заказ')
    def add_bun_to_basket(self):
        self.add_ingredient_to_basket(mp.bun_ingredient)

    @allure.step('Получить текст счётчика ингредиентов')
    def get_ingredient_counter_text(self):
        return self.get_text(mp.bun_count)
    


