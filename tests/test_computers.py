from allure_commons._allure import step
from pages.computers_page import ComputersPage


# def test_computers_page():
#     with step('Testing the computers page'):
#         page_computers = ComputersPage()
#         page_computers.open_main_page()
#         page_computers.go_computers_menu()
#         page_computers.should_computers_page()

class TestRun:
    def test_run(self):
        with step('Testing the computers page'):
            ComputersPage.open_main_page(self)
            ComputersPage.go_computers_menu(self)
            ComputersPage.should_computers_page(self)



