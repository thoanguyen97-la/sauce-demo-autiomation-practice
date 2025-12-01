from Pages.login_page import LoginPage

def login_as_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.open(login_page.URL)
    login_page.login("standard_user", "secret_sauce")

