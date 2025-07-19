from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage


class HomePage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.shop_button = (By.CSS_SELECTOR, "a[href*=shop]")
        self.name_text = (By.NAME, "name")
        self.email_text = (By.NAME, "email")
        self.password_text = (By.ID, "exampleInputPassword1")
        self.check_me = (By.CSS_SELECTOR, "#exampleCheck1")
        self.gender_dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
        self.employment_status = (By.CSS_SELECTOR, "#inlineRadio2")
        self.dob_txt = (By.XPATH, "//input[@name='bday']")
        self.twoway_text = (By.XPATH, "(//input[@type='text'])[3]")
        self.submit_button = (By.XPATH, "//input[@type='submit']")
        self.success_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        self.footer_txt = (By.XPATH, "//footer/div[@class='container']")

    # Action methods
    def click_shop_button(self):
        self.driver.find_element(*self.shop_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page

    def setName(self, username):
        return self.driver.find_element(*self.name_text).send_keys(username)

    def setEmail(self, email):
        return self.driver.find_element(*self.email_text).send_keys(email)

    def setPassword(self, password):
        return self.driver.find_element(*self.password_text).send_keys(password)

    def setCheckMe(self):
        return self.driver.find_element(*self.check_me)

    def setGender(self):
        return self.driver.find_element(*self.gender_dropdown)

    def setStatus(self):
        return self.driver.find_element(*self.employment_status)

    def setDob(self):
        return self.driver.find_element(*self.dob_txt)

    def getTwoway(self):
        return self.driver.find_element(*self.twoway_text)

    def setSubmit(self):
        return self.driver.find_element(*self.submit_button)

    def get_success_msg(self):
        return self.driver.find_element(*self.success_msg)

    def get_footer_txt(self):
        return self.driver.find_element(*self.footer_txt)
