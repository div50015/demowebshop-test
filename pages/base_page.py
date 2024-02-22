from selene import browser
from allure_commons._allure import step


class BasePage:
    def open_main_page(self):
        WEB_URL = "https://demowebshop.tricentis.com/"
        API_URL = "https://demowebshop.tricentis.com/"
        with step("Opening the main page"):
            browser.open(WEB_URL)
            return self
