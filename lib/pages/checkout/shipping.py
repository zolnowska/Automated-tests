from selenium.webdriver.common.by import By
from lib.pages.base import Base


class ShippingLocators:
    RADIO_PRESTASHOP = (By.XPATH, '//*[@id="js-delivery"]/div/div[1]/div[1]/div/span')
    RADIO_MY_CARRIER = (By.XPATH, '//*[@id="js-delivery"]/div/div[1]/div[4]/div/span')
    BUTTON_CONTINUE = (By.XPATH, '//button[@name="confirmDeliveryOption"]')


class Shipping(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_shipping_method(self, shipping_method='My carrier'):
        if shipping_method == 'Prestashop':
            self.wait_and_click(ShippingLocators.RADIO_PRESTASHOP)
        elif shipping_method == 'My carrier':
            self.wait_and_click(ShippingLocators.RADIO_MY_CARRIER)

    def click_continue(self):
        self.wait_and_click(ShippingLocators.BUTTON_CONTINUE)

    def process_shipping(self, shipping_method='My carrier'):
        self.choose_shipping_method(shipping_method)
        self.click_continue()
