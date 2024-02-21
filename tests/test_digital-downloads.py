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
from pages.digital_downloads_page import DigitalDownloadfPage


def test_digital_downloads_page():
    with step("Testing the digital-downloads page"):
        digital_downloads_page = DigitalDownloadfPage()
        digital_downloads_page.open_main_page()
        digital_downloads_page.go_digital_downloads_menu()
        digital_downloads_page.should_digital_downloads_page()