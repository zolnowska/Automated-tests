from selenium.webdriver.common.by import By
from lib.pages.base import Base


class ClothesWomenLocators:

    BTN_HUMMINGBIRD_PRINTED_SWEATER = (By.XPATH, '//div[@class="thumbnail-container reviews-loaded"]')


class ClothesWomen(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_hummingbird_printed_sweater(self):
        self.wait_until_element(ClothesWomenLocators.BTN_HUMMINGBIRD_PRINTED_SWEATER)
        self.move_to_element_and_click(ClothesWomenLocators.BTN_HUMMINGBIRD_PRINTED_SWEATER)