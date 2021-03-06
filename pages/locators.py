from selenium.webdriver.common.by import By

class BasePageLocators():
    """CSS selectors for BasePage object. Used on each page"""

    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini > span > a")

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    """CSS selectors for basket page."""

    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

    PRODUCT_UNIT = (By.CSS_SELECTOR, "#basket_formset > div.basket-items")

class LoginPageLocators():
    """CSS selectors for login and registration page."""

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

class MainPageLocators():
    """CSS selectors for main page."""

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    """CSS selectors for product page."""

    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BASKET_SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_WHOLE_COST = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    
    PRODUCT_COST = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")