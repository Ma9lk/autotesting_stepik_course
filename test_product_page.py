import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    alert_answer = BasePage(browser, link)
    alert_answer.solve_quiz_and_get_code()
    assert page.should_be_name_of_book() == page.should_be_succsess_message(), \
        f'Название продукта {page.should_be_name_of_book()} не совпадает c текстом в сообщении {page.should_be_succsess_message()}'
    assert page.should_be_product_price() == page.should_be_product_price_in_basket(), \
        f'Цена продукта {page.should_be_product_price} не совпадает c ценой в корзине {page.should_be_product_price_in_basket()}'

    
    