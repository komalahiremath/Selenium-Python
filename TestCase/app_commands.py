from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

#verify the title
print(driver.title)
#verify the url
print(driver.current_url)


# Verify new page URL
actual_url = driver.current_url
assert actual_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"




