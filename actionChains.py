from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
import time

path = "/Users/anhthuy/Documents/GitHub/chromedriver" 
driver = webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]
actions = ActionChains(driver)
ActionChains(driver).double_click(cookie).perform()
for i in [5000]:   
    actions.perform()
