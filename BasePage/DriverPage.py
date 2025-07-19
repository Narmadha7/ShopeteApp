import pytest
from selenium import webdriver


class DriverPage:
    @staticmethod
    def set_driver_details():
        driver = None
        if pytest.browser == "chrome":
            driver = webdriver.Chrome()
        elif pytest.browser == "firefox":
            driver = webdriver.Firefox()

        driver.implicitly_wait(3)

        return driver
