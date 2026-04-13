from selenium.webdriver.common.by import By


class LoginPageLocators:
    enter_button = [By.XPATH, '//button[text()="Войти"]']
    email_field = [By.XPATH, '//input[@type="text"]']
    password_field = [By.XPATH, '//input[@type="password"]']
