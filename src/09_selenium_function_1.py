from selenium import webdriver
import time

path = "D:\\chromedriver.exe"
driver = webdriver.Chrome(path)
time.sleep(1) # 로딩시간 대기

URL = "https://python.org"
driver.get(URL)

time.sleep(3)
input_element = driver.find_element_by_id('id-search-field')
input_element.clear()
input_element.send_keys('pandas')