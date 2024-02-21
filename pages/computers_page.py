from pages.base_page import BasePage
from selene import browser, have
from allure_commons._allure import step


class ComputersPage(BasePage):
    def go_computers_menu(self):
        with step("Go to the books page"):
            browser.all('a[href="/computers"]').first.click()
            return self

    def should_computers_page(self):
        with step("Checking the opening of a book page"):
            browser.element('.page-title>h1').should(have.text('Computers'))
            return self
