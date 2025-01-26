# we need to install requests package to python intrepreter
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fcomputers")


links=driver.find_elements(By.TAG_NAME,'a')
count=0
count2=0


##testing the broken link
for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is valid link")
        count2 += 1

print("Total number of broken links:",count)
print("Total number of broken links:",count2)