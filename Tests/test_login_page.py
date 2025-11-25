from Pages.login_page import LoginPage

def test_login_successful(driver):
    page = LoginPage(driver)
    page.open(page.URL)
    page.login("standard_user","secret_sauce")
    assert "inventory" in driver.current_url

def test_login_with_invalid_username(driver):
    page = LoginPage(driver)
    page.open(page.URL)
    page.login("invalidusername","secret_sauce")
    error_message = page.get_error_message()
    assert page.ERROR_INVALID_CREDENTIALS in error_message

def test_login_with_invalid_password(driver):
    page = LoginPage(driver)
    page.open(page.URL)
    page.login("standard_user","abc")
    error_message = page.get_error_message()
    assert page.ERROR_INVALID_CREDENTIALS in error_message
