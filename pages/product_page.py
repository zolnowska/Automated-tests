from pages.base import Base
from locators import product_page


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def choose_size(self, size='S'):
        if size in ['S', 'M', 'L', 'XL']:
            self.select_element_from_drop_down(product_page.DROP_DOWN_SIZE, size, 'text')

    def choose_paper_type(self, paper='Ruled'):
        if paper in ['Ruled', 'Plain', 'Squarred', 'Doted']:
            self.select_element_from_drop_down(product_page.DROP_DOWN_PAPER, paper, 'text')

    def choose_color(self, color="white"):
        if color == "white":
            self.wait_and_click(product_page.RADIO_COLOR_WHITE)
        elif color == "black":
            self.wait_and_click(product_page.RADIO_COLOR_BLACK)

    def get_current_price(self):
        return self.get_text(product_page.TEXT_CURRENT_PRICE)

    def get_regular_price(self):
        return self.get_text(product_page.TEXT_REGULAR_PRICE)

    def get_discount(self):
        return self.get_text(product_page.TEXT_DISCOUNT)

    def get_size(self):
        return self.get_text(product_page.BTN_SELECTED_SIZE)

    def get_paper_type(self):
        return self.get_text(product_page.BTN_SELECTED_PAPER)

    def increase_quantity(self, quantity=1):
        while quantity > 0:
            self.wait_and_click(product_page.BTN_INCREASE_QUANTITY)
            quantity = quantity - 1

    def decrease_quantity(self, quantity=1):
        while quantity > 0:
            self.wait_and_click(product_page.BTN_DECREASE_QUANTITY)
            quantity = quantity - 1

    def input_quantity(self, quantity):
        self.input(product_page.INPUT_QUANTITY, quantity)

    def get_product_availability(self):
        return self.get_text(product_page.TEXT_PRODUCT_AVAILABILITY)

    def click_add_to_cart(self):
        self.wait_and_click(product_page.BTN_ADD_TO_CART)

    # POPUP

    def click_proceed_to_checkout(self):
        self.wait_and_click(product_page.BTN_PROCEED_TO_CHECKOUT)






