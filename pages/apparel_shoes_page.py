from pages.base_page import BasePage
from selene import browser, have
from allure_commons._allure import step


class ApparelShoesPage(BasePage):
    def go_apparel_shoes_menu(self):
        with step("Go to the apparel shoes page"):
            browser.all('a[href="/apparel-shoes"]').first.click()
            return self

    def should_apparel_shoes_page(self):
        with step("Checking the opening of a apparel shoes page"):
            browser.element('.page-title>h1').should(have.text('Apparel & Shoes'))
            return self
