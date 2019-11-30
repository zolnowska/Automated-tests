import unittest
import time
import string
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from configuration import *


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    def load_url(self, url):
        self.driver.get(url)

    def reload_page(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    ###########

    def check_if_exists(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    ##############

    def find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def find_elements(self, locator):
        return self.driver.find_elements(locator[0], locator[1])

    def wait_until_element(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_text(self, locator):
        return self.find_element(locator).text

    ################

    def wait_until_clickable_element(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_is_not_clickable(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def click_if_exists(self, locator):
        if self.check_if_exists(locator):
            self.click_element(locator)

    def wait_and_click(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        self.wait_until_clickable_element(locator, timeout)
        self.click_element(locator)

    #############

    def action_chain(self):
        return ActionChains(self.driver)

    def click(self, locator):
        element = self.find_element(locator)
        action = self.action_chain()
        action.click(element)
        action.perform()

    def send_keys(self, keys):
        action = self.action_chain()
        action.send_keys(keys)
        action.perform()

    def move_to_element(self, locator):
        element = self.find_element(locator)
        action = self.action_chain()
        action.move_to_element(element)
        action.perform()

    def move_to_element_and_click(self, locator):
        element = self.find_element(locator)
        self.move_to_element(element).click(element).perform()

    def input(self, locator, keys):
        element = self.find_element(locator)
        action = self.action_chain()
        action.click(element)
        action.send_keys(keys)
        action.perform()
