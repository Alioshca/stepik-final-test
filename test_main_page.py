# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.login_page import LoginPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_be_on_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_page()          # выполняем метод страницы - переходим на страницу логина
# class TestStepik():

#     def test_basket_button(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         browser.get(link)
#         # Сначала ждём загрузки всей страницы
#         browser.implicitly_wait(3)
#         # Для перестраховки подождём и загрузки самого элемента
#         button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
#         # assert здесь для красоты, он никак не влияет на результат прохождения теста
#         assert button

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()

# def go_to_login_page(browser):
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()

# def test_guest_can_go_to_login_page(browser): 
#     browser.get(link) 
#     go_to_login_page(browser) 