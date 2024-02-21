from pages.base_page import BasePage
from selene import browser, have
from allure_commons._allure import step


class GiftCardsPage(BasePage):
    def go_gift_cards_menu(self):
        with step("Go to the books page"):
            browser.all('a[href="/gift-cards"]').first.click()
            return self

    def should_gift_cards_page(self):
        with step("Checking the opening of a book page"):
            browser.element('.page-title>h1').should(have.text('Gift Cards'))
            return self