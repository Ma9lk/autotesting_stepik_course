import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time

@pytest.mark.registration_user
class TestUserAddToBasketFromProductPage():

    link = 'http://selenium1py.pythonanywhere.com/accounts/login/'

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'EOdqA3Y@|v'
        page = LoginPage(browser, self.link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):

        page = ProductPage(browser, self.link)
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):

        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
        page = ProductPage(browser, link)
        page.should_be_add_to_basket()
        page.should_be_comparison_names()
        page.should_be_comparison_prices()

        
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.should_be_comparison_names()
    page.should_be_comparison_prices()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_text_that_basket_is_empty()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.should_be_disappeared_success_message()
