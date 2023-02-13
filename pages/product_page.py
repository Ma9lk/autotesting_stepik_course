from .base_page import BasePage
from .locators import ProductPageLocators
import re



class ProductPage(BasePage):

    def should_be_add_to_basket(self):
        add_to_basket_click = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_click.click()

    def should_be_name_of_book(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        return name_of_book.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_succsess_message(self):
        text_in_succsess_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        return text_in_succsess_message.text

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is disappeared, but should not be'

    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_be_product_price_in_basket(self):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_MESSAGE)
        return product_price_in_basket.text