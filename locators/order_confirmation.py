from selenium.webdriver.common.by import By

TEXT_1ST_BOUGHT_ITEM = (By.XPATH, '//div[@class="col-sm-4 col-xs-9 details"]/span')
TEXT_ITEM_COST_1ST_ITEM = (By.XPATH, '//div[@class="col-xs-5 text-sm-right text-xs-left"]')
TEXT_QUANTITY_1ST_ITEMS = (By.XPATH, '//div[@class="col-xs-2"]')
TEXT_ITEMS_COST_1ST_ITEMS = (By.XPATH, '//div[@class="col-xs-5 text-xs-right bold"]')
TEXT_SUBTOTAL_COST = (By.XPATH, '//*[@id="order-items"]/div/table/tbody/tr[1]/td[2]')
TEXT_SHIPPING_COST = (By.XPATH, '//*[@id="order-items"]/div/table/tbody/tr[2]/td[2]')
TEXT_TOTAL_COST = (By.XPATH, '//*[@id="order-items"]/div/table/tbody/tr[3]/td[2]')
