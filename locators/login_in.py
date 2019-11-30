from selenium.webdriver.common.by import By

INPUT_EMAIL = (By.XPATH, '//input[@class="form-control"]')
INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')
BTN_SIGN_IN = (By.ID, 'submit-login')
BTN_CREATE_ACCOUNT = (By.XPATH, '//div[@class="no-account"]/a')
TEXT_AUTHENTICATION_FAILED = (By.XPATH, '//div[@class="help-block"]')
