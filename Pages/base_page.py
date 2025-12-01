from typing import Tuple

from selenium.common import TimeoutException, NoSuchElementException
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
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise ElementNotFound(f"Cannot find element: {locator}")

    def find_elements(self, locator: Locator) -> WebElement:
        try:
            elements = self.find_elements(locator)
            return elements
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
    #get locator add to cart btn
    @staticmethod
    def add_to_cart_btn(product_name)-> Locator|None:
        try:
            return (
                By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class = 'inventory_item']//button[text()='Add to cart']"
            )
        except NoSuchElementException:
            print("No 'Add to cart' button found!")
    #get locator remove btn
    @staticmethod
    def remove_from_cart_btn(product_name)-> Locator|None:
        try:
            return(
                    By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class = 'inventory_item']//button[text()='Remove']"
                )
        except NoSuchElementException:
            print("No 'Remove' button found!")

    def is_element_not_present(self, locator: Locator) -> bool:
        return len(self.driver.find_elements(*locator)) == 0

    def wait_for_element_not_present(self,locator: Locator):
        self.wait.until(EC.invisibility_of_element_located(locator))










