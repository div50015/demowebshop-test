from selene import browser
import os
from allure_commons._allure import step


class BasePage:
    WEB_URL = "https://demowebshop.tricentis.com/"
    API_URL = "https://demowebshop.tricentis.com/"

    def open_main_page(self):
        with step("Opening the main page"):
            browser.open(self.WEB_URL)
            return self
