from selenium.webdriver.common.by import By
from lib.pages.base import Base


class OrderConfirmationLocators:

    TEXT_1ST_BOUGHT_ITEM = (By.XPATH, '//div[@class="col-sm-4 col-xs-9 details"]/span')
    TEXT_ITEM_COST_1ST_ITEM = (By.XPATH, '//div[@class="col-xs-4 text-sm-center text-xs-left"]')
    TEXT_QUANTITY_1ST_ITEMS = (By.XPATH, '//div[@class="col-xs-4 text-sm-center"]')
    TEXT_ITEMS_COST_1ST_ITEMS = (By.XPATH, '//div[@class="col-xs-4 text-sm-center text-xs-right bold"]')
    TEXT_SUBTOTAL_COST = (By.XPATH, '//*[@id="order-items"]/div/table/tbody/tr[1]/td[2]')
    TEXT_SHIPPING_COST = (By.XPATH, '//*[@id="order-items"]/div/table/tbody/tr[2]/td[2]')
    TEXT_TOTAL_COST = (By.XPATH, '//*[@id="order-items"]/div/table/tbody/tr[3]/td[2]')


class OrderConfirmation(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def get_information_1st_bought_item(self):
        return self.get_text(OrderConfirmationLocators.TEXT_1ST_BOUGHT_ITEM)

    def get_item_cost_1st_item(self):
        return self.get_text(OrderConfirmationLocators.TEXT_ITEM_COST_1ST_ITEM)

    def get_quantity_1st_item(self):
        return self.get_text(OrderConfirmationLocators.TEXT_QUANTITY_1ST_ITEMS)

    def get_items_cost_1st_item(self):
        return self.get_text(OrderConfirmationLocators.TEXT_ITEMS_COST_1ST_ITEMS)

    def get_subtotal_cost(self):
        return self.get_text(OrderConfirmationLocators.TEXT_SUBTOTAL_COST)

    def get_shipping_cost(self):
        return self.get_text(OrderConfirmationLocators.TEXT_SHIPPING_COST)

    def get_total_cost(self):
        return self.get_text(OrderConfirmationLocators.TEXT_TOTAL_COST)
