import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("selenium_driver")
class BaseTest:

    def maximize_windows(self):
        self.driver.maximize_window()

    @staticmethod
    def selectOptionByText(locator, text):
        gender = Select(locator)
        gender.select_by_visible_text(text)

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))
