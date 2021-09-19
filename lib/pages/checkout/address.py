from lib.pages.base import Base
from selenium.webdriver.common.by import By


class AddressesLocators:
    INPUT_COMPANY = (By.XPATH, '//input[@name="company"]')
    INPUT_VAT = (By.XPATH, '//input[@name="vat_number"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@name="address1"]')
    INPUT_ADDRESS_COMPLEMENT = (By.XPATH, '//input[@name="address2"]')
    INPUT_CITY = (By.XPATH, '//input[@name="city"]')
    INPUT_POSTAL_CODE = (By.XPATH, '//input[@name="postcode"]')
    DROP_DOWN_COUNTRY = (By.XPATH, '//select[@name="id_country"]')
    INPUT_PHONE = (By.XPATH, '//input[@name="phone"]')
    CHECKBOX_SAME_ADDRESS = (By.ID, 'use_same_address')
    BTN_CONTINUE = (By.XPATH, '//button[@name="confirm-addresses"]')


class Addresses(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def minimal_addresses(self, address_delivery, city, postal_code):
        self.input(AddressesLocators.INPUT_ADDRESS, address_delivery)
        self.input(AddressesLocators.INPUT_CITY, city)
        self.input(AddressesLocators.INPUT_POSTAL_CODE, postal_code)

    def full_addresses(self, address_delivery, city, postal_code, country, address_complement='', company='', vat='',
                       phone=''):
        self.minimal_addresses(address_delivery, city, postal_code)
        self.input(AddressesLocators.INPUT_COMPANY, company)
        self.input(AddressesLocators.INPUT_VAT, vat)
        self.input(AddressesLocators.INPUT_ADDRESS_COMPLEMENT, address_complement)
        self.select_element_from_drop_down(AddressesLocators.DROP_DOWN_COUNTRY, country, 'text')
        self.input(AddressesLocators.INPUT_PHONE, phone)

    def click_same_address_for_invoice(self):
        self.move_to_element_and_click(AddressesLocators.CHECKBOX_SAME_ADDRESS)

    def click_continue(self):
        self.move_to_element_and_click(AddressesLocators.BTN_CONTINUE)
