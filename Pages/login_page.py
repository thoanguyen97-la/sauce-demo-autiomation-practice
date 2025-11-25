from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    #Locator
    UserName = (By.ID, "user-name")
    PassWord = (By.ID, "password")
    LoginBtn = (By.ID, "login-button")
    ErrorContainer = (By.XPATH, "//div[@class='error-message-container error']")
    ERROR_INVALID_CREDENTIALS = "Username and password do not match any user in this service"

    def login(self, username: str, password: str):
        self.type(self.UserName,username)
        self.type(self.PassWord,password)
        self.click(self.LoginBtn)

    def get_error_message(self):
        try:
            error_message =  self.find_element(self.ErrorContainer).text
            return error_message
        except NoSuchElementException:
            print("No error message found!")



