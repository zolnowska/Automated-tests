from locators.checkout import shipping
from pages.base import Base


class Shipping(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_shipping_method(self, shipping_method='My carrier'):
        if shipping_method == 'Prestashop':
            self.wait_and_click(shipping.RADIO_PRESTASHOP)
        elif shipping_method == 'My carrier':
            self.wait_and_click(shipping.RADIO_MY_CARRIER)

    def click_continue(self):
        self.wait_and_click(shipping.BUTTON_CONTINUE)

    def process_shipping(self, shipping_method='My carrier'):
        self.choose_shipping_method(shipping_method)
        self.click_continue()
