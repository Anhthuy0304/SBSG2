from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
path = "/Users/anhthuy/Documents/GitHub/chromedriver" 
driver = webdriver.Chrome(path)
driver.get("https://starbucks-uat-ecomm.ascentis.com.sg/product/christmassiren22")
print(driver.title)
link = driver.find_element_by_xpath("// input[@id='name']")
link.send_keys("Thuy")
link = driver.find_element_by_xpath("// input[@id='email']")
link.send_keys("thuymai1473@gmail.com")
link = driver.find_element_by_xpath("// textarea[@id='message']")
link.send_keys("Hello")
time.sleep(20)
driver.quit()