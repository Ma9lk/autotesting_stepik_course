from selenium.webdriver.common.by import By

class MainPageLocators():

    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators():

    LOGIN_FORM = (By.ID, 'login-form')
    REGISTER_FORM = (By.ID, 'register-form')

class ProdcutPageLocators():

    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_OF_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    TEXT_IN_SUCCSESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alert-info strong')