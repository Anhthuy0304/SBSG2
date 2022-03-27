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
driver.get("https://starbucks-uat-ecomm.ascentis.com.sg/productlist/category/MERCHANDISE?SortBy=publishdate&keyword=")
print(driver.title)
driver.maximize_window()
link = driver.find_element_by_link_text("Singapore Collection")
link.click()
time.sleep(2)
link = driver.find_element_by_link_text("Tumblers")
link.click()
element = driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "// img[@alt='DUMMY SKU TEST 11']")))).click()

element = driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "// span[@class='FormReceiver__addToCart FormReceiver__button buttonAddToCart up Button Button__frap Button__primary Button__bold Button__shadow']")))).click()
driver.quit()
