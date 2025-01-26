from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")

#click on link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()
time.sleep(5)


#find number of links in page
links=driver.find_elements(By.TAG_NAME,'a')
#links=driver.find_elements(By.TAG_NAME,'//a')
print("total number of links:",len(links))

#print all the links name
for link in links:
    print(link.text)


