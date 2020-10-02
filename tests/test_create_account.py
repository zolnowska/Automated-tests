from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pytest
from pages.header import Header
from pages.log_in import LogIn
from pages.create_account import CreateAccount
from urls import urls
from test_data.generate_random_data import generate_unique_email
from test_data.manage_test_data import save_new_user
from datetime import datetime
import os


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver_init(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--incoginito')
        web_driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    elif request.param == "firefox":
        firefox_options = Options()
        firefox_options.headless = True
        firefox_private = webdriver.FirefoxProfile()
        firefox_private.set_preference("browser.privatebrowsing.autostart", True)
        web_driver = Firefox(executable_path='../webdriver/geckodriver', options=firefox_options,
                             firefox_profile=firefox_private)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class TestCreateAccount(BasicTest):
    def test_correct_create_account(self):
        self.driver.get(urls.home_page)
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
            assert user_name == "FirstName LastName", "Test Passed"
            assert current_url == urls.home_page, "Test Passed"
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="True")
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestCreateAccount")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestCreateAccount/" +
                                               "correct_create_account-%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="Not_sure")
            raise e

    # test_data capslock
    def test_create_account_used_email(self):
        self.driver.get(urls.home_page)
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
            text_email_already_used = create_account.get_text_email_arleady_used()
            current_url = create_account.get_current_url()
            assert text_email_already_used == "The email is already used, please choose another one or sign in", \
                "Test Passed"
            assert current_url == urls.create_account, "Test Passed"
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="False")
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestCreateAccount")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestCreateAccount/" +
                                               "create_account_used_email_%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, birthdate, created="Not_sure")
            raise e

    # direct url, no birthdate, First and Last Name with space and -
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
            assert user_name == "Anna Alina Kowalska-Kukulska", "Test Passed"
            assert current_url == urls.home_page, "Test Passed"
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="True")
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestCreateAccount")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestCreateAccount/" +
                                               "create_account_direct_url_no_birthdate_%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="Not_sure")
            raise e

    # input all correct, in opposite order
    def test_create_account_opposite_order(self):
        self.driver.get(urls.home_page)
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
            create_account.click_term()
            create_account.input_birthdate(brithdate)
            create_account.input_password(password)
            create_account.input_email(email)
            create_account.input_last_name(last_name)
            create_account.input_first_name(first_name)
            create_account.choose_gender(gender)
            create_account.click_save()
            current_url = create_account.get_current_url()
            user_name = header.get_user_name()
            assert user_name == "Фёдор Миха́йлович Достое́вский", "Test passed"
            assert current_url == urls.home_page, "Test passed"
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="True")
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestCreateAccount")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestCreateAccount/" +
                                               "create_account_opposite_order_%s.png" % now)
            save_new_user(email, gender, first_name, last_name, password, brithdate, created="Not_sure")
            raise e
