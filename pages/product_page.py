from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    """Test methods for product page"""
    
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def is_guest_on_login_page(self):
        self.go_to_login_page()
        assert "http://selenium1py.pythonanywhere.com" in self.browser.current_url and "accounts/login" in self.browser.current_url

    def is_product_cost_equal_to_basket(self):
        cost_product = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        cost_basket = self.browser.find_element(*ProductPageLocators.BASKET_WHOLE_COST)
        assert cost_basket.text == cost_product.text, "Price of product is not equal to basket cost"

    def is_product_name_in_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_message = self.browser.find_element(*ProductPageLocators.BASKET_SUCCESS_MESSAGE_PRODUCT_NAME)
        assert name_product.text == success_message.text, "Price of product is not equal to basket cost"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_SUCCESS_MESSAGE), "Success message has not dissapeared"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_SUCCESS_MESSAGE), "Success message is presented, but should not be"