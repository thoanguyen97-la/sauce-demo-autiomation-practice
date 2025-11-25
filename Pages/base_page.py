from typing import Tuple

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

Locator = Tuple[str, str]
class ElementNotFound(Exception):
    pass

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self,url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def find_element(self, locator: Locator) -> WebElement:
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise ElementNotFound(f"Cannot find element: {locator}")

    def click(self, locator : Locator) -> WebElement:
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            return element
        except TimeoutException:
            raise ElementNotFound(f"Cannot find element: {locator}")

    def type(self, locator: Locator, text)-> WebElement:
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
            return element
        except TimeoutException:
            raise ElementNotFound(f"Cannot find element: {locator}")

