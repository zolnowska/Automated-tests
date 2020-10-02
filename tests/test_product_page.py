from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pytest
from pages.home import Home
from pages.product_list.clothes_women import ClothesWomen
from pages.product_list.accessories_stationery import AccessoriesStationery
from pages.product_page import ProductPage
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


class TestProductPage(BasicTest):
    def test_correct_information(self):
        self.driver.get(urls.home_page)
        try:
            home = Home(self.driver)
            home.click_clothes_women()
            ClothesWomen(self.driver).click_hummingbird_printed_sweater()
            product_page = ProductPage(self.driver)
            assert product_page.get_regular_price() == '£43.08', 'Test Passed'
            assert product_page.get_current_price() == '£34.46', 'Test Passed'
            assert product_page.get_discount() == 'SAVE 20%', 'Test Passed'
            assert product_page.get_size() == 'S', 'Test Passed'
            assert product_page.get_product_availability() == '', 'Test Passed'
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestProductPage")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestProductPage" +
                                               "correct_information-%s.png" % now)
            raise e

    def test_product_unavailability(self):
        self.driver.get(urls.product_list_accessories_stationery)
        try:
            AccessoriesStationery(self.driver).click_mountain_fox_notebook()
            product_page = ProductPage(self.driver)
            product_page.choose_paper_type('Squarred')
            product_page.input_quantity(1000000)
            assert product_page.get_current_price() == '£15.48', 'Test Passed'
            assert product_page.get_selected_paper_type_squarred() == 'Squarred', 'Test Passed'
            assert product_page.get_product_availability() == ' There are not enough products in stock', 'Test Passed'
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestProductPage")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestProductPage/" +
                                               "product_unavailability-%s.png" % now)
            raise e
