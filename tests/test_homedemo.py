import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHome(BaseClass):
    def test_homeDemo(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        log.info("first name is " + getData["Name"])
        hp.setName().send_keys(getData["Name"])

        hp.setEmail().send_keys(getData["Email"])
        hp.setPassword().send_keys(getData["Password"])

        hp.setCheckMe().click()

        # static dropdowns
        self.selectOptionByText(hp.setGender(), getData["gender"])

        # Employment status
        hp.setStatus().click()

        # date picker
        hp.setDob().send_keys(getData["dob"])

        twoway = hp.getTwoway().get_attribute("value")
        print(twoway)
        assert twoway == "Micky Mak"

        hp.setSubmit().click()
        time.sleep(2)
        message = hp.getSuccessmsg().text
        print(message)
        assert "Success!" in message

        footer_txt = hp.getFootertxt().text
        print(footer_txt)
        assert "Copyright" in footer_txt

    @pytest.fixture(params= HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
