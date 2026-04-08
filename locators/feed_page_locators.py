from selenium.webdriver.common.by import By


class FeedPageLocators:
    feed_header = [By.XPATH, '//h1[text()="Лента заказов"]']
    order_in_progress = [By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady__1YFem")]/li']
    completed_ever = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p']
    completed_today = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p']