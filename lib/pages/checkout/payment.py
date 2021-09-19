from selenium.webdriver.common.by import By
from lib.pages.base import Base


class PaymentLocators:
    RADIO_PAY_BY_CHECK = (By.XPATH, '//*[@id="payment-option-1-container"]/span')
    RADIO_PAY_BY_BANK_WIRE = (By.XPATH, '//*[@id="payment-option-2-container"]/span')
    CHECKBOX_TERMS = (By.XPATH, '//*[@id="conditions-to-approve"]/ul/li/div[1]/span')
    BTN_ORDER = (By.XPATH, '//button[@class="btn btn-primary center-block"]')


class Payment(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_payment_method(self, payment_method='Bank wire'):
        if payment_method == 'Bank wire':
            self.move_to_element_and_click(PaymentLocators.RADIO_PAY_BY_BANK_WIRE)
        elif payment_method == 'Check':
            self.move_to_element_and_click(PaymentLocators.RADIO_PAY_BY_CHECK)

    def process_payment(self, payment_method='Bank wire'):
        self.choose_payment_method(payment_method)
        self.move_to_element_and_click(PaymentLocators.CHECKBOX_TERMS)
        self.move_to_element_and_click(PaymentLocators.BTN_ORDER)
