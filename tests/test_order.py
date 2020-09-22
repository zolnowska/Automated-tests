import pytest
from test_data.generate_random_data import generate_unique_email
from selenium import webdriver
from pages.home import Home
from pages.product_page import ProductPage
from pages.cart import Cart
from locators import urls
import os
from datetime import datetime
from pages.order_confirmation import OrderConfirmation


def test_order_hummingbird_printed_tshirt():
    driver = webdriver.Chrome('C:/bin/chromedriver')
    driver.maximize_window()
    driver.get(urls.home_page)
    size = 'L'
    color = 'black'
    increase_quantity = 5
    gender = 'male'
    first_name = 'Jan'
    last_name = 'Kowalski'
    email = generate_unique_email()
    address = 'Kościuszki 1'
    city = 'Kraków'
    postal_code = '30-030'
    shipping_method = 'My carrier'
    payment_method = 'Bank wire'
    try:
        home = Home(driver)
        home.click_hummingbird_printed_tshirt()
        product_page = ProductPage(driver)
        product_page.choose_size(size)
        product_page.choose_color(color)
        product_page.increase_quantity(increase_quantity)
        product_page.click_add_to_cart()
        product_page.click_proceed_to_checkout()
        cart = Cart(driver)
        cart.click_proceed_to_checkout()
        cart.order_as_guest(email, gender, first_name, last_name)
        cart.minimal_addresses(address, city, postal_code)
        cart.process_shipping(shipping_method)
        cart.process_payment(payment_method)
        order_confirmation = OrderConfirmation(driver)
        assert order_confirmation.get_information_1st_bought_item() == \
               'Hummingbird printed t-shirt - Size : L- Color : Black', 'Test Passed'
        assert order_confirmation.get_item_cost_1st_item() == '£22.94', 'Test Passed'
        assert order_confirmation.get_quantity_1st_item() == '6', 'Test Passed'
        assert order_confirmation.get_items_cost_1st_item() == '£137.66', 'Test Passed'
        assert order_confirmation.get_subtotal_cost() == '£137.66', 'Test Passed'
        assert order_confirmation.get_shipping_cost() == '£8.40', 'Test Passed'
        assert order_confirmation.get_total_cost() == '£146.06', 'Test Passed'
        driver.close()
    except Exception as e:
        try:
            os.makedirs("../screenshots")
        except FileExistsError:
            pass
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file("../screenshots/" + "order_hummingbird_printed_tshirt_%s.png" % now)
        driver.close()
        raise e
