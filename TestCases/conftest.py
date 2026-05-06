import pytest
from selenium import webdriver



@pytest.fixture()
def setup():

    driver= webdriver.Chrome()
    print("Launching chrome browser.........")
    yield driver
    driver.quit()

