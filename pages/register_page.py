from locators.register_page_locators import RegisterPageLocators as rp
from locators.login_page_locators import LoginPageLocators as lp
from pages.base_page import BasePage
from data import generate_random_string
import allure
from urls import *


class RegisterPage(BasePage):

    @allure.step('Загрузка страницы оформления заказа')
    def open_register_page(self):
        self.open_page(REGISTER_URL)
        self.wait_for_element_visible(rp.register_button)

    @allure.step('Ввод в поле "Имя"')
    def set_name(self, name):
        self.send_keys_to_element(rp.name_field, name)

    @allure.step('Ввод в поле "Email"')
    def set_email(self, email):
        self.send_keys_to_element(rp.email_field, email)
        return email

    @allure.step('Ввод в поле "Пароль"')
    def set_password(self, password):
        self.send_keys_to_element(rp.password_field, password)
        return password
    
    @allure.step('Регистрация нового пользователя с сохраненнием данных для логина')
    def register_user(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_element(rp.register_button)
        self.wait_for_element_clickable(lp.enter_button)
    
