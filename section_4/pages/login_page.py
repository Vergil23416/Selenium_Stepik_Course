import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert (
            LoginPageLocators.CURRENT_LINK_SUFFIX in current_url
        ), "Login url is not corrected"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)

        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        input_password.send_keys(password)

        input_return_password = self.browser.find_element(
            *LoginPageLocators.REGISTER_RETURN_PASSWORD
        )
        input_return_password.send_keys(password)

        button_submit = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON_SUBMIT
        )
        button_submit.click()
