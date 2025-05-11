from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # в этом классе каждый селектор — это пара: как искать и что искать

class LoginPageLocators():
    LOGIN_LINK_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK_REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

# Задание: добавление в корзину со страницы товара
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')

    # Сообщения, которые появляются после нажатия кнопки "добавить в корзину"
    MESSAGE_BASKET_NAME = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')    
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')