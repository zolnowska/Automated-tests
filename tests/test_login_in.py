from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pytest
import os
from datetime import datetime
from tests.urls.urls import Urls
from lib.pages.header import Header
from lib.pages.log_in import LogIn


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver_init(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--incoginito')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
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


class TestLoginIn(BasicTest):
    def test_correct_data(self):
        self.driver.get(Urls.HOME_PAGE)
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.log_in()
            user_name = header.get_user_name()
            current_url = login_in.get_current_url()
            assert user_name == "Test Test"
            assert current_url == Urls.MY_ACCOUNT
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestLoginIn/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/correct_data_%s.png" % now)
            raise e

    def test_incorrect_email(self):
        self.driver.get(Urls.HOME_PAGE)
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.log_in(email="test1@test.test")
            authentication_failed = login_in.get_text_authentication_failed()
            current_url = login_in.get_current_url()
            assert authentication_failed == "Authentication failed."
            assert current_url == Urls.LOGIN_IN
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestLoginIn/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/incorrect_email_%s.png" % now)
            raise e

    def test_incorrect_password(self):
        self.driver.get(Urls.HOME_PAGE)
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.log_in(password="test2")
            authentication_failed = login_in.get_text_authentication_failed()
            current_url = login_in.get_current_url()
            assert authentication_failed == "Authentication failed."
            assert current_url == Urls.LOGIN_IN
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestLoginIn/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir +
                                               "/incorrect_password_%s.png" % now)
            raise e

    def test_no_email_no_password(self):
        self.driver.get(Urls.LOGIN_IN)
        try:
            login_in = LogIn(self.driver)
            login_in.click_sign_in()
            current_url = login_in.get_current_url()
            assert current_url == Urls.LOGIN_IN
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestLoginIn/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/no_email_no_password_%s.png" % now)
            raise e

    def test_no_email(self):
        self.driver.get(Urls.LOGIN_IN)
        try:
            login_in = LogIn(self.driver)
            login_in.input_password("test12345")
            login_in.click_sign_in()
            current_url = login_in.get_current_url()
            assert current_url == Urls.LOGIN_IN
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestLoginIn/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/no_email_%s.png" % now)
            raise e

    def test_no_password(self):
        self.driver.get(Urls.LOGIN_IN)
        try:
            login_in = LogIn(self.driver)
            login_in.input_email("test12345@mail.com")
            login_in.click_sign_in()
            current_url = login_in.get_current_url()
            assert current_url == Urls.LOGIN_IN
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestLoginIn/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir + "/no_password_%s.png" % now)
            raise e