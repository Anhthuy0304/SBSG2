from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
path = "/Users/anhthuy/Documents/GitHub/chromedriver" 
driver = webdriver.Chrome(path)
driver.get("https://starbucks-uat-ecomm.ascentis.com.sg/productlist/category/MERCHANDISE?SortBy=publishdate&keyword=")
print(driver.title)
search = driver.find_element_by_class_name("SearchInput-input")
search.send_keys('dummy')
time.sleep(5)
search.send_keys(Keys.ENTER)

try:

    main = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "main")))
    products = driver.find_elements_by_class_name("product")
    for product in products:
     header = products.find_elements_by_class_name("listProduct-item col-6 col-md-4")
    print(header.text)

except TimeoutException:
    
    driver.quit()