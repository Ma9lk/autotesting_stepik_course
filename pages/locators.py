from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():

    LOGIN_FORM = (By.ID, 'login-form')
    REGISTER_FORM = (By.ID, 'register-form')
    REGISTER_FORM_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_FORM_PASSWORD = (By.ID, 'id_registration-password1')
    REPEAT_REGISTER_FORM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')

class ProductPageLocators():

    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_OF_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_PRICE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')

class BasketPageLocators():

    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '.basket-items')
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')