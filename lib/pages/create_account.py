from selenium.webdriver.common.by import By
from lib.pages.base import Base
from faker import Faker


class CreateAccountLocators:
    RADIO_GENDER_MR = (By.XPATH, '//label[1]/span[@class="custom-radio"]')
    RADIO_GENDER_MRS = (By.XPATH, '//label[2]/span[@class="custom-radio"]')
    INPUT_FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
    INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    INPUT_BIRTHDATE = (By.XPATH, '//input[@name="birthday"]')
    CHECKBOX_CUSTOMER_PRIVACY = (By.XPATH, '//input[@name="customer_privacy"]')
    CHECKBOX_TERMS = (By.XPATH, '//input[@name="psgdpr"]')
    BTN_SAVE = (By.XPATH, '//*[@id="customer-form"]/footer/button')
    TEXT_EMAIL_ALREADY_USED = (By.XPATH, '//li[@class="alert alert-danger"]')


class CreateAccount(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_gender(self, gender="male"):
        if gender == "male":
            self.move_to_element_and_click(CreateAccountLocators.RADIO_GENDER_MR)
        elif gender == "female":
            self.move_to_element_and_click(CreateAccountLocators.RADIO_GENDER_MRS)

    def input_first_name(self, first_name="FirstName"):
        self.input(CreateAccountLocators.INPUT_FIRST_NAME, first_name)

    def input_last_name(self, last_name="LastName"):
        self.input(CreateAccountLocators.INPUT_LAST_NAME, last_name)

    def input_email(self, email=Faker().email()):
        self.input(CreateAccountLocators.INPUT_EMAIL, email)

    def input_password(self, password="test1"):
        self.input(CreateAccountLocators.INPUT_PASSWORD, password)

    def input_birthdate(self, birthdate="1969-01-31"):
        self.input(CreateAccountLocators.INPUT_BIRTHDATE, birthdate)

    def click_customer_privacy(self):
        self.move_to_element(CreateAccountLocators.CHECKBOX_CUSTOMER_PRIVACY)
        self.click(CreateAccountLocators.CHECKBOX_CUSTOMER_PRIVACY)

    def click_term(self):
        self.move_to_element(CreateAccountLocators.CHECKBOX_TERMS)
        self.click(CreateAccountLocators.CHECKBOX_TERMS)

    def click_save(self):
        self.move_to_element_and_click(CreateAccountLocators.BTN_SAVE)

    def create_account(self, email, gender, first_name, last_name, password, birthdate=""):
        self.choose_gender(gender)
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_email(email)
        self.input_password(password)
        self.input_birthdate(birthdate)
        self.click_term()
        self.click_customer_privacy()
        self.click_save()

    def get_text_email_already_used(self):
        return self.get_text(CreateAccountLocators.TEXT_EMAIL_ALREADY_USED)

    def get_text_first_name(self):
        return self.get_text(CreateAccountLocators.INPUT_FIRST_NAME)
