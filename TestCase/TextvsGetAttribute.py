from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
time.sleep(2)

emailbox = driver.find_element(By.XPATH,"(//input[@id='Email'])[1]")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")

#text for inner text of element in html
print("result of text: ",emailbox.text)     #result of text:
#get_attribute for text
print("result of get_attribute():",emailbox.get_attribute('value'))         #result of get_attribute(): abc@gmail.com

