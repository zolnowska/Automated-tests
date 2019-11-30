import unittest
from selenium import webdriver
from pages.header import Header
from pages.log_in import LogIn
from pages.create_account import CreateAccount
from locators import urls
from random_data.generate_random_data import generate_unique_email
from random_data.generate_random_data import save_new_user
from datetime import datetime

from time import sleep


class CreateAccountTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('incognito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(urls.home_page)

    def test_create_account(self):
        email = generate_unique_email()
        gender = "male"
        first_name = "FirstName"
        last_name = "LastName"
        password = "test1"
        birthdate = "01/31/1969"
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.click_create_account()
            create_account = CreateAccount(self.driver)
            create_account.create_account(email, gender, first_name, last_name, password, birthdate)
            user_name = header.get_user_name()
            current_url = create_account.get_current_url()
            self.assertEqual(user_name, "FirstName LastName")
            self.assertEqual(current_url, urls.home_page)
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="True")
        except Exception as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/"+"create_account-%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="Not_sure")
            raise e

    #data capslock

    def test_create_account_used_email(self):
        email = "test@test.test"
        gender = "female"
        first_name = "FIRSTNAME"
        last_name = "LASTNAME"
        password = "qwerty12345"
        birthdate = "12/12/2000"
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.click_create_account()
            create_account = CreateAccount(self.driver)
            create_account.create_account(email, gender, first_name, last_name, password, birthdate)
            text_email_arleady_ussed = create_account.get_text_email_arleady_used()
            current_url = create_account.get_current_url()
            self.assertEqual(text_email_arleady_ussed, "The email is already used, please choose another one or sign in")
            self.assertEqual(current_url, urls.create_account)
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="False")
        except Exception as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/"+"create_account-%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="Not_sure")
            raise e


    #direct url, no birthdate, First and Last Name with space and -

    def test_create_account_direct_url_no_birthdate(self):
        email = generate_unique_email()
        gender = "male"
        first_name = "Anna Alina"
        last_name = "Kowalska-Kukulska"
        password = "((Kokuwarku))!"
        brithdate = ""
        try:
            header = Header(self.driver)
            header.load_url(urls.create_account)
            create_account = CreateAccount(self.driver)
            create_account.create_account(email, gender, first_name, last_name, password)
            current_url = create_account.get_current_url()
            user_name = header.get_user_name()
            self.assertEqual(user_name, "Anna Alina Kowalska-Kukulska")
            self.assertEqual(current_url, urls.home_page)
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="True")
        except Exception as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/"+"create_account-%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="Not_sure")
            raise e

    #input all correct, in opposite order

    def test_create_account_opposite_order(self):
        email = generate_unique_email()
        gender = "female"
        first_name = "Фёдор Миха́йлович"
        last_name = "Достое́вский"
        password = "((((___AAAaaa)))"
        brithdate = "29/02/1992"
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.click_create_account()
            create_account = CreateAccount(self.driver)
            create_account.input_birthdate(brithdate)
            create_account.input_password(password)
            create_account.input_email(email)
            create_account.input_last_name(last_name)
            create_account.input_first_name(first_name)
            create_account.choose_gender(gender)
            create_account.click_save()
            current_url = create_account.get_current_url()
            user_name = header.get_user_name()
            self.assertEqual(user_name, "Фёдор Миха́йлович Достое́вский")
            self.assertEqual(current_url, urls.home_page)
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="True")
        except Exception as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/"+"create_account-%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="Not_sure")
            raise e


    #input all correct, in mixed order except password, just press "SHOW" password



    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

