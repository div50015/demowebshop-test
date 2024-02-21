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
from pages.gift_cards_page import GiftCardsPage

def test_page_gift_cards():
    with step('Testing the gift cards page'):
        gift_cards_page = GiftCardsPage()
        gift_cards_page.open_main_page()
        gift_cards_page.go_gift_cards_menu()
        gift_cards_page.should_gift_cards_page()
