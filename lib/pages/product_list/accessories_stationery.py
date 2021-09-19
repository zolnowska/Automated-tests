from selenium.webdriver.common.by import By
from lib.pages.base import Base


class AccessoriesStationeryLocators:

    BTN_MOUNTAIN_FOX_NOTEBOOK = (By.XPATH,
                                 '//img[@src="http://127.0.0.1/prestashop/18-home_default/mountain-fox-notebook.jpg"]')


class AccessoriesStationery(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_mountain_fox_notebook(self):
        self.move_to_element_and_click(AccessoriesStationeryLocators.BTN_MOUNTAIN_FOX_NOTEBOOK)
