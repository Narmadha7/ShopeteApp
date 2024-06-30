import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") - to remove this we are inheriting baseclass
class TestShop(BaseClass):
    def test_shop(self, setup):
        log = self.getLogger()
        hp = HomePage(self.driver)
        cp = hp.shopItems()
        log.info("getting all the card titles")
        cards = cp.getCartTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                cp.getCartFooter()[i].click()

        cp.getCheckoutButton().click()

        con = cp.checkOutItems()
        log.info("Entering country name as ind")
        con.getCountryName().send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        con.getName().click()
        con.getConfirm().click()
        con.getSubmit().click()

        textMatch = con.getSuccess().text
        log.info("Text received from application is "+textMatch)
        assert "Sducdfsces!" in textMatch
