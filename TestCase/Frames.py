from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(5)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()   #go back to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()   #go back to main page

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//*[@id='navbar-top-firstrow']/li[8]/a").click()
time.sleep(5)