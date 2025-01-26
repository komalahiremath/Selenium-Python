from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)

driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)


driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
links=driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-results']/div/a").text

print(links)
#for link in links:
   #link.click()

time.sleep(2)