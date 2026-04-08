from selenium.webdriver.common.by import By


class MainPageLocators:
    burger_header = [By.XPATH, '//h1[text()="Соберите бургер"]']
    bun_ingredient = [By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]']
    ingredient_details = [By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//p[text()='Флюоресцентная булка R2-D3']"]
    details_close_button = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 button"]
    drop_bun_spot = [By.XPATH, '//span[text()="Перетяните булочку сюда (верх)"]']
    bun_count = [By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6d'] p.counter_counter__num__3nue1"]
    make_order = [By.XPATH, '//button[text()="Оформить заказ"]']
    order_window_close_button = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 .Modal_modal__close__TnseK"]
    order_number = [By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 .Modal_modal__title_shadow__3ikwq"]