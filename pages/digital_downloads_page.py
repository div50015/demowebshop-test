from pages.base_page import BasePage
from selene import browser, have
from allure_commons._allure import step


class DigitalDownloadfPage(BasePage):
    def go_digital_downloads_menu(self):
        with step("Go to the digitel-downloads page"):
            browser.all('a[href="/digital-downloads"]').first.click()
            return self

    def should_digital_downloads_page(self):
        with step("Checking the opening of a digital -downloads page"):
            browser.element('.page-title>h1').should(have.text('Digital downloads'))
            return self