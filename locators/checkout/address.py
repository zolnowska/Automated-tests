from selenium.webdriver.common.by import By

INPUT_COMPANY = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[3]/div[1]')
INPUT_VAT = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[4]/div[1]')
INPUT_ADDRESS = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[5]/div[1]')
INPUT_ADDRESS_COMPLEMENT = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[6]/div[1]')
INPUT_CITY = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[7]/div[1]')
INPUT_POSTAL_CODE = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[8]/div[1]')
DROP_DOWN_COUNTRY = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[9]/div[1]/select')
INPUT_PHONE = (By.XPATH, '//*[@id="delivery-address"]/div/section/div[10]/div[1]')
CHECKBOX_SAME_ADDRESS = (By.ID, 'use_same_address')
BTN_CONTINUE = (By.XPATH, '//button[@name="confirm-addresses"]')
