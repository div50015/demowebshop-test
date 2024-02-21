import os
import time
import requests
import json
import allure
import logging
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
from dotenv import load_dotenv
from pages.electronics_page import ElectronicsPage

def test_electronics_page():
    with step('Testing electronics page'):
        electronics_page = ElectronicsPage()
        electronics_page.open_main_page()
        electronics_page.go_electronics_menu()
        electronics_page.should_electronics_page()