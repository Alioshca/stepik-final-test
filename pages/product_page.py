from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def is_product_cost_equal_to_basket(self):
        cost_product = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        cost_basket = self.browser.find_element(*ProductPageLocators.BASKET_WHOLE_COST)
        assert cost_basket.text == cost_product.text, "Price of product is not equal to basket cost"

    def is_product_name_in_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_message = self.browser.find_element(*ProductPageLocators.BASKET_SUCCESS_MESSAGE)
        assert name_product.text == success_message.text, "Price of product is not equal to basket cost"