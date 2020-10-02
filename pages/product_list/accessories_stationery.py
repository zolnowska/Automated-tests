from pages.base import Base
from locators.product_list import accessories_stationery


class AccessoriesStationery(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_mountain_fox_notebook(self):
        self.move_to_element_and_click(accessories_stationery.BTN_MOUNTAIN_FOX_NOTEBOOK)
