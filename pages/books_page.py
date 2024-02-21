from pages.base_page import BasePage
from selene import browser, have
from allure_commons._allure import step


class BookPage(BasePage):
    def go_books_menu(self):
        with step("Go to the books page"):
            browser.all('a[href="/books"]').first.click()
            return self

    def should_book_page(self):
        with step("Checking the opening of a book page"):
            browser.element('div.page-title>h1').should(have.text('Books'))
            return self