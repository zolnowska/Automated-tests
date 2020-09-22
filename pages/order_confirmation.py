from pages.base import Base
from locators import order_confirmation


class OrderConfirmation(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def get_information_1st_bought_item(self):
        return self.get_text(order_confirmation.TEXT_1ST_BOUGHT_ITEM)

    def get_item_cost_1st_item(self):
        return self.get_text(order_confirmation.TEXT_ITEM_COST_1ST_ITEM)

    def get_quantity_1st_item(self):
        return self.get_text(order_confirmation.TEXT_QUANTITY_1ST_ITEMS)

    def get_items_cost_1st_item(self):
        return self.get_text(order_confirmation.TEXT_ITEMS_COST_1ST_ITEMS)

    def get_subtotal_cost(self):
        return self.get_text(order_confirmation.TEXT_SUBTOTAL_COST)

    def get_shipping_cost(self):
        return self.get_text(order_confirmation.TEXT_SHIPPING_COST)

    def get_total_cost(self):
        return self.get_text(order_confirmation.TEXT_TOTAL_COST)