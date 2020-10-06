from selenium.webdriver.common.by import By
from lib.pages.base import Base
from faker import Faker


class PersonalInformationLocators:
    RADIO_GENDER_MR = (By.XPATH, '//label[1]/span[@class="custom-radio"]')
    RADIO_GENDER_MRS = (By.XPATH, '//label[2]/span[@class="custom-radio"]')
    INPUT_FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
    INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    INPUT_BIRTHDATE = (By.XPATH, '//input[@name="birthday"]')
    CHECKBOX_TERMS = (By.XPATH, '//div[9]/div[@class="col-md-6"]/span/label')
    BTN_CONTINUE = (By.XPATH, '//*[@id="customer-form"]/footer/button')
    TEXT_EMAIL_ALREADY_USED = (By.XPATH, '//li[@class="alert alert-danger"]')


class PersonalInformation(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_gender(self, gender="male"):
        if gender == "male":
            self.move_to_element_and_click(PersonalInformationLocators.RADIO_GENDER_MR)
        elif gender == "female":
            self.move_to_element_and_click(PersonalInformationLocators.RADIO_GENDER_MRS)

    def input_first_name(self, first_name="FirstName"):
        self.input(PersonalInformationLocators.INPUT_FIRST_NAME, first_name)

    def input_last_name(self, last_name="LastName"):
        self.input(PersonalInformationLocators.INPUT_LAST_NAME, last_name)

    def input_email(self, email=Faker().email):
        self.input(PersonalInformationLocators.INPUT_EMAIL, email)

    def input_password(self, password="test1"):
        self.input(PersonalInformationLocators.INPUT_PASSWORD, password)

    def input_birthdate(self, birthdate="01/31/1969"):
        self.input(PersonalInformationLocators.INPUT_BIRTHDATE, birthdate)

    def click_term(self):
        self.move_to_element_and_click(PersonalInformationLocators.CHECKBOX_TERMS)

    def order_as_guest(self, email, gender, first_name, last_name):
        self.choose_gender(gender)
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_email(email)
        self.click_term()

    def create_account(self, email, password, gender, first_name, last_name, birthdate=""):
        self.order_as_guest(email, gender, first_name, last_name)
        self.input_password(password)
        self.input_birthdate(birthdate)

    def click_continue(self):
        self.move_to_element_and_click(PersonalInformationLocators.BTN_CONTINUE)
