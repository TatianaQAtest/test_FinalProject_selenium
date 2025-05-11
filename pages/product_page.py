from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
    # метод добавления товара в корзину
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()
   
    def should_be_add_to_basket(self):
    # проверка,что товар добавлен в корзину
        self.should_be_right_product_name()
        self.should_be_right_product_price()

    def should_be_right_product_name(self):
    # проверка,что название товара в сообщении совпадает с добавленным товаром

        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        product_name_text = product_name.text

        basket_name = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_NAME)
        basket_name_text = basket_name.text

        print(product_name_text, basket_name_text)
        assert product_name_text == basket_name_text, f"{product_name_text} is not {basket_name_text}"

    def should_be_right_product_price(self):
    # проверка,что стоимость корзины равна цене товара

        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        product_price_text = product_price.text

        basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE)
        basket_price_text = basket_price.text

        print(product_price_text, basket_price_text)
        assert product_price_text == basket_price_text, f"{product_price_text} not equal {basket_price_text}"
    
    