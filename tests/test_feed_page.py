import allure
from data import *


class TestFeedPage:
   
    @allure.title('Проверка увеличения счётчика заказов за всё время после оформления заказа')
    @allure.description('Регистрация и логин пользователя, получение количества заказов в "счётчике заказов за всё время" ' \
    'до оформления заказа, оформление заказа и сравнение числа заказов в "счётчике заказов за всё время" до и после заказа') 
    def test_completed_ever_counter_increase(self, register_page, main_page, login_page, feed_page):
        register_page.open_register_page()
        email, password = register_page.register_user()
        login_page.login(email, password)
        main_page.click_feed_button()
        before_order = feed_page.get_order_ever_counter_text()
        feed_page.click_constructor_button()
        main_page.add_bun_to_basket()
        main_page.make_order()
        feed_page.open_feed_page()
        assert feed_page.get_order_ever_counter_text() > before_order

    @allure.title('Проверка увеличения счётчика заказов за сегодня после оформления заказа')
    @allure.description('Регистрация и логин пользователя, получение количества заказов в "счётчике заказов за сегодня" ' \
    'до оформления заказа, оформление заказа и сравнение числа заказов в "счётчике заказов за сегодня" до и после заказа') 
    def test_completed_today_counter_increase(self, register_page, main_page, login_page, feed_page):
        register_page.open_register_page()
        email, password = register_page.register_user()
        login_page.login(email, password)
        main_page.click_feed_button()
        before_order = feed_page.get_order_today_counter_text()
        feed_page.click_constructor_button()
        main_page.add_bun_to_basket()
        main_page.make_order()
        feed_page.open_feed_page()
        assert feed_page.get_order_today_counter_text() > before_order 

    @allure.title('Оформление заказа и проверка появления номера заказа в разделе "В работе" на странице "Лента заказов"')
    @allure.description('Регистрация и логин пользователя, оформление заказа, переход на страницу "Лента заказов" ' \
    'и ожидание появления номера оформленного заказа в разделе "В работе"') 
    def test_order_number_in_order_progress_list(self, register_page, main_page, login_page, feed_page):
        register_page.open_register_page()
        email, password = register_page.register_user()
        login_page.login(email, password)
        main_page.add_bun_to_basket()
        main_page.make_order()
        order_number = main_page.wait_for_and_get_order_number()
        feed_page.open_feed_page()
        assert feed_page.wait_for_order_number_in_progress(order_number)
