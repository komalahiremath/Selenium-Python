import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://www.opencart.com/index.php?route=account/register")

drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry=Select(drpcountry_ele)

#select option for the dropdown
drpcountry.select_by_visible_text("India")
drpcountry.select_by_index(13)
drpcountry.select_by_value("10")

#capture all the options and print them
drpcountry_ele=drpcountry.options
print("total number of options:",len(drpcountry_ele))

for opt in drpcountry_ele:
    print(opt.text)


#select option from dropdown without using built-in method
for opt in drpcountry_ele:
    if opt.text=='India':
        opt.click()
        break