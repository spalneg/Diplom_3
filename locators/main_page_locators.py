from selenium.webdriver.common.by import By


burger_header = [By.XPATH, '//h1[text()="Соберите бургер"]']
bun_ingredient = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
ingredient_details = [By.XPATH, '//h2[text()="Детали ингредиента"]']
details_close_button = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 button"]