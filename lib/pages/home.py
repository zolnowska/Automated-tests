from selenium.webdriver.common.by import By
from lib.pages.base import Base


class HomeLocators:
    # HEADER NAVIGATION
    BTN_CLOTHES = (By.ID, 'category-3')
    BTN_CLOTHES_MEN = (By.ID, 'category-4')
    BTN_CLOTHES_WOMEN = (By.ID, 'category-5')
    BTN_ACCESSORIES = (By.ID, 'category-6')
    BTN_STATIONERY = (By.ID, 'category-7')
    BTN_HOME_ACCESSORIES = (By.ID, 'category-8')
    BTN_ART = (By.ID, 'category-9')

    # POPULAR PRODUCTS
    BTN_HUMMINGBIRD_PRINTED_TSHIRT = (By.XPATH, '//article[@data-id-product="1"]')
    BTN_TODAY_IS_A_GOOD_DAY_FRAMED = (By.XPATH, '//article[@data-id-product="5"]')

    # FOOTER
    BTN_PRICES_DROP = (By.ID, 'link-product-page-prices-drop-1')


class Home(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_clothes(self):
        self.move_to_element_and_click(HomeLocators.BTN_CLOTHES)

    def click_clothes_men(self):
        self.move_to_element(HomeLocators.BTN_CLOTHES)
        self.wait_and_click(HomeLocators.BTN_CLOTHES_MEN)

    def click_clothes_women(self):
        self.move_to_element(HomeLocators.BTN_CLOTHES)
        self.wait_and_click(HomeLocators.BTN_CLOTHES_WOMEN)

    def click_accessories(self):
        self.move_to_element_and_click(HomeLocators.BTN_ACCESSORIES)

    def click_stationery(self):
        self.move_to_element(HomeLocators.BTN_ACCESSORIES)
        self.wait_and_click(HomeLocators.BTN_STATIONERY)

    def click_home_accessories(self):
        self.move_to_element(HomeLocators.BTN_ACCESSORIES)
        self.wait_and_click(HomeLocators.BTN_HOME_ACCESSORIES)

    def click_art(self):
        self.move_to_element_and_click(HomeLocators.BTN_ART)

    def click_hummingbird_printed_tshirt(self):
        self.move_to_element_and_click(HomeLocators.BTN_HUMMINGBIRD_PRINTED_TSHIRT)

    def click_today_is_a_good_day_framed(self):
        self.move_to_element_and_click(HomeLocators.BTN_TODAY_IS_A_GOOD_DAY_FRAMED)

    # FOOTER
    def click_prices_drop(self):
        self.move_to_element_and_click(HomeLocators.BTN_PRICES_DROP)
