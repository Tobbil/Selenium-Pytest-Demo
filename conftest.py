import datetime
import logging
import os

import chromedriver_autoinstaller
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

LOGGER = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture(scope="session", autouse=True)
def main_fixture(request):
    headless = request.config.getoption("--headless")
    options = Options()
    if headless:
        options.add_argument("--headless")
    yield options
    date = datetime.date.today().strftime("%d%m%Y")
    current_time = datetime.datetime.now().strftime("%H%M%S")
    os.rename(
        "./logs/test.log", f"./logs/test_{date}_{current_time}.log")


@pytest.fixture(scope="class")
def driver_setup_fixture(main_fixture):
    chromedriver_autoinstaller.install()
    service_obj = Service("chromedriver")
    options = main_fixture
    driver = WebDriver(service=service_obj, options=options)
    yield driver
    driver.quit()
