from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import os
import pytest
from datetime import datetime
from tests.urls.urls import Urls
from lib.pages.home import Home
from lib.pages.product_page import ProductPage
from lib.pages.product_list.clothes_women import ClothesWomen
from lib.pages.product_list.accessories_stationery import AccessoriesStationery


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


class TestProductPage(BasicTest):
    def test_correct_information(self):
        self.driver.get(Urls.HOME_PAGE)
        try:
            home = Home(self.driver)
            home.click_clothes_women()
            ClothesWomen(self.driver).click_hummingbird_printed_sweater()
            product_page = ProductPage(self.driver)
            assert product_page.get_regular_price() == '£43.08'
            assert product_page.get_current_price() == '£34.46'
            assert product_page.get_discount() == 'SAVE 20%'
            assert product_page.get_size() == 'S'
            assert product_page.get_product_availability() == ''
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestProductPage/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir +
                                               "/correct_information-%s.png" % now)
            raise e

    def test_product_unavailability(self):
        self.driver.get(Urls.PRODUCT_LIST_ACCESSORIES_STATIONARY)
        try:
            AccessoriesStationery(self.driver).click_mountain_fox_notebook()
            product_page = ProductPage(self.driver)
            product_page.choose_paper_type('Squarred')
            product_page.input_quantity(1000000)
            assert product_page.get_current_price() == '£15.48'
            assert product_page.get_selected_paper_type_squarred() == 'Squarred'
            assert product_page.get_product_unavailability() == ' There are not enough products in stock'
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestProductPage/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir +
                                               "/product_unavailability_%s.png" % now)
            raise e
