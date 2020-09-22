from selenium import webdriver
from pages.header import Header
from pages.log_in import LogIn
from urls import urls
import os
from datetime import datetime


def test_login_in():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.home_page)
    try:
        header = Header(driver)
        header.click_sign_in()
        login_in = LogIn(driver)
        login_in.log_in()
        user_name = header.get_user_name()
        current_url = login_in.get_current_url()
        assert user_name == "Test Test", "Test Passed"
        assert current_url == urls.my_account, "Test Passed"
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "login_in_%s.png" % now)
        driver.close()
        raise e


def test_login_in_incorrect_email():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.home_page)
    try:
        header = Header(driver)
        header.click_sign_in()
        login_in = LogIn(driver)
        login_in.log_in(email="test1@test.test")
        authentication_failed = login_in.get_text_authentication_failed()
        current_url = login_in.get_current_url()
        assert authentication_failed == "Authentication failed.", "Test Passed"
        assert current_url == urls.login_in, "Test Passed"
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "login_in_incorrect_email_%s.png" % now)
        driver.close()
        raise e


def test_login_in_incorrect_password():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.home_page)
    try:
        header = Header(driver)
        header.click_sign_in()
        login_in = LogIn(driver)
        login_in.log_in(password="test2")
        authentication_failed = login_in.get_text_authentication_failed()
        current_url = login_in.get_current_url()
        assert authentication_failed == "Authentication failed.", "Test Passed"
        assert current_url == urls.login_in, "Test Passed"
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "login_in_incorrect_password_%s.png" % now)
        driver.close()
        raise e
