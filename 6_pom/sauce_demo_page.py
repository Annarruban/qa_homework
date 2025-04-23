from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoPage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, self.TIMEOUT)

    def start(self):
        self.driver.get("https://www.saucedemo.com/")

    def close(self):
        self.driver.quit()

    def _wait_until_found(self, id):
        return self.wait.until(EC.presence_of_element_located(
            (By.ID, id))
        )

    def _wait_until_clickable(self, id):
        return self.wait.until(EC.element_to_be_clickable((By.ID, id)))

    def _enter_value_to_input(self, input_id, value):
        input =  self._wait_until_clickable(input_id)
        input.clear()
        input.send_keys(value)

    def login(self, username, password):
        self._enter_value_to_input("user-name", username)
        self._enter_value_to_input("password", password)
        login_button = self._wait_until_clickable("login-button")
        login_button.click()

    def add_to_cart(self, item):
        button_name = f"add-to-cart-{item}"
        button = self._wait_until_clickable(button_name)
        button.click()

    def go_to_cart(self):
        link = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
        link.click()

    def checkout(self):
        button = self._wait_until_clickable("checkout")
        button.click()

    def fill_out_personal_info(self, first_name, last_name, post_index):
        self._enter_value_to_input("first-name", first_name)
        self._enter_value_to_input("last-name", last_name)
        self._enter_value_to_input("postal-code", post_index)
        button = self._wait_until_clickable("continue")
        button.click()

    def total(self):
        text = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return text.text.lstrip("Total: ")