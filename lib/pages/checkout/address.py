from lib.pages.base import Base
from selenium.webdriver.common.by import By


class AddressesLocators:
    INPUT_COMPANY = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[3]/div[1]')
    INPUT_VAT = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[4]/div[1]')
    INPUT_ADDRESS = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[5]/div[1]')
    INPUT_ADDRESS_COMPLEMENT = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[6]/div[1]')
    INPUT_CITY = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[7]/div[1]')
    INPUT_POSTAL_CODE = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[8]/div[1]')
    DROP_DOWN_COUNTRY = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[9]/div[1]/select')
    INPUT_PHONE = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[10]/div[1]')
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
