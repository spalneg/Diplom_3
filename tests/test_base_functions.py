import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.feed_page import FeedPage
import allure
from data import *

class TestBaseFunctions():

    def test_constructor_button(self, feed_page):
        feed_page.open_feed_page()
        assert feed_page.click_constructor_button()


