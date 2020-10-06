from selenium.webdriver.common.by import By
from lib.pages.base import Base


class HeaderLocators:
    BTN_SIGN_IN = (By.XPATH, '//div[@class="user-info"]/a')
    BTN_CART = (By.XPATH, '//div[@class="header"]')
    BTN_ACCOUNT = (By.XPATH, '//a[@class="account"]/span[@class="hidden-sm-down"]')


class Header(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in(self):
        self.move_to_element_and_click(HeaderLocators.BTN_SIGN_IN)

    def get_user_name(self):
        return self.get_text(HeaderLocators.BTN_ACCOUNT)
