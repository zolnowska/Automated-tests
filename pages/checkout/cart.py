from locators.checkout import cart
from pages.base import Base


class Cart(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed_to_checkout(self):
        self.move_to_element_and_click(cart.BTN_PROCEED_TO_CHECKOUT)
