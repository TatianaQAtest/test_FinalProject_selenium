from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
# MainPage наследник класса BasePage (в скобках указан класс-предок)
# Т.о. класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        # мы намеренно сделали селектор неправильным, чтобы посмотреть, что именно выдаст тест, если поймает баг