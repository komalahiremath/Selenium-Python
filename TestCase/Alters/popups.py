#alter window is not a web element
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

alertwindow=driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Welcome")
alertwindow.accept()

time.sleep(2)

#cancel the alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

link2=driver.switch_to.alert
link2.dismiss()
time.sleep(2)

#accept the alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(2)

link2=driver.switch_to.alert
link2.accept()
time.sleep(2)