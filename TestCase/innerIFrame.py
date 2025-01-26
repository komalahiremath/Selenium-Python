from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(5)


driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()


outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")

driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Komala")
time.sleep(5)
#driver.switch_to.parent_frame()  # directly switch to patent frame