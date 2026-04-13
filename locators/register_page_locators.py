from selenium.webdriver.common.by import By


class RegisterPageLocators:
    name_field = [By.XPATH, '//label[text()="Имя"]/following-sibling::input']
    email_field = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    password_field = [By.XPATH, '//input[@type="password"]']
    register_button = [By.XPATH, '//button[text()="Зарегистрироваться"]']