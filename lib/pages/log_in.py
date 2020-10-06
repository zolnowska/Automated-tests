from lib.pages.base import Base
from selenium.webdriver.common.by import By


class LoginInLocators:

    INPUT_EMAIL = (By.XPATH, '//input[@class="form-control"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')
    BTN_SIGN_IN = (By.ID, 'submit-login')
    BTN_CREATE_ACCOUNT = (By.XPATH, '//div[@class="no-account"]/a')
    TEXT_AUTHENTICATION_FAILED = (By.XPATH, '//div[@class="help-block"]')


class LogIn(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, email="test@test.test"):
        self.input(LoginInLocators.INPUT_EMAIL, email)

    def input_password(self, password="test1"):
        self.input(LoginInLocators.INPUT_PASSWORD, password)

    def click_sign_in(self):
        self.move_to_element_and_click(LoginInLocators.BTN_SIGN_IN)

    def click_create_account(self):
        self.move_to_element_and_click(LoginInLocators.BTN_CREATE_ACCOUNT)

    def log_in(self, email="test@test.test", password="test1"):
        self.input_email(email)
        self.input_password(password)
        self.click_sign_in()

    def get_text_authentication_failed(self):
        return self.get_text(LoginInLocators.TEXT_AUTHENTICATION_FAILED)
