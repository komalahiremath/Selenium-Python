import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()


##explicit wait declaration
##skip the line, if got Exception
##wait for every 2sec interval of time for the element
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception])


driver.get("https://www.google.com/")
time.sleep(5)
driver.maximize_window()

searchbox=driver.find_element(By.NAME,"q")

searchbox.send_keys("Selenium")
searchbox.submit()

#wait for the specific element
##skip the line, if got Exception
searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()

driver.quit()