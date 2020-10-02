from locators.checkout import payment
from pages.base import Base


class Payment(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_payment_method(self, payment_method='Bank wire'):
        if payment_method == 'Bank wire':
            self.move_to_element_and_click(payment.RADIO_PAY_BY_BANK_WIRE)
        elif payment_method == 'Check':
            self.move_to_element_and_click(payment.RADIO_PAY_BY_CHECK)

    def process_payment(self, payment_method='Bank wire'):
        self.choose_payment_method(payment_method)
        self.move_to_element_and_click(payment.CHEKBOX_TERMS)
        self.move_to_element_and_click(payment.BTN_ORDER)
