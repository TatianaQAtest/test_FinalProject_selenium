import time
from .base_page import BasePage
from  .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        time.sleep(3)
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket is not empty"

    def should_be_message_empty_basket(self):
        time.sleep(3)
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "No message about empty basket"