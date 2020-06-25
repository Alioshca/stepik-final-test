from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """Test methods for login-and-registration page"""

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_password_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        reg_password_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        reg_email.send_keys(email)
        reg_password_1.send_keys(password)
        reg_password_2.send_keys(password)
        reg_button.click()
        assert self.should_be_authorized_user() is None, "User is not authorized, but should be"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented on the page"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.current_url
        assert "login" in login_link, "The link does not match login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented on the page"

