from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url 
        self.browser.implicitly_wait(timeout)  
    
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):    
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
    # Этот метод проверяет, что элемент не появляется на странице в течение заданного времени
    # Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False  

    def is_disappeared(self, how, what, timeout=4):
    # Этот метод проверяет,что элемент исчезает со страницы(используем явное ожидание и  функцию until_not)
    # Будет ждать до тех пор, пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

# Перенесли методы из main_page.py
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        # В примере из 4.3 шаг 6 "Плюсы наследования: пример" в параметрах стоит -  LOGIN_LINK_INVALID и тогда тест не проходит.
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

# 4.3 шаг 10 Задание: наследование и отрицательные проверки 
    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()  

# Для 4.3.13 задания: группировка тестов и setup
    def should_be_authorized_user(self):
    # Проверка: пользователь залогинен
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"      