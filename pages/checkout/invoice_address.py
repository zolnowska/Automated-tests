from pages.base import Base
from locators.cart import invoice_address


class InvoiceAddresses(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def minimal_addresses(self, address, city, postal_code):
        self.input(invoice_address.INPUT_ADDRESS, address)
        self.input(invoice_address.INPUT_CITY, city)
        self.input(invoice_address.INPUT_POSTAL_CODE, postal_code)

    def full_addresses(self, address, city, postal_code, country, address_complement='', company='', vat='', phone=''):
        self.minimal_addresses(address, city, postal_code)
        self.input(invoice_address.INPUT_COMPANY, company)
        self.input(invoice_address.INPUT_VAT, vat)
        self.input(invoice_address.INPUT_ADDRESS_COMPLEMENT, address_complement)
        self.select_element_from_drop_down(invoice_address.DROP_DOWN_COUNTRY, country, 'text')
        self.input(invoice_address.INPUT_PHONE, phone)

    def click_cancel(self):
        self.wait_and_click(invoice_address.BTN_CANCEL)

    def click_continue(self):
        self.wait_and_click(invoice_address.BTN_CONTINUE)