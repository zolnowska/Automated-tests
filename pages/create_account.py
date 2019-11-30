from pages.base import Base
from locators import create_account
from random_data.generate_random_data import generate_unique_email
from random_data.generate_random_data import save_new_user


class CreateAccount(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_gender(self, gender="male"):
        if gender is "male":
            self.wait_and_click(create_account.RADIO_GENDER_MR)
        elif gender is "female":
            self.wait_and_click(create_account.RADIO_GENDER_MRS)

    def input_first_name(self, first_name="FirstName"):
        self.input(create_account.INPUT_FIRST_NAME, first_name)

    def input_last_name(self, last_name="LastName"):
        self.input(create_account.INPUT_LAST_NAME, last_name)

    def input_email(self, email=generate_unique_email()):
        self.input(create_account.INPUT_EMAIL, email)

    def input_password(self, password="test1"):
        self.input(create_account.INPUT_PASSWORD, password)

    def input_birthdate(self, birthdate="01/31/1969"):
        self.input(create_account.INPUT_BIRTHDATE, birthdate)

    def click_save(self):
        self.wait_and_click(create_account.BTN_SAVE)

    def create_account(self, email, gender, first_name, last_name, password, birthdate=""):
        self.choose_gender(gender)
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_email(email)
        self.input_password(password)
        self.input_birthdate(birthdate)
        self.click_save()

    def get_text_email_arleady_used(self):
        return self.get_text(create_account.TEXT_EMAIL_ALREADY_USED)

    def get_text_first_name(self):
        return self.get_text(create_account.INPUT_FIRST_NAME)

