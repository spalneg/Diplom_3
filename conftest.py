import pytest
from selenium import webdriver
from data import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    return {
        'name': 'Burgerman',
        'email': f'{generate_random_string(10)}@test.test',
        'password': '654321'
    }