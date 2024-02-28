import os
import requests
import json
import allure
import logging
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have


LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"
cookie = ''

def test_login_through_api(browser_setup):
    with step("Login with API"):
        result = requests.post(
            url=API_URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        assert result.status_code == 302
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)


    # global cookie
    # with step("Get cookie from API"):
    #     cookie = result.cookies.get("NOPCOMMERCE.AUTH")
    #
    # with step("Set cookie from API and open web url"):
    #     browser.open(WEB_URL)
    #     browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    #     browser.open(WEB_URL)
    #
    # with step("Verify successful authorization"):
    #     browser.element('.account').should(have.text(f'{LOGIN}'))
    #
