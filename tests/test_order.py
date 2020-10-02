from test_data.generate_random_data import generate_unique_email
from test_data.generate_random_data import generate_birthdate
from test_data.generate_random_data import generate_password
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import pytest
from pages.home import Home
from pages.product_page import ProductPage
from pages.checkout.cart import Cart
from pages.checkout.personal_information import PersonalInformation
from pages.checkout.address import Addresses
from pages.checkout.invoice_address import InvoiceAddresses
from pages.checkout.shipping import Shipping
from pages.checkout.payment import Payment
from pages.order_confirmation import OrderConfirmation
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


class TestOrder(BasicTest):
    def test_order_hummingbird_printed_tshirt(self):
        self.driver.get(urls.home_page)
        try:
            home = Home(self.driver)
            home.click_hummingbird_printed_tshirt()
            product_page = ProductPage(self.driver)
            product_page.choose_size('L')
            product_page.choose_color('black')
            product_page.increase_quantity(5)
            product_page.click_add_to_cart()
            product_page.click_proceed_to_checkout()
            Cart(self.driver).click_proceed_to_checkout()
            personal_information = PersonalInformation(self.driver)
            personal_information.order_as_guest(generate_unique_email(), 'male', 'Jan', 'Kowalski')
            personal_information.click_continue()
            address = Addresses(self.driver)
            address.minimal_addresses('Kościuszki 1', 'Kraków', '30-030')
            address.click_continue()
            Shipping(self.driver).process_shipping('My carrier')
            Payment(self.driver).process_payment('Bank wire')
            order_confirmation = OrderConfirmation(self.driver)
            assert order_confirmation.get_information_1st_bought_item() == \
                   'Hummingbird printed t-shirt - Size : L- Color : Black', 'Test Passed'
            assert order_confirmation.get_item_cost_1st_item() == '£22.94', 'Test Passed'
            assert order_confirmation.get_quantity_1st_item() == '6', 'Test Passed'
            assert order_confirmation.get_items_cost_1st_item() == '£137.66', 'Test Passed'
            assert order_confirmation.get_subtotal_cost() == '£137.66', 'Test Passed'
            assert order_confirmation.get_shipping_cost() == '£8.40', 'Test Passed'
            assert order_confirmation.get_total_cost() == '£146.06', 'Test Passed'

        except Exception as e:
            try:
                os.makedirs("../screenshots/TestOrder")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestOrder/" +
                                               "order_hummingbird_printed_tshirt_%s.png" % now)
            raise e

    def test_order_brown_bear_cushion(self):
        self.driver.get(urls.product_page_brown_bear_cushion)
        try:
            product_page = ProductPage(self.driver)
            product_page.choose_color('white')
            product_page.increase_quantity(5)
            product_page.decrease_quantity(2)
            product_page.click_add_to_cart()
            product_page.click_proceed_to_checkout()
            Cart(self.driver).click_proceed_to_checkout()
            personal_information = PersonalInformation(self.driver)
            personal_information.create_account(generate_unique_email(), generate_password(), 'female', 'Léa',
                                                'Bàçrthèïs', generate_birthdate())
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
                   'Brown bear cushion - Color : White', 'Test Passed'
            assert order_confirmation.get_item_cost_1st_item() == '£22.68', 'Test Passed'
            assert order_confirmation.get_quantity_1st_item() == '4', 'Test Passed'
            assert order_confirmation.get_items_cost_1st_item() == '£90.72', 'Test Passed'
            assert order_confirmation.get_subtotal_cost() == '£90.72', 'Test Passed'
            assert order_confirmation.get_shipping_cost() == 'Free', 'Test Passed'
            assert order_confirmation.get_total_cost() == '£90.72', 'Test Passed'
        except Exception as e:
            try:
                os.makedirs("../screenshots/TestOrder")
            except FileExistsError:
                pass
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file("../screenshots/TestOrder/" +
                                               "order_brown_bear_cushion-%s.png" % now)
            raise e
