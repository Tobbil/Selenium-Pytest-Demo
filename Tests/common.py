from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Common:
    """Common methods"""

    def __init__(self, driver):
        self.driver = driver

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
