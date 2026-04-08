from locators.register_page_locators import RegisterPageLocators as rp
from locators.login_page_locators import LoginPageLocators as lp
from pages.base_page import BasePage
from data import generate_random_string
import allure
from urls import *


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Загрузка страницы оформления заказа')
    def open_register_page(self):
        self.open_page(REGISTER_URL)
        self.wait_for_element_visible(rp.register_button)

    @allure.step('Ввод в поле "Имя" имени "Burgerman"')
    def set_name(self):
        self.send_keys_to_element(rp.name_field, 'Burgerman')

    @allure.step('Ввод в поле "Email" уникальной сгенерированной почты')
    def set_email(self):
        email = f'{generate_random_string(10)}@test.test'
        self.send_keys_to_element(rp.email_field, email)
        return email

    @allure.step('Ввод в поле "Пароль" пароля "654321"')
    def set_password(self):
        password = '654321'
        self.send_keys_to_element(rp.password_field, password)
        return password
    
    @allure.step('Регистрация нового пользователя с сохраненнием данных для логина')
    def register_user(self):
        self.set_name()
        email = self.set_email()
        password = self.set_password()
        self.click_element(rp.register_button)
        self.wait_for_element_visible(lp.enter_button)
        return email, password
    
