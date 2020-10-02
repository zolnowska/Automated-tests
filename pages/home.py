from pages.base import Base
from locators import home_page


class Home(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_clothes(self):
        self.move_to_element_and_click(home_page.BTN_CLOTHES)

    def click_clothes_men(self):
        self.move_to_element(home_page.BTN_CLOTHES)
        self.wait_and_click(home_page.BTN_CLOTHES_MEN)

    def click_clothes_women(self):
        self.move_to_element(home_page.BTN_CLOTHES)
        self.wait_and_click(home_page.BTN_CLOTHES_WOMEN)

    def click_accessories(self):
        self.move_to_element_and_click(home_page.BTN_ACCESSORIES)

    def click_stationery(self):
        self.move_to_element(home_page.BTN_ACCESSORIES)
        self.wait_and_click(home_page.BTN_STATIONERY)

    def click_home_accessories(self):
        self.move_to_element(home_page.BTN_ACCESSORIES)
        self.wait_and_click(home_page.BTN_HOME_ACCESSORIES)

    def click_art(self):
        self.move_to_element_and_click(home_page.BTN_ART)

    def click_hummingbird_printed_tshirt(self):
        self.move_to_element_and_click(home_page.BTN_HUMMINGBIRD_PRINTED_TSHIRT)

    def click_today_is_a_good_day_framed(self):
        self.move_to_element_and_click(home_page.BTN_TODAY_IS_A_GOOD_DAY_FRAMED)

    # FOOTER
    def click_prices_drop(self):
        self.move_to_element_and_click(home_page.BTN_PRICES_DROP)
