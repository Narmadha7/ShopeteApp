from selenium.webdriver.common.by import By


class ConfirmPage:
    # Locators
    country_name = (By.ID, "country")
    name = (By.LINK_TEXT, "India")
    confirm_button = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_button = (By.CSS_SELECTOR, "[type='submit']")
    success_txt = (By.CSS_SELECTOR, "[class*='alert alert-success alert-dismissible']")

    # Constructor

    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.country_name)

    def getName(self):
        return self.driver.find_element(*ConfirmPage.name)

    def getConfirm(self):
        return self.driver.find_element(*ConfirmPage.confirm_button)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit_button)

    def getSuccess(self):
        return self.driver.find_element(*ConfirmPage.success_txt)

