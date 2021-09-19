from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import os
import pytest
from datetime import datetime
from faker import Faker
from tests.urls.urls import Urls
from lib.pages.home import Home
from lib.pages.product_page import ProductPage
from lib.pages.order_confirmation import OrderConfirmation
from lib.pages.checkout.cart import Cart
from lib.pages.checkout.personal_information import PersonalInformation
from lib.pages.checkout.address import Addresses
from lib.pages.checkout.invoice_address import InvoiceAddresses
from lib.pages.checkout.shipping import Shipping
from lib.pages.checkout.payment import Payment

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
    web_driver.stop_client()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class TestOrder(BasicTest):


    def test_hummingbird_printed_tshirt_minimal_address(self):
        self.driver.get(Urls.HOME_PAGE)
        home = Home(self.driver)
        home.click_hummingbird_printed_tshirt()
        product_page = ProductPage(self.driver)
        product_page.choose_size('L')
        product_page.choose_color('black')
        product_page.increase_quantity_by(5)
        product_page.click_add_to_cart()
        product_page.click_proceed_to_checkout()
        Cart(self.driver).click_proceed_to_checkout()

    # order product as guest with minimal necessary data in address
    def test_hummingbird_printed_tshirt_minimal_address(self):
        self.driver.get(Urls.HOME_PAGE)
        try:
            home = Home(self.driver)
            home.click_hummingbird_printed_tshirt()
            product_page = ProductPage(self.driver)
            product_page.choose_size('L')
            product_page.choose_color('black')
            product_page.wait_until_hummingbird_printed_tshirt()
            product_page.increase_quantity_by(5)
            product_page.click_add_to_cart()
            product_page.click_proceed_to_checkout()
            Cart(self.driver).click_proceed_to_checkout()
            personal_information = PersonalInformation(self.driver)
            personal_information.order_as_guest(Faker().email(), 'male', 'Jan', 'Kowalski')
            personal_information.click_continue()
            address = Addresses(self.driver)
            address.minimal_addresses('Kościuszki 1', 'Kraków', '30-030')
            address.click_continue()
            Shipping(self.driver).process_shipping('My carrier')
            Payment(self.driver).process_payment('Bank wire')
            order_confirmation = OrderConfirmation(self.driver)
            assert order_confirmation.get_information_1st_bought_item() == \
                   'Hummingbird printed t-shirt - Size : L- Colour : Black'
            assert order_confirmation.get_item_cost_1st_item() == '£22.94'
            assert order_confirmation.get_quantity_1st_item() == '6'
            assert order_confirmation.get_items_cost_1st_item() == '£137.66'
            assert order_confirmation.get_subtotal_cost() == '£137.66'
            assert order_confirmation.get_shipping_cost() == '£8.40'
            assert order_confirmation.get_total_cost() == '£146.06'

        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestOrder/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir +
                                               "/hummingbird_printed_tshirt_minimal_address_%s.png" % now)
            raise e

    # order as guest with all data in address including invoice address
    def test_brown_bear_cushion_full_address(self):
        self.driver.get(Urls.PRODUCT_PAGE_BROWN_BEAR_CUSHION)
        try:
            product_page = ProductPage(self.driver)
            product_page.choose_color('white')
            product_page.increase_quantity_by(5)
            product_page.decrease_quantity_by(2)
            product_page.click_add_to_cart()
            product_page.click_proceed_to_checkout()
            Cart(self.driver).click_proceed_to_checkout()
            personal_information = PersonalInformation(self.driver)
            personal_information.create_account(Faker().email(), Faker().password(), 'female', 'Léa',
                                                'Bàçrthèïs', str(Faker().date_of_birth()))
            personal_information.click_continue()
            address = Addresses(self.driver)
            address.full_addresses('Kośćźąłñń 1', 'Káâãéêíóôõúü', '30030', 'United Kingdom', 'mięó 12', 'Qæøiå',
                                   '1234567890', '+48121212121')
            address.click_same_address_for_invoice()
            address.click_continue()
            invoice_address = InvoiceAddresses(self.driver)
            invoice_address.full_addresses('Száâãéêíóôõúü 99A', 'Wróośćźąłñń', '00-000', 'United Kingdom', 'Lmięó 12',
                                           'Pwqåæøi', '091', '+13484848484')
            invoice_address.click_continue()
            Shipping(self.driver).process_shipping('Prestashop')
            Payment(self.driver).process_payment('Check')
            order_confirmation = OrderConfirmation(self.driver)
            assert order_confirmation.get_information_1st_bought_item() == \
                   'Brown bear cushion - Colour : White', 'Test Passed'
            assert order_confirmation.get_item_cost_1st_item() == '£22.68'
            assert order_confirmation.get_quantity_1st_item() == '4'
            assert order_confirmation.get_items_cost_1st_item() == '£90.72'
            assert order_confirmation.get_subtotal_cost() == '£90.72'
            assert order_confirmation.get_shipping_cost() == 'Free'
            assert order_confirmation.get_total_cost() == '£90.72'
        except Exception as e:
            day = datetime.now().strftime('%Y%m%d')
            name_dir = "../reports/" + day + "/TestOrder/screenshots"
            try:
                os.makedirs(name_dir)
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.driver.get_screenshot_as_file(name_dir +
                                               "/brown_bear_cushion_full_address_%s.png" % now)
            raise e
