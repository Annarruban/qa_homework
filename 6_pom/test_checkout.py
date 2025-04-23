import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from sauce_demo_page import SauceDemoPage

def setup_driver():
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   driver.maximize_window()
   return driver

@pytest.fixture
def page():
   driver = setup_driver()
   page = SauceDemoPage(driver)
   yield page


def test_checkout(page):
   page.start()
   page.login("standard_user", "secret_sauce")
   page.add_to_cart("sauce-labs-backpack")
   page.add_to_cart("sauce-labs-bolt-t-shirt")
   page.add_to_cart("sauce-labs-onesie")
   page.go_to_cart()
   page.checkout()
   page.fill_out_personal_info("Anna", "Ruban", "14169")
   total = page.total()
   page.close()
   assert total == "$58.29"