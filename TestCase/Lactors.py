from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
#driver.get("https://automationpratice.com/index.php")
time.sleep(2)

# id & name locators
driver.find_element(By.ID ,"small-searchterms").send_keys("Iphone pad")
driver.find_element(By.NAME ,"q").send_keys("Iphone pad")
time.sleep(2)

#linktext & partial linktext
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
time.sleep(2)

#classname and tagname
sliders=driver.find_elements(By.CLASS_NAME,"nivo-slice")
print(f"Number of the sliders on home-page:", len(sliders))
links=driver.find_elements(By.TAG_NAME,"a")
print(f"Number of the links on home-page:",len(links))


## CSS Selector
#tag and id
#driver.find_element(By.CSS_SELECTOR,"input#small-searchterms").send_keys("Iphone pad")
#tag and class
driver.find_element(By.CSS_SELECTOR,"input.search-box-text").send_keys("Iphone pad")
#driver.find_element(By.CSS_SELECTOR,"input.inputtext _55r1 _6luy").send_keys("komalashiremath6@gmail.com")##space in value called is not allowed
time.sleep(2)
#tag and attribute
driver.find_element(By.CSS_SELECTOR,"input[autocomplete=off]").send_keys("iphone pad")
time.sleep(2)
#tag class and attribute
#####to access the second element which has same name attribute
#####eg. in facebook page

##xpath

