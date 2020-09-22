from selenium import webdriver
from pages.home import Home
from pages.product_list.clothes_women import ClothesWomen
from pages.product_list.accessories_stationery import AccessoriesStationery
from pages.product_page import ProductPage
from urls import urls
import os
from datetime import datetime


def test_correct_information():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.home_page)
    try:
        home = Home(driver)
        home.click_clothes_women()
        ClothesWomen(driver).click_hummingbird_printed_sweater()
        product_page = ProductPage(driver)
        assert product_page.get_regular_price() == '£43.08', 'Test Passed'
        assert product_page.get_current_price() == '£34.46', 'Test Passed'
        assert product_page.get_discount() == 'SAVE 20%', 'Test Passed'
        assert product_page.get_size() == 'S', 'Test Passed'
        assert product_page.get_product_availability('') == '', 'Test Passed'
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "test_correct_information_product_page_%s.png" % now)
        driver.close()
        raise e


def test_product_unavailability():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incoginito')
    driver = webdriver.Chrome(executable_path='../webdriver/chromedriver', options=chrome_options)
    driver.maximize_window()
    driver.get(urls.product_list_accessories_stationery)
    try:
        AccessoriesStationery(driver).click_mountain_fox_notebook()
        product_page = ProductPage(driver)
        product_page.choose_paper_type('Squarred')
        product_page.input_quantity(1000000)
        assert product_page.get_current_price() == '£15.48', 'Test Passed'
        assert product_page.get_paper_type('Squarred') == 'Squarred', 'Test Passed'
        assert product_page.get_product_availability(' There are not enough products in stock') == \
               ' There are not enough products in stock', 'Test Passed'
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "test_correct_information_product_page_%s.png" % now)
        driver.close()
        raise e
