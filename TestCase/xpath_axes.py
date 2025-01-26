from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
time.sleep(2)


#self node
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/self::a").text
print(text_msg)

#parent node
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/parent::td").text
print(text_msg)

#child
childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/ancestor::tr/child::td")
print(len(childs))          #6

#ancestor
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/ancestor::tr").text
print(text_msg)             #Tata Consultancy A 4,265.55 4,291.80 + 0.62 Buy  |  Sell


#descendant
descendant = driver.find_elements(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/ancestor::td/descendant::*")
print("Number of descendant nodes:",len(descendant))       #1

following = driver.find_elements(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/ancestor::td/following::*")
print("Number of following nodes:",len(following))          #354

#following-sibling
following_siblings = driver.find_elements(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/ancestor::td/following-sibling::*")
print("Number of following-siblings nodes:",len(following_siblings))         #5

#preceding
preceding = driver.find_elements(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/ancestor::td/preceding::*")
print("Number of preceding nodes:",len(preceding))              #310

#preceding_siblings
preceding_siblings = driver.find_elements(By.XPATH,"//a[contains(text(),'Tata Consultancy')]/ancestor::td/preceding-sibling::*")
print("Number of preceding_siblings nodes:",len(preceding_siblings))
driver.close()