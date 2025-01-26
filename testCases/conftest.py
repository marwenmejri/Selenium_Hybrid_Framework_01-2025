import pytest
from selenium.webdriver import Chrome


# @pytest.fixture()
# def setup():
#     driver = Chrome()
#     driver.implicitly_wait(time_to_wait=5)
#     driver.maximize_window()
#     return driver


@pytest.fixture(scope='class')
def setup():
    driver = Chrome()
    driver.implicitly_wait(time_to_wait=5)
    driver.maximize_window()
    yield driver
    driver.quit()
