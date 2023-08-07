import logging

from BaseTest import BaseTest

from PageObjects.MainPage import MainPage

LOGGER = logging.getLogger(__name__)
MAIN_URL = MainPage.URL


class TestMainPage(BaseTest):

    def test_page_title(self):
        self.driver.get(MAIN_URL)
        LOGGER.info("Checking page title")
        assert self.driver.title == MainPage.EXPECTED_PAGE_TITLE, "Title is incorrect"

    def test_phone_number(self):
        self.driver.get(MAIN_URL)

        phone_number = self.get_element(MainPage.PHONE_NUMBER)
        LOGGER.info("Checking phone number")
        assert phone_number.text == MainPage.EXPECTED_PHONE_NUMBER, "Phone number is incorrect"

    def test_email_address(self):
        self.driver.get(MAIN_URL)

        email = self.get_element(MainPage.EMAIL_ADDRESS)
        LOGGER.info("Checking e-mail address")
        assert email.text == MainPage.EXPECTED_EMAIL, "E-mail address is incorrect"

    def test_facebook_link(self):
        self.driver.get(MAIN_URL)

        facebook_link = self.get_element(MainPage.FACEBOOK_LINK)
        LOGGER.info("Checking Facebook link")
        assert facebook_link.get_attribute(
            "href") == MainPage.EXPECTED_FACEBOOK_LINK, "Facebook link is incorrect"
