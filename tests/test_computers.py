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

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"
cookie = ''

def test_page_computers():
    with step("Set cookie from API and open web url"):
        browser.open(WEB_URL)
        browser.all('a[href="/computers"]').first.click()
        # browser.all('//div[@class="header-menu"]/ul/li/a[@href="/books"]').first.click()
#        time.sleep(5)
