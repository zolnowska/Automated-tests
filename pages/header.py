from pages.base import Base
from locators import header


class Header(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in(self):
        self.move_to_element_and_click(header.BTN_SIGN_IN)

    def get_user_name(self):
        return self.get_text(header.BTN_ACCOUNT)
