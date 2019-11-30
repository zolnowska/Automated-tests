from selenium.webdriver.common.by import By

#RADIO_GENDER_MR = (By.XPATH, '//input[@name="id_gender" and @value="1"]')
RADIO_GENDER_MR = (By.XPATH, '//label[1]/span[@class="custom-radio"]')
RADIO_GENDER_MRS = (By.XPATH, '//label[2]/span[@class="custom-radio"]')
INPUT_FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
INPUT_LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
INPUT_BIRTHDATE = (By.XPATH, '//input[@name="birthday"]')
BTN_SAVE = (By.XPATH, '//*[@id="customer-form"]/footer/button')
TEXT_EMAIL_ALREADY_USED = (By.XPATH, '//li[@class="alert alert-danger"]')
