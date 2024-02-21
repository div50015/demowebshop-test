from allure_commons._allure import step
from pages.apparel_shoes_page import ApparelShoesPage


def test_page_apparel_shoes():
    with step('Testing the apparel shoes page'):
        apparel_shoes_page = ApparelShoesPage()
        apparel_shoes_page.open_main_page()
        apparel_shoes_page.go_apparel_shoes_menu()
        apparel_shoes_page.should_apparel_shoes_page()



