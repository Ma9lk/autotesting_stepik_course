from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
            'Basket should be empty, but not'

    def should_be_not_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
            'Basket empty, but should not'

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), \
            'Element absent'

