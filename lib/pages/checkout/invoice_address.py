from selenium.webdriver.common.by import By
from lib.pages.base import Base


class InvoiceAddressesLocators:
    INPUT_COMPANY = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[3]/div[1]/input')
    INPUT_VAT = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[4]/div[1]/input')
    INPUT_ADDRESS = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[5]/div[1]/input')
    INPUT_ADDRESS_COMPLEMENT = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[6]/div[1]/input')
    INPUT_CITY = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[7]/div[1]/input')
    INPUT_POSTAL_CODE = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[8]/div[1]')
    DROP_DOWN_COUNTRY = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[9]/div[1]/select')
    INPUT_PHONE = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[10]/div[1]')
    BTN_CANCEL = (By.XPATH, '//*[@id="invoice-address"]/div/footer/a')
    BTN_CONTINUE = (By.XPATH, '//*[@id="invoice-address"]/div/footer/button')


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
