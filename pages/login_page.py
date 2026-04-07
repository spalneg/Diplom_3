from locators.main_page_locators import MainPageLocators as mp
from locators.base_page_locators import BasePageLocators as bp
from locators.feed_page_locators import FeedPageLocators as fp
from locators.register_page_locators import RegisterPageLocators as rp
from locators.login_page_locators import LoginPageLocators as lp
from pages.base_page import BasePage
import allure
from urls import *


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.send_keys_to_element(lp.email_field, email)
        self.send_keys_to_element(lp.password_field, password)
        self.click_element(lp.enter_button)
        self.wait_for_element_visible(mp.burger_header)



