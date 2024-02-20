from selene import browser


class BasePage:
    def open_page(self,url):
        browser(url)
        return self