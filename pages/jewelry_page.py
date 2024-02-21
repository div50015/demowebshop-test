from pages.base_page import BasePage
from selene import browser, have
from allure_commons._allure import step


class JewelryPage(BasePage):
    def go_jewelry_menu(self):
        with step("Go to the jewelry page"):
            browser.all('a[href="/jewelry"]').first.click()
            return self

    def should_jewelry_page(self):
        with step('Checking the opening of a jewelry page'):
            browser.element('.page-title>h1').should(have.text('Jewelry'))
            return self