from pages.basket_page import BasketPage # use '.pages.basket_page' for unix environment
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest
import time

PROJ_LINKS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.login_guest
class TestGuestCanGoToLoginPage():
    """Tests to check if guest can go to login page from product page.

    Input to your console 'pytest -s -v --tb=line --language=en -m login_guest test_product_page.py' to run tests.
    """
    
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.is_guest_on_login_page()


@pytest.mark.basket_guest
class TestGuestAddToBasketFromProductPage():
    """Tests to check if guest can add a product to the basket.

    Some tests use PROJ_LINKS variable, other use simple link.
    It was made only to show parametrizing mechanism. You can change it manually.

    Input to your console 'pytest -s -v --tb=line --language=en -m basket_guest test_product_page.py' to run tests.
    """

    @pytest.mark.parametrize('link', PROJ_LINKS)
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.is_product_cost_equal_to_basket()
        page.is_product_name_in_basket()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.is_empty_basket_message_presented()

    @pytest.mark.parametrize('link', PROJ_LINKS)
    @pytest.mark.xfail(reason="negative test result is what we need")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.parametrize('link', PROJ_LINKS)
    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="bug is being checked now")
    @pytest.mark.parametrize('link', PROJ_LINKS)
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_dissapear_success_message()


@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage():
    """Tests to check if user can add a product to the basket.
    
    Input to your console 'pytest -s -v --tb=line --language=en -m basket_user test_product_page.py' to run tests.
    """

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        test_email = f"{time.time()}@fakemail.org"
        test_password = f"{time.time()}"
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, self.link)
        login_page.register_new_user(test_email, test_password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.add_product_to_basket()
        page.is_product_cost_equal_to_basket()
        page.is_product_name_in_basket()

