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
from pages.jewelry_page import JewelryPage

def test_jewerly_page():
    with step('Testing the jewelry page'):
        jewelry_page = JewelryPage()
        jewelry_page.open_main_page()
        jewelry_page.go_jewelry_menu()
        jewelry_page.should_jewelry_page()
