from selenium import webdriver
import time

path = "D:\\chromedriver.exe"
driver = webdriver.Chrome(path)

time.sleep(1)
URL = "https://python.org"
driver.get(URL)

time.sleep(3)
input_element = driver.find_element_by_id('id-search-field')
input_element.send_keys('pandas')

time.sleep(1)
button_element = driver.find_element_by_id('submit')
button_element.click()


time.sleep(5)
driver.close()
