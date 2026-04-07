import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)

@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)