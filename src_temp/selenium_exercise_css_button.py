from selenium import webdriver
import time

path = "D:\\chromedriver.exe"
driver = webdriver.Chrome(path)

time.sleep(1)
URL = "https://python.org"
driver.get(URL)

time.sleep(3)
button_elements = driver.find_elements_by_css_selector("button")
for button_element in button_elements:
    button_string = button_element.text
    if button_string=="GO":
        button_element.click()




time.sleep(5)
driver.close()
