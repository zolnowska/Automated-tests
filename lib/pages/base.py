from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from configuration import *


def handler_move_target_out_of_bound_exception(func):
    def inner(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except MoveTargetOutOfBoundsException:
            element = self.find_element(*args, **kwargs)
            self.wait_until_element(*args, **kwargs)
            self.scroll_until_element_is_in_the_middle_of_page(*args, **kwargs)
            action = self.action_chain()
            action.move_to_element(element)
            action.perform()
    return inner


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

    def wait_until_clickable_element(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_is_not_clickable(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        WebDriverWait(self.driver, timeout).until_not(EC.element_to_be_clickable(locator))

    def wait_until_is_visibility(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_invisibility_element(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    ################

    def get_text(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        self.wait_until_element(locator, timeout)
        return self.find_element(locator).text

    def get_text_visibly(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        self.wait_until_is_visibility(locator, timeout)
        return self.find_element(locator).text

    def click_element(self, locator):
        self.find_element(locator).click()

    def click_if_exists(self, locator):
        if self.check_if_exists(locator):
            self.click_element(locator)

    def wait_and_click(self, locator, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        self.wait_until_clickable_element(locator, timeout)
        self.click_element(locator)

    def implicitly_wait(self, timeout=DEFAULT_SELENIUM_WAIT_SECONDS):
        self.driver.implicitly_wait(timeout)

    #############

    def scroll_until_element_is_in_the_middle_of_page(self, locator):
        element = self.find_element(locator)
        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (self.driver.execute_script('return window.innerHeight') / 2) + self.driver.execute_script(
            'return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

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

    @handler_move_target_out_of_bound_exception
    def move_to_element(self, locator):
        element = self.find_element(locator)
        self.wait_until_element(locator)
        action = self.action_chain()
        action.move_to_element(element)
        action.perform()

    def move_to_element_and_click(self, locator):
        self.wait_until_clickable_element(locator)
        self.move_to_element(locator)
        self.wait_and_click(locator)

    def input(self, locator, keys):
        element = self.find_element(locator)
        self.move_to_element(locator)
        self.wait_until_clickable_element(locator)
        action = self.action_chain()
        action.click(element)
        action.send_keys(keys)
        action.perform()

    ##############

    def select_element_from_drop_down(self, locator, element, element_type):
        self.move_to_element(locator)
        select = Select(self.find_element(locator))
        if element_type == 'id':
            select.select_by_id(element)
        elif element_type == 'text':
            select.select_by_visible_text(element)
        elif element_type == 'value':
            select.select_by_value(element)
