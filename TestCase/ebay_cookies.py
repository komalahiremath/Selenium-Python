from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://www.ebay.co.uk/")
time.sleep(10)

alertcookies=driver.switch_to.alert
alertcookies.accept()

driver.find_element(By.XPATH,"//input[@id='gh-ac']").send_keys("lipstrict")
time.sleep(2)