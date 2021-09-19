from selenium.webdriver.common.by import By
from configuration import DEFAULT_SELENIUM_WAIT_SECONDS
from lib.pages.base import Base
from selenium.common.exceptions import StaleElementReferenceException


class ProductPageLocators:

    TEXT_REGULAR_PRICE = (By.XPATH, '//span[@class="regular-price"]')
    TEXT_CURRENT_PRICE = (By.XPATH, '//div[@class="current-price"]/span[@itemprop="price"]')
    TEXT_DISCOUNT = (By.XPATH, '//span[@class="discount discount-percentage"]')
    DROP_DOWN_SIZE = (By.ID, 'group_1')
    DROP_DOWN_PAPER = (By.ID, 'group_4')
    BTN_SELECTED_SIZE = (By.XPATH, '//*[@id="group_1"]/option[@selected="selected"]')
    BTN_SELECTED_PAPER_SQUARRED = (By.XPATH, '//*[@id="group_4"]/option[@selected="selected" and @title="Squarred"]')
    BTN_ADD_TO_CART = (By.XPATH, '//button[@class="btn btn-primary add-to-cart"]')
    RADIO_COLOR_WHITE = (By.XPATH, '//input[@class="input-color" and @title="White"]')
    RADIO_COLOR_BLACK = (By.XPATH, '//input[@class="input-color" and @title="Black"]')
    INPUT_QUANTITY = (By.ID, 'quantity_wanted')
    TEXT_PRODUCT_AVAILABILITY = (By.ID, 'product-availability')
    SYMBOL_PRODUCT_UNAVAILABILITY = (By.XPATH, '//span[@id="product-availability"]/i')
    BTN_INCREASE_QUANTITY = (By.XPATH, '//button[@class="btn btn-touchspin js-touchspin bootstrap-touchspin-up"]')
    BTN_DECREASE_QUANTITY = (By.XPATH, '//button[@class="btn btn-touchspin js-touchspin bootstrap-touchspin-down"]')
    IMG_HUMMINGBIRD_PRINTED_TSHIRT_BLACK = \
        (By.XPATH, '//img[@src="http://127.0.0.1/prestashop/1-large_default/hummingbird-printed-t-shirt.jpg"]')

    # Popup Add to Cart
    BTN_PROCEED_TO_CHECKOUT = (By.XPATH, '//a[@class="btn btn-primary"]')
    BTN_CONTINUE_SHOPPING = (By.XPATH, '//button[@class="btn btn-secondary"]')


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_size(self, size='S'):
        if size in ['S', 'M', 'L', 'XL']:
            self.select_element_from_drop_down(ProductPageLocators.DROP_DOWN_SIZE, size, 'text')

    def choose_paper_type(self, paper='Ruled'):
        if paper in ['Ruled', 'Plain', 'Squarred', 'Doted']:
            self.select_element_from_drop_down(ProductPageLocators.DROP_DOWN_PAPER, paper, 'text')

    def choose_color(self, color="white"):
        if color == "white":
            self.wait_until_element(ProductPageLocators.RADIO_COLOR_WHITE)
            self.click(ProductPageLocators.RADIO_COLOR_WHITE)
        elif color == "black":
            self.wait_until_element(ProductPageLocators.RADIO_COLOR_BLACK)
            self.click(ProductPageLocators.RADIO_COLOR_BLACK)

    def wait_until_hummingbird_printed_tshirt(self):
        self.wait_until_element(ProductPageLocators.IMG_HUMMINGBIRD_PRINTED_TSHIRT_BLACK)

    def get_current_price(self):
        return self.get_text(ProductPageLocators.TEXT_CURRENT_PRICE)

    def get_regular_price(self):
        return self.get_text(ProductPageLocators.TEXT_REGULAR_PRICE)

    def get_discount(self):
        return self.get_text(ProductPageLocators.TEXT_DISCOUNT)

    def get_size(self):
        return self.get_text(ProductPageLocators.BTN_SELECTED_SIZE)

    def get_selected_paper_type_squarred(self, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        try:
            return self.get_text(ProductPageLocators.BTN_SELECTED_PAPER_SQUARRED)
        except StaleElementReferenceException:
            self.get_selected_paper_type_squarred(timeout)

    def increase_quantity_by(self, quantity=1):
        while quantity > 0:
            self.move_to_element_and_click(ProductPageLocators.BTN_INCREASE_QUANTITY)
            quantity = quantity - 1

    def decrease_quantity_by(self, quantity=1):
        while quantity > 0:
            self.move_to_element_and_click(ProductPageLocators.BTN_DECREASE_QUANTITY)
            quantity = quantity - 1

    def input_quantity(self, quantity):
        self.input(ProductPageLocators.INPUT_QUANTITY, quantity)

    def get_product_availability(self, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        return self.get_text(ProductPageLocators.TEXT_PRODUCT_AVAILABILITY, timeout)

    def get_product_unavailability(self, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        self.wait_until_element(ProductPageLocators.SYMBOL_PRODUCT_UNAVAILABILITY)
        return self.get_text(ProductPageLocators.TEXT_PRODUCT_AVAILABILITY, timeout)

    def click_add_to_cart(self):
        self.wait_until_element(ProductPageLocators.BTN_ADD_TO_CART)
        self.move_to_element_and_click(ProductPageLocators.BTN_ADD_TO_CART)

    # POPUP

    def click_proceed_to_checkout(self):
        self.wait_until_element(ProductPageLocators.BTN_PROCEED_TO_CHECKOUT)
        self.wait_until_is_visibility(ProductPageLocators.BTN_PROCEED_TO_CHECKOUT)
        self.move_to_element_and_click(ProductPageLocators.BTN_PROCEED_TO_CHECKOUT)
