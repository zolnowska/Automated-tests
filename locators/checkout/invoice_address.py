from selenium.webdriver.common.by import By

INPUT_COMPANY = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[3]/div[1]/input')
INPUT_VAT = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[4]/div[1]/input')
INPUT_ADDRESS = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[5]/div[1]/input')
INPUT_ADDRESS_COMPLEMENT = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[6]/div[1]/input')
INPUT_CITY = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[7]/div[1]/input')
INPUT_POSTAL_CODE = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[8]/div[1]')
DROP_DOWN_COUNTRY = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[9]/div[1]/select')
INPUT_PHONE = (By.XPATH, '//*[@id="invoice-address"]/div/section/div[10]/div[1]')
BTN_CANCEL = (By.XPATH, '//*[@id="invoice-address"]/div/footer/a')
BTN_CONTINUE = (By.XPATH, '//*[@id="invoice-address"]/div/footer/button')
