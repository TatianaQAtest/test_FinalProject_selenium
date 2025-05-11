from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage): 
# MainPage наследник класса BasePage (в скобках указан класс-предок)
# Т.о. класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #символ *, он указывает на то, что мы передали именно пару(этот кортеж нужно распаковать)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # Создаем адекватное сообщение об ошибке для негативной проверки  