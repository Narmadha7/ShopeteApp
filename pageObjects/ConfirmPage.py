from selenium.webdriver.common.by import By


class ConfirmPage:
    # Constructor

    def __init__(self, driver):
        self.driver = driver
        self.country_textbox = (By.ID, "country")
        self.country_name = (By.LINK_TEXT, "India")
        self.checkbox_button = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_txt = (By.CSS_SELECTOR, "[class*='alert alert-success alert-dismissible']")

    # Action methods
    def getCountryName(self):
        return self.driver.find_element(*self.country_textbox)

    def getName(self):
        return self.driver.find_element(*self.country_name)

    def clickCheckbox(self):
        return self.driver.find_element(*self.checkbox_button)

    def getSubmit(self):
        return self.driver.find_element(*self.submit_button)

    def getSuccess(self):
        return self.driver.find_element(*self.success_txt)

