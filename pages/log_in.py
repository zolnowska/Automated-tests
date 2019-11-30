from pages.base import Base
from locators import login_in


class LogIn(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, email="test@test.test"):
        self.input(login_in.INPUT_EMAIL, email)

    def input_password(self, password="test1"):
        self.input(login_in.INPUT_PASSWORD, password)

    def click_sign_in(self):
        self.wait_and_click(login_in.BTN_SIGN_IN)

    def click_create_account(self):
        self.wait_and_click(login_in.BTN_CREATE_ACCOUNT)

    def log_in(self, email="test@test.test", password="test1"):
        self.input_email(email)
        self.input_password(password)
        self.click_sign_in()

    def get_text_authentication_failed(self):
        return self.get_text(login_in.TEXT_AUTHENTICATION_FAILED)

