from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckoutPage:
    # Locators
    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods

    def getCartTitles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def getCartFooter(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        con = ConfirmPage(self.driver)
        return con

