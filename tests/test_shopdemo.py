import time

import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from BasePage.BasePage import BaseTest


# @pytest.mark.usefixtures("selenium_driver") # to remove this we are inheriting baseclass
class TestShop(BaseTest):
    def test_shop(self):
        homepage = HomePage(self.driver)
        shop_page = homepage.click_shop_button()

        all_titles = shop_page.getCartTitles()
        i = -1
        for title in all_titles:
            i += 1
            if title.text == "Blackberry":
                shop_page.getCartButtons()[i].click()

        shop_page.clickCheckoutButton().click()
        time.sleep(4)

        checkout = CheckoutPage(self.driver)
        confirm_page = checkout.checkOutItems()
        time.sleep(4)

        confirm_page.getCountryName().send_keys("ind")
        time.sleep(5)
        self.verifyLinkPresence("India")

        confirm_page.getName().click()
        confirm_page.clickCheckbox().click()
        confirm_page.getSubmit().click()

        text_match = confirm_page.getSuccess().text
        assert "Success!" in text_match
