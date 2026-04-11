import allure
from data import *
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestBaseFunctions():

    @allure.title('Проверка кнопки "Конструктор"') 
    @allure.description('Загрузка страницы "Лента заказов", клик по кнопке "Конструктор" с проверкой загрузки страницы')    
    def test_constructor_button(self, driver):
        feed_page = FeedPage(driver)

        feed_page.open_feed_page()
        
        assert feed_page.click_constructor_button()

    @allure.title('Проверка кнопки "Лента заказов"') 
    @allure.description('Загрузка страницы "Конструктор", клик по кнопке "Лента заказов" с проверкой загрузки страницы')    
    def test_feed_button(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()

        assert main_page.click_feed_button()    
    
    @allure.title('Проверка появления описания ингредиента по клику на ингредиент')
    @allure.description('Загрузка страницы "Конструктор", клик по кнопке ингредиента с проверкой текста информации о ингредиенте') 
    def test_ingredient_description_on_click(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()

        assert main_page.click_bun_button()
         
    @allure.title('Проверка закрытия окна описания ингредиента по клику на "крестик"')
    @allure.description('Загрузка страницы "Конструктор", клик по кнопке ингредиента, клик по "крестику" в информации о ингредиенте с проверкой закрытия окна') 
    def test_ingredient_description_close_button(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_bun_button()

        assert main_page.click_ingredient_close_button()
    
    @allure.title('Проверка увеличения количества ингредиентов в счётчике ингредиента при его добавлении в заказ')
    @allure.description('Загрузка страницы "Конструктор", добавление в заказ булки (добавляются по 2), проверка увеличения счётчика на 2')
    def test_ingredient_count_increase(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.add_bun_to_basket()

        assert main_page.get_ingredient_counter_text() == '2'

    