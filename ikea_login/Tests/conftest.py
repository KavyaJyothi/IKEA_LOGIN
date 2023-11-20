import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
@pytest.yield_fixture(scope="class")
def oneTimeSetup():

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get("https://www.ikea.com/in/en/?iss=https%3A%2F%2Fin.accounts.ikea.com%2F")
            driver.implicitly_wait(6)
