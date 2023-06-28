import logging

from BaseTest import BaseTest
from common import Common

from PageObjects.MainPage import MainPage

LOGGER = logging.getLogger(__name__)
MAIN_URL = MainPage.URL


class TestMainPage(BaseTest):

    def test_page_title(self):
        self.driver.get(MAIN_URL)
        assert self.driver.title == MainPage.EXPECTED_PAGE_TITLE, "Title is incorrect"

    def test_phone_number(self):
        commons = Common(self.driver)
        self.driver.get(MAIN_URL)

        phone_number = commons.get_element(MainPage.PHONE_NUMBER)
        assert phone_number.text == MainPage.EXPECTED_PHONE_NUMBER, "Phone number is incorrect"

    def test_email_address(self):
        commons = Common(self.driver)
        self.driver.get(MAIN_URL)

        LOGGER.info("Checking e-mail address")
        email = commons.get_element(MainPage.EMAIL_ADDRESS)
        assert email.text == MainPage.EXPECTED_EMAIL

    def test_facebook_link(self):
        commons = Common(self.driver)
        self.driver.get(MAIN_URL)

        facebook_link = commons.get_element(MainPage.FACEBOOK_LINK)
        assert facebook_link.get_attribute(
            "href") == MainPage.EXPECTED_FACEBOOK_LINK, "Facebook link is incorrect"