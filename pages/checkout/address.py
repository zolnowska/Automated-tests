from pages.base import Base
from locators.checkout import address


class Addresses(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def minimal_addresses(self, address_delivery, city, postal_code):
        self.input(address.INPUT_ADDRESS, address_delivery)
        self.input(address.INPUT_CITY, city)
        self.input(address.INPUT_POSTAL_CODE, postal_code)

    def full_addresses(self, address_delivery, city, postal_code, country, address_complement='', company='', vat='',
                       phone=''):
        self.minimal_addresses(address_delivery, city, postal_code)
        self.input(address.INPUT_COMPANY, company)
        self.input(address.INPUT_VAT, vat)
        self.input(address.INPUT_ADDRESS_COMPLEMENT, address_complement)
        self.select_element_from_drop_down(address.DROP_DOWN_COUNTRY, country, 'text')
        self.input(address.INPUT_PHONE, phone)

    def click_same_address_for_invoice(self):
        self.move_to_element_and_click(address.CHECKBOX_SAME_ADDRESS)

    def click_continue(self):
        self.move_to_element_and_click(address.BTN_CONTINUE)
