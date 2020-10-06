from selenium.webdriver.common.by import By
from lib.pages.base import Base


class CartLocators:
    BTN_PROCEED_TO_CHECKOUT = (By.XPATH, '//div[@class="text-sm-center"]')


class Cart(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_proceed_to_checkout(self):
        self.move_to_element_and_click(CartLocators.BTN_PROCEED_TO_CHECKOUT)
