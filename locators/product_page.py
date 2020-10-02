from selenium.webdriver.common.by import By

TEXT_REGULAR_PRICE = (By.XPATH, '//span[@class="regular-price"]')
TEXT_CURRENT_PRICE = (By.XPATH, '//div[@class="current-price"]/span[@itemprop="price"]')
TEXT_DISCOUNT = (By.XPATH, '//span[@class="discount discount-percentage"]')
DROP_DOWN_SIZE = (By.ID, 'group_1')
DROP_DOWN_PAPER = (By.ID, 'group_4')
BTN_SELECTED_SIZE = (By.XPATH, '//*[@id="group_1"]/option[@selected="selected"]')
BTN_SELECTED_PAPER_SQUARRED = (By.XPATH, '//*[@id="group_4"]/option[@selected="selected" and @title="Squarred"]')
BTN_ADD_TO_CART = (By.XPATH, '//button[@class="btn btn-primary add-to-cart"]')
RADIO_COLOR_WHITE = (By.XPATH, '//*[@id="group_2"]/li[1]/label')
RADIO_COLOR_BLACK = (By.XPATH, '//*[@id="group_2"]/li[2]/label')
INPUT_QUANTITY = (By.ID, 'quantity_wanted')
TEXT_PRODUCT_AVAILABILITY = (By.ID, 'product-availability')
BTN_INCREASE_QUANTITY = (By.XPATH, '//button[@class="btn btn-touchspin js-touchspin bootstrap-touchspin-up"]')
BTN_DECREASE_QUANTITY = (By.XPATH, '//button[@class="btn btn-touchspin js-touchspin bootstrap-touchspin-down"]')

# Popup Add to Cart
BTN_PROCEED_TO_CHECKOUT = (By.XPATH, '//a[@class="btn btn-primary"]')
BTN_CONTINUE_SHOPPING = (By.XPATH, '//button[@class="btn btn-secondary"]')






