from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import os
import pytest
from datetime import datetime
from tests.urls.urls import Urls
from lib.pages.header import Header
from lib.pages.log_in import LogIn
from lib.pages.create_account import CreateAccount
from faker import Faker


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
    def test_correct_data(self):
        self.driver.get(Urls.HOME_PAGE)
        email = Faker().email()
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
            assert user_name == "FirstName LastName"
            assert current_url == Urls.HOME_PAGE
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestCreateAccount/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/correct_data-%s.png" % now)
            raise e

    # test_data capslock
    def test_used_email(self):
        self.driver.get(Urls.HOME_PAGE)
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
            assert text_email_already_used == "The email is already used, please choose another one or sign in"
            assert current_url == Urls.CREATE_ACCOUNT
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestCreateAccount/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/used_email_%s.png" % now)
            raise e

    # direct url, no birthdate, First and Last Name with space and -
    def test_direct_url_no_birthdate(self):
        email = Faker().email()
        gender = "male"
        first_name = "Anna Alina"
        last_name = "Kowalska-Kukulska"
        password = "((Kokuwarku))!"
        try:
            header = Header(self.driver)
            header.load_url(Urls.CREATE_ACCOUNT)
            create_account = CreateAccount(self.driver)
            create_account.create_account(email, gender, first_name, last_name, password)
            current_url = create_account.get_current_url()
            user_name = header.get_user_name()
            assert user_name == "Anna Alina Kowalska-Kukulska"
            assert current_url == Urls.HOME_PAGE
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestCreateAccount/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/direct_url_no_birthdate_%s.png" % now)
            raise e

    # input all correct, in opposite order
    def test_input_data_in_opposite_order(self):
        self.driver.get(Urls.HOME_PAGE)
        email = Faker().email()
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
            assert user_name == "Фёдор Миха́йлович Достое́вский"
            assert current_url == Urls.HOME_PAGE
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestCreateAccount/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/input_data_in_opposite_order_%s.png" % now)
            raise e
