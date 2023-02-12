from .base_page import BasePage
from .locators import ProdcutPageLocators
import re



class ProductPage(BasePage):

    def should_be_add_to_basket(self):
        add_to_basket_click = self.browser.find_element(*ProdcutPageLocators.ADD_TO_BASKET)
        add_to_basket_click.click()

    def should_be_name_of_book(self):
        name_of_book = self.browser.find_element(*ProdcutPageLocators.NAME_OF_BOOK)
        name_of_book.text

    def should_be_succsess_message(self):
        text_in_succsess_message = self.browser.find_element(*ProdcutPageLocators.TEXT_IN_SUCCSESS_MESSAGE)
        text_in_succsess_message.text

    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProdcutPageLocators.PRODUCT_PRICE)
        text_product_price = product_price.text
        return text_product_price

    def should_be_product_price_in_basket(self):
        product_price_in_basket = self.browser.find_element(*ProdcutPageLocators.PRODUCT_PRICE_IN_BASKET)
        text_product_price_in_basket = product_price_in_basket.text
        return text_product_price_in_basket