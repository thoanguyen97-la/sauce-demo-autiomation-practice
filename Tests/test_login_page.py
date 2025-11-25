from Pages.login_page import LoginPage
from TestData.login_testdata import LoginTestData as TD

def test_login_successful(driver):
    page = LoginPage(driver)
    page.open(page.URL)
    page.login(TD.VALID_USERNAME,TD.VALID_PASSWORD)
    assert "inventory" in driver.current_url

def test_login_with_invalid_username(driver):
    page = LoginPage(driver)
    page.open(page.URL)
    page.login(TD.INVALID_USERNAME,TD.VALID_PASSWORD)
    error_message = page.get_error_message()
    assert TD.ERROR_INVALID_CREDENTIALS in error_message

def test_login_with_invalid_password(driver):
    page = LoginPage(driver)
    page.open(page.URL)
    page.login(TD.VALID_USERNAME,TD.INVALID_PASSWORD)
    error_message = page.get_error_message()
    assert TD.ERROR_INVALID_CREDENTIALS in error_message
