from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):

        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        input_email.send_keys(email)

        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        input_password.send_keys(password)

        repeat_input_password = self.browser.find_element(*LoginPageLocators.REPEAT_REGISTER_FORM_PASSWORD)
        repeat_input_password.send_keys(password)
        
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.current_url
        assert True, 'Подстрока "login" отсутствует в URL'

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert True, 'Форма логина отсутствует'

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert True, 'Форма регитсрации отсутствует'