from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # в этом классе каждый селектор — это пара: как искать и что искать

class LoginPageLocators():
    LOGIN_LINK_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK_REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    # Для 4.3.13 задания: группировка тестов и setup
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#register_form #id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#register_form #id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#register_form #id_registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')

# Задание: добавление в корзину со страницы товара
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')

    # Сообщения, которые появляются после нажатия кнопки "добавить в корзину"
    MESSAGE_BASKET_NAME = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')    
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')

    #Отрицательные проверки: как проверить отсутствие элемента
    SUCCESS_MESSAGE  = (By.CSS_SELECTOR, '.alert-success:first-child')

# Плюсы наследования: пример
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # Для 4.3.13 задание: группировка тестов и setup

#Задание: наследование и отрицательные проверки
class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")