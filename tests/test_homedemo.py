import json
import os.path
import time

import pytest

from BasePage.BasePage import BaseTest
from pageObjects.HomePage import HomePage

path = os.path.abspath(os.curdir) + "//testdata//testdata.json"
with open(path) as f:
    test_data = json.load(f)
    data_list = test_data["data"]


@pytest.mark.parametrize("data_item", data_list)
class TestHomePage(BaseTest):

    def test_homeDemo(self, data_item):
        self.maximize_windows()
        home_page = HomePage(self.driver)
        home_page.setName(data_item["Name"])

        home_page.setEmail(data_item["Email"])
        home_page.setPassword(data_item["Password"])

        home_page.setCheckMe().click()

        # static dropdowns
        self.selectOptionByText(home_page.setGender(), data_item["gender"])

        # Employment status
        home_page.setStatus().click()

        # date picker
        home_page.setDob().send_keys(data_item["dob"])

        twoway = home_page.getTwoway().get_attribute("value")
        print(twoway)
        assert twoway == "Micky Mak"

        home_page.setSubmit().click()
        time.sleep(2)
        message = home_page.get_success_msg().text
        print(message)
        assert "Success!" in message

        footer_txt = home_page.get_footer_txt().text
        print(footer_txt)
        assert "Copyright" in footer_txt
