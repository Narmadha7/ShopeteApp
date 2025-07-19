from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckoutPage:

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.checkout = (By.XPATH, "//button[@class='btn btn-success']")

    # Action methods

    def checkOutItems(self):
        self.driver.find_element(*self.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

