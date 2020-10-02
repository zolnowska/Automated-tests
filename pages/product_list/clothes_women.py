from pages.base import Base
from locators.product_list import clothes_women


class ClothesWomen(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_hummingbird_printed_sweater(self):
        self.move_to_element_and_click(clothes_women.BTN_HUMMINGBIRD_PRINTED_SWEATER)