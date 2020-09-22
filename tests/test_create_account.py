from selenium import webdriver
from pages.header import Header
from pages.log_in import LogIn
from pages.create_account import CreateAccount
from urls import urls
from test_data.generate_random_data import generate_unique_email
from test_data.manage_test_data import save_new_user
from datetime import datetime
import os


def test_create_account():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.home_page)
    email = generate_unique_email()
    gender = "male"
    first_name = "FirstName"
    last_name = "LastName"
    password = "test1"
    birthdate = "01/31/1969"
    try:
        header = Header(driver)
        header.click_sign_in()
        login_in = LogIn(driver)
        login_in.click_create_account()
        create_account = CreateAccount(driver)
        create_account.create_account(email, gender, first_name, last_name, password, birthdate)
        user_name = header.get_user_name()
        current_url = create_account.get_current_url()
        assert user_name == "FirstName LastName", "Test Passed"
        assert current_url == urls.home_page, "Test Passed"
        save_new_user(email, gender, first_name, last_name, password, birthdate, created="True")
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "create_account-%s.png" % now)
        save_new_user(email, gender, first_name, last_name, password, birthdate, created="Not_sure")
        driver.close()
        raise e


# test_data capslock
def test_create_account_used_email():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.home_page)
    email = "test@test.test"
    gender = "female"
    first_name = "FIRSTNAME"
    last_name = "LASTNAME"
    password = "qwerty12345"
    birthdate = "12/12/2000"
    try:
        header = Header(driver)
        header.click_sign_in()
        login_in = LogIn(driver)
        login_in.click_create_account()
        create_account = CreateAccount(driver)
        create_account.create_account(email, gender, first_name, last_name, password, birthdate)
        text_email_already_used = create_account.get_text_email_arleady_used()
        current_url = create_account.get_current_url()
        assert text_email_already_used == "The email is already used, please choose another one or sign in", \
            "Test Passed"
        assert current_url == urls.create_account, "Test Passed"
        save_new_user(email, gender, first_name, last_name, password, birthdate, created="False")
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "create_account_used_email_%s.png" % now)
        save_new_user(email, gender, first_name, last_name, password, birthdate, created="Not_sure")
        driver.close()
        raise e


# direct url, no birthdate, First and Last Name with space and -
def test_create_account_direct_url_no_birthdate():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    email = generate_unique_email()
    gender = "male"
    first_name = "Anna Alina"
    last_name = "Kowalska-Kukulska"
    password = "((Kokuwarku))!"
    brithdate = ""
    try:
        header = Header(driver)
        header.load_url(urls.create_account)
        create_account = CreateAccount(driver)
        create_account.create_account(email, gender, first_name, last_name, password)
        current_url = create_account.get_current_url()
        user_name = header.get_user_name()
        assert user_name == "Anna Alina Kowalska-Kukulska", "Test Passed"
        assert current_url == urls.home_page, "Test Passed"
        save_new_user(email, gender, first_name, last_name, password, brithdate, created="True")
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "create_account_direct_url_no_birthdate_%s.png" % now)
        save_new_user(email, gender, first_name, last_name, password, brithdate, created="Not_sure")
        driver.close()
        raise e


# input all correct, in opposite order

def test_create_account_opposite_order():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.home_page)
    email = generate_unique_email()
    gender = "female"
    first_name = "Фёдор Миха́йлович"
    last_name = "Достое́вский"
    password = "((((___AAAaaa)))"
    brithdate = "29/02/1992"
    try:
        header = Header(driver)
        header.click_sign_in()
        login_in = LogIn(driver)
        login_in.click_create_account()
        create_account = CreateAccount(driver)
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
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "create_account_opposite_order_%s.png" % now)
        save_new_user(email, gender, first_name, last_name, password, brithdate, created="Not_sure")
        driver.close()
        raise e
