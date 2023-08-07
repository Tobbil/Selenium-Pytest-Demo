import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    @pytest.fixture(autouse=True)
    def _driver_setup(self, driver_setup_fixture):
        self.driver = driver_setup_fixture

    def _handle_exceptions(self, element):
        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(element))

        return el

    def get_element(self, element):
        el = self._handle_exceptions(element)

        return el

    def click_element(self, element):
        el = self._handle_exceptions(element)
        self.driver.click(el)
