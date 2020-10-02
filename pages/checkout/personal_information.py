from pages.base import Base
from locators.checkout import personal_information
from test_data.generate_random_data import generate_unique_email


class PersonalInformation(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_gender(self, gender="male"):
        if gender == "male":
            self.move_to_element_and_click(personal_information.RADIO_GENDER_MR)
        elif gender == "female":
            self.move_to_element_and_click(personal_information.RADIO_GENDER_MRS)

    def input_first_name(self, first_name="FirstName"):
        self.input(personal_information.INPUT_FIRST_NAME, first_name)

    def input_last_name(self, last_name="LastName"):
        self.input(personal_information.INPUT_LAST_NAME, last_name)

    def input_email(self, email=generate_unique_email()):
        self.input(personal_information.INPUT_EMAIL, email)

    def input_password(self, password="test1"):
        self.input(personal_information.INPUT_PASSWORD, password)

    def input_birthdate(self, birthdate="01/31/1969"):
        self.input(personal_information.INPUT_BIRTHDATE, birthdate)

    def click_term(self):
        self.move_to_element_and_click(personal_information.CHECKBOX_TERMS)

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
        self.move_to_element_and_click(personal_information.BTN_CONTINUE)
