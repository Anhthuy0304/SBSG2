from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = "/Users/anhthuy/Documents/GitHub/chromedriver" 
driver = webdriver.Chrome(path)
driver.get("https://starbucks-uat-ecomm.ascentis.com.sg/")
print(driver.title)
