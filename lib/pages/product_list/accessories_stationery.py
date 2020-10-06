from selenium.webdriver.common.by import By
from lib.pages.base import Base


class AccessoriesStationeryLocators:

    BTN_MOUNTAIN_FOX_NOTEBOOK = (By.XPATH, '//*[@id="js-product-list"]/div[1]/article[1]/div/a')


class AccessoriesStationery(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_mountain_fox_notebook(self):
        self.move_to_element_and_click(AccessoriesStationeryLocators.BTN_MOUNTAIN_FOX_NOTEBOOK)
