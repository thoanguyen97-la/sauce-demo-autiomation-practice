from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from TestData.inventory_testdata import InventoryTestData as ID


class InventoryPage(BasePage):
    #locators
    ShoppingCartBadge = (By.CSS_SELECTOR,"[data-test= 'shopping-cart-badge']")

    def add_to_cart(self, product_name):
        self.click(self.add_to_cart_btn(product_name))

    def remove_item_from_cart(self, product_name):
        self.click(self.remove_from_cart_btn(product_name))

        # get total of items in cart
    def get_shopping_cart_badge_value(self) -> str | None:
        try:
            value = self.find_element((By.CSS_SELECTOR, "[data-test= 'shopping-cart-badge']")).text
            return value
        except NoSuchElementException:
            print("No value found")



















