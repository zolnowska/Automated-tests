import unittest
from selenium import webdriver
from pages.header import Header
from pages.log_in import LogIn
from locators import urls

import time


class LoginInTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('incoginito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(urls.home_page)

    def test_login_in(self):
        header = Header(self.driver)
        header.click_sign_in()
        login_in = LogIn(self.driver)
        login_in.log_in()
        user_name = header.get_user_name()
        current_url = login_in.get_current_url()
        self.assertEqual(user_name, "Test Test")
        self.assertEqual(current_url, urls.my_account)

    """
    # trzeba założyć konto dla seleniumprestashop@gmail.com
    def test_login_in_2(self):
        header = Header(self.driver)
        header.click_sign_in()
        login_in = LogIn(self.driver)
        email = users.user_2.get("USER_EMAIL")
        password = users.user_2.get("PASSWORD")
        login_in.log_in(email=email, password=password)
        user_name = header.get_user_name()
        current_url = login_in.get_current_url()
        self.assertEqual(1,1)
    """
    
    def test_login_in_incorrect_email(self):
        header = Header(self.driver)
        header.click_sign_in()
        login_in = LogIn(self.driver)
        login_in.log_in(email="test1@test.test")
        authentication_failed = login_in.get_text_authentication_failed()
        current_url = login_in.get_current_url()
        self.assertEqual(authentication_failed, "Authentication failed.")
        self.assertEqual(current_url, urls.login_in)

    def test_login_in_incorrect_password(self):
        header = Header(self.driver)
        header.click_sign_in()
        login_in = LogIn(self.driver)
        login_in.log_in(password="test2")
        authentication_failed = login_in.get_text_authentication_failed()
        current_url = login_in.get_current_url()
        self.assertEqual(authentication_failed, "Authentication failed.")
        self.assertEqual(current_url, urls.login_in)

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
