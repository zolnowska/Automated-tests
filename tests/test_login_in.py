from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pytest
from pages.header import Header
from pages.log_in import LogIn
from urls import urls
import os
from datetime import datetime


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


class TestLoginIn(BasicTest):
    def test_correct_login_in(self):
        self.driver.get(urls.home_page)
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.log_in()
            user_name = header.get_user_name()
            current_url = login_in.get_current_url()
            assert user_name == "Test Test", "Test Passed"
            assert current_url == urls.my_account, "Test Passed"
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestLoginIn")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestLoginIn/" + "correct_login_in_%s.png" % now)
            raise e

    def test_login_in_incorrect_email(self):
        self.driver.get(urls.home_page)
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.log_in(email="test1@test.test")
            authentication_failed = login_in.get_text_authentication_failed()
            current_url = login_in.get_current_url()
            assert authentication_failed == "Authentication failed.", "Test Passed"
            assert current_url == urls.login_in, "Test Passed"
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestLoginIn")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestLoginIn/" + "login_in_incorrect_email_%s.png" % now)
            raise e

    def test_login_in_incorrect_password(self):
        self.driver.get(urls.home_page)
        try:
            header = Header(self.driver)
            header.click_sign_in()
            login_in = LogIn(self.driver)
            login_in.log_in(password="test2")
            authentication_failed = login_in.get_text_authentication_failed()
            current_url = login_in.get_current_url()
            assert authentication_failed == "Authentication failed.", "Test Passed"
            assert current_url == urls.login_in, "Test Passed"
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestLoginIn")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestLoginIn/" +
                                               "login_in_incorrect_password_%s.png" % now)
            raise e