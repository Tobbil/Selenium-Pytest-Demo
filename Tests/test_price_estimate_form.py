import logging

from BaseTest import BaseTest

from PageObjects.EstimatePage import EstimatePage

LOGGER = logging.getLogger(__name__)
PAGE_URL = EstimatePage.URL


class TestEstimatePage(BaseTest):

    def test_page_title(self):
        self.driver.get(PAGE_URL)
        assert self.driver.title == EstimatePage.EXPECTED_PAGE_TITLE
