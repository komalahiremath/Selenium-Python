from fileinput import close

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
time.sleep(5)



#is_displayed()  and  is_enabled()-----conditional_commands
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status:",searchbox.is_displayed())
print("Enabled status:",searchbox.is_enabled())


#is_selected() ---for radio buttons and check boxes
male_rd=driver.find_element(By.XPATH,"//input[@id='gender-male']")
female_rd=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(male_rd.is_selected())
print(female_rd.is_selected())


#driver.close()      ##browser commands
driver.quit()