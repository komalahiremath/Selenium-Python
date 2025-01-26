from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
time.sleep(2)
driver.get("https://www.snapdeal.com/")
time.sleep(2)
driver.back()           #nopcomerce
time.sleep(2)
driver.forward()           #snapdeal
time.sleep(2)
