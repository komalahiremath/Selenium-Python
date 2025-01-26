import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://itera-qa.azurewebsites.net/home/automation")


#select specific checkbox
driver.find_element(By.XPATH,"//input[@id='monday']").click()


#select all the checkbox
checkboxes=driver.find_element(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))   #7


#Approach1
for i in range(len(checkboxes)):
    checkboxes[i].click()


#Approach2
for checkbox in checkboxes:
    checkbox.click()

#select multiple checkboxes by choice
for checkbox in checkboxes:
    weekname=checkbox.get_attribute('id')
    if weekname=='monday' or weekname=='sunday' or weekname=='saturday':
        checkbox.click()


#select last 2 checkboxes
#totalnumberofelements-2=starting index
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()


#select first 3 checkboxes
for i in range(len(checkboxes)):
    if i<3:
        checkboxes[i].click()


#non-select all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()