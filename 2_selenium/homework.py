from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://itcareerhub.de/ru")
link = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
link.click()
sleep(5)
driver.save_screenshot('screenshot.png')