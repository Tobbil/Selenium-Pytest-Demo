import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def _driver(self, driver_setup_fixture):
        self.driver = driver_setup_fixture
