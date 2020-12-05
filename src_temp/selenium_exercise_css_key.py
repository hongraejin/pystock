from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "D:\\chromedriver.exe"
driver = webdriver.Chrome(path)

time.sleep(1)
URL = "https://python.org"
driver.get(URL)

time.sleep(3)
input_element = driver.find_element_by_css_selector("input.search-field")
input_element.send_keys("pandas")
input_element.send_keys(Keys.ENTER)

time.sleep(5)
driver.close()
