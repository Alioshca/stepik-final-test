from pages.basket_page import BasketPage # use '.pages.basket_page' for unix environment 
from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest

@pytest.mark.basket_empty_guest
class TestGuestCanGoToEmptyBasketFromMainPage():
    """Tests to check if guest can go to empty basket from main page with no products added.

    Input to your console 'pytest -s -v --tb=line --language=en -m basket_empty_guest test_main_page.py' to run tests.
    """

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.is_empty_basket_message_presented()

@pytest.mark.login_guest
class TestGuestCanGoToLoginPageFromMainPage():
    """Tests to check if guest can go to login page from main page.

    Input to your console 'pytest -s -v --tb=line --language=en -m login_guest test_main_page.py' to run tests.
    """

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_be_on_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()

