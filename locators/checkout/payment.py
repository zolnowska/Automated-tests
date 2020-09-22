from selenium.webdriver.common.by import By

RADIO_PAY_BY_CHECK = (By.XPATH, '//*[@id="payment-option-1-container"]/span')
RADIO_PAY_BY_BANK_WIRE = (By.XPATH, '//*[@id="payment-option-2-container"]/span')
CHEKBOX_TERMS = (By.XPATH, '//*[@id="conditions-to-approve"]/ul/li/div[1]/span')
BTN_ORDER = (By.XPATH, '//button[@class="btn btn-primary center-block"]')