import allure
from urls import *
from locators.main_page_locators import MainPageLocators as mp
from locators.base_page_locators import BasePageLocators as bp
from locators.feed_page_locators import FeedPageLocators as fp
from pages.base_page import BasePage


class FeedPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Открытие страницы ленты заказов и ожидание загрузки страницы')       
    def open_feed_page(self):
        self.open_page(FEED_URL) 
        self.wait_for_element_visible(fp.feed_header) 

    @allure.step('Клик по кнопке "Конструктор" и ожидание загрузки страницы')
    def click_constructor_button(self):
        self.click_element(bp.base_constructor_button)
        return self.wait_for_element_visible(mp.burger_header)

    @allure.step('Получить текст раздела "Выполнено за всё время"')
    def get_order_ever_counter_text(self):
        return self.get_text(fp.completed_ever) 
    
    @allure.step('Получить текст раздела "Выполнено за сегодня"')
    def get_order_today_counter_text(self):
        return self.get_text(fp.completed_today) 
    
    @allure.step('Дождаться появления заказа в разделе "В работе"')
    def wait_for_order_number_in_progress(self, order_number):
        return self.wait_until_text_contains(fp.order_in_progress, order_number)
    

