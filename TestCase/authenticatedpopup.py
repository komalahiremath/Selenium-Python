from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)
#driver.get("https://the-internet.herokuapp.com/basic_auth")
#to bypass the authenticatedpopup
#syntax---https://username:password@url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)