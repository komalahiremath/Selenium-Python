from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.ebay.co.uk/")
time.sleep(5)

##absulte xpath
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/header/table/tbody/tr/td[5]/form/table/tbody/tr/td[1]/div/div/input[1]").send_keys("T-shirts")

#time.sleep(5)

###Relative xpath
driver.find_element(By.XPATH,'.//*[@id="gh-ac"]').send_keys("Ladies watch")
driver.find_element(By.XPATH,'//*[@id="gh-btn"]').click()
#time.sleep(5)

#Or, And operator
driver.find_element(By.XPATH,"//input[@name='_nkw' or @id='gh-ac']").send_keys("Ladies watch")
driver.find_element(By.XPATH,"//input[@class='btn btn-prim gh-spr' and @id='gh-btn']").click()
#time.sleep(5)

#contains and starts-with function for dynamic attribute
driver.find_element(By.XPATH,"//input[contains(@id,'ac')]").send_keys("weather ladies pant")
driver.find_element(By.XPATH,"//input[starts-with(@value,'Se')]").click()
#time.sleep(5)

#text for inner text name link
driver.find_element(By.XPATH,"//a[text()='Saved']").click()
time.sleep(5)