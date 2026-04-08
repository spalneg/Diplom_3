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
        return self.wait_for_element_visible(mp.burger_header)   

    @allure.step('Клик по ингредиенту "Флюоресцентная булка" и ожидание загрузки деталей ингредиента')
    def click_bun_button(self):
        self.click_element(mp.bun_ingredient)
        return self.wait_for_element_visible(mp.ingredient_details)

    @allure.step('Клик по кнопке "Лента заказов" и ожидание загрузки страницы')
    def click_feed_button(self):
        self.click_element(bp.base_feed_button)
        return self.wait_for_element_visible(fp.feed_header)

    @allure.step('Клик по кнопке закрытия окна с деталями ингредиента и ожидание закрытия окна')
    def click_ingredient_close_button(self):
        self.click_element(mp.details_close_button)
        return self.wait_for_element_invisible(mp.ingredient_details)

    @allure.step('Добавление булки в заказ')
    def add_bun_to_basket(self):
        self.add_ingredient_to_basket(mp.bun_ingredient)

    @allure.step('Получение текста счётчика ингредиентов')
    def get_ingredient_counter_text(self):
        return self.get_text(mp.bun_count)
    
    @allure.step('Клик по кнопке "Оформить заказ"')
    def make_order(self):
        self.click_element(mp.make_order)
        self.wait_for_element_clickable(mp.order_window_close_button)

    @allure.step('Ожидание появления заказа и получение номера заказа')
    def wait_for_and_get_order_number(self):
        self.wait_until_text_changes(mp.order_number, '9999')
        return self.get_text(mp.order_number)    
    

        
    

    

