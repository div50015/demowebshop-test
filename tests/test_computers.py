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
from pages.computers_page import ComputersPage


def test_computers_page():
    with step('Testing the computers page'):
        page_computers = ComputersPage()
        page_computers.open_main_page()
        page_computers.go_computers_menu()
        page_computers.should_computers_page()