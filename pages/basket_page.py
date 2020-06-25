from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_UNIT), "Product is in basket, but should not be"

    def is_empty_basket_message_presented(self):
        element = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE) and "Your basket is empty" in element.text, "Empty basket message is not presented, but should be"