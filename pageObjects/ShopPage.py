from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.all_card_titles = (By.CSS_SELECTOR, ".card-title a")
        self.all_card_buttons = (By.CSS_SELECTOR, ".card-footer button")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCartTitles(self):
        return self.driver.find_elements(*self.all_card_titles)

    def getCartButtons(self):
        return self.driver.find_elements(*self.all_card_buttons)

    def clickCheckoutButton(self):
        return self.driver.find_element(*self.checkout_button)






