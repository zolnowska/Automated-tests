from selenium.webdriver.common.by import By

RADIO_PRESTASHOP = (By.XPATH, '//*[@id="js-delivery"]/div/div[1]/div[1]/div/span')
RADIO_MY_CARRIER = (By.XPATH, '//*[@id="js-delivery"]/div/div[1]/div[4]/div/span')
BUTTON_CONTINUE = (By.XPATH, '//button[@name="confirmDeliveryOption"]')