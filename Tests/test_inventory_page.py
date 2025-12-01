from Pages.inventory_page import InventoryPage
from TestData.inventory_testdata import InventoryTestData as IT
from Helpers.login_helper import login_as_standard_user

def test_add_to_cart(driver):
    page = InventoryPage(driver)
    login_as_standard_user(driver)
    page.add_to_cart(IT.ProductName)
    total_items_in_cart = page.get_shopping_cart_badge_value()
    assert "1" == total_items_in_cart

def test_remove_from_cart(driver):
    page = InventoryPage(driver)
    login_as_standard_user(driver)
    page.add_to_cart(IT.ProductName)
    page.remove_item_from_cart(IT.ProductName)
    #page.wait_for_element_not_present(page.ShoppingCartBadge)
    assert  page.is_element_not_present(page.ShoppingCartBadge)


