import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterField
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        # print(self.url, 'вот нужный адрес ')
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.url, 'Sorry.. Url is not valid'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
                                    'Sorry.. Login form is missing'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
                                    'Sorry.. Register form is missing'

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*RegisterField.LOGIN_FIELD)
        login_field.send_keys(email)
        password_field_1 = self.browser.find_element(*RegisterField.PASSWORD_FIELD)
        password_field_1.send_keys(password)
        password_field_2 = self.browser.find_element(*RegisterField.DOUBLE_PASSWORD_FIELD)
        password_field_2.send_keys(password)
        button_register = self.browser.find_element(*RegisterField.BUTTON_REGISTER)
        button_register.click()
