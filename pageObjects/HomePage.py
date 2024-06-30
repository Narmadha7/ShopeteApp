from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    # Locators
    shop = (By.CSS_SELECTOR, "a[href*=shop]")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check_me = (By.CSS_SELECTOR, "#exampleCheck1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    status = (By.CSS_SELECTOR, "#inlineRadio2")
    dob = (By.XPATH, "//input[@name='bday']")
    twoway = (By.XPATH, "(//input[@type='text'])[3]")
    submit = (By.XPATH, "//input[@type='submit']")
    success_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    footer_txt = (By.XPATH, "//footer/div[@class='container']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        cp = CheckoutPage(self.driver)
        return cp

    def setName(self):
        return self.driver.find_element(*HomePage.name)

    def setEmail(self):
        return self.driver.find_element(*HomePage.email)

    def setPassword(self):
        return self.driver.find_element(*HomePage.password)

    def setCheckMe(self):
        return self.driver.find_element(*HomePage.check_me)

    def setGender(self):
        return self.driver.find_element(*HomePage.gender)

    def setStatus(self):
        return self.driver.find_element(*HomePage.status)

    def setDob(self):
        return self.driver.find_element(*HomePage.dob)

    def getTwoway(self):
        return self.driver.find_element(*HomePage.twoway)

    def setSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessmsg(self):
        return self.driver.find_element(*HomePage.success_msg)

    def getFootertxt(self):
        return self.driver.find_element(*HomePage.footer_txt)
