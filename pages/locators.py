from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():

    LOGIN_FORM = (By.ID, 'login-form')
    REGISTER_FORM = (By.ID, 'register-form')

class ProductPageLocators():

    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_OF_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_PRICE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')
