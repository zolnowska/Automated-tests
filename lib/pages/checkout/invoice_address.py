from selenium.webdriver.common.by import By
from lib.pages.base import Base


class InvoiceAddressesLocators:
    INPUT_COMPANY = (By.XPATH, '//input[@name="company"]')
    INPUT_VAT = (By.XPATH, '//input[@name="vat_number"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@name="address1"]')
    INPUT_ADDRESS_COMPLEMENT = (By.XPATH, '//input[@name="address2"]')
    INPUT_CITY = (By.XPATH, '//input[@name="city"]')
    INPUT_POSTAL_CODE = (By.XPATH, '//input[@name="postcode"]')
    DROP_DOWN_COUNTRY = (By.XPATH, '//select[@name="id_country"]')
    INPUT_PHONE = (By.XPATH, '//input[@name="phone"]')
    BTN_CANCEL = (By.XPATH, '//a[@class="js-cancel-address cancel-address float-xs-right"]')
    BTN_CONTINUE = (By.XPATH, '//button[@name="confirm-addresses"]')


class InvoiceAddresses(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def minimal_addresses(self, address, city, postal_code):
        self.input(InvoiceAddressesLocators.INPUT_ADDRESS, address)
        self.input(InvoiceAddressesLocators.INPUT_CITY, city)
        self.input(InvoiceAddressesLocators.INPUT_POSTAL_CODE, postal_code)

    def full_addresses(self, address, city, postal_code, country, address_complement='', company='', vat='', phone=''):
        self.minimal_addresses(address, city, postal_code)
        self.input(InvoiceAddressesLocators.INPUT_COMPANY, company)
        self.input(InvoiceAddressesLocators.INPUT_VAT, vat)
        self.input(InvoiceAddressesLocators.INPUT_ADDRESS_COMPLEMENT, address_complement)
        self.select_element_from_drop_down(InvoiceAddressesLocators.DROP_DOWN_COUNTRY, country, 'text')
        self.input(InvoiceAddressesLocators.INPUT_PHONE, phone)

    def click_cancel(self):
        self.move_to_element_and_click(InvoiceAddressesLocators.BTN_CANCEL)

    def click_continue(self):
        self.move_to_element_and_click(InvoiceAddressesLocators.BTN_CONTINUE)
