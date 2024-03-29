from pages.base_page import BasePage
from selene import browser, have
from allure_commons._allure import step


class ElectronicsPage(BasePage):
    def go_electronics_menu(self):
        with step("Go to the books page"):
            browser.all('a[href="/electronics"]').first.click()
            return self

    def should_electronics_page(self):
        with step("Checking the opening of a book page"):
            browser.element('.page-title>h1').should(have.text('Electronics'))
            return self