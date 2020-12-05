from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import glob
import shutil

path = "D:\\chromedriver.exe"

driver = webdriver.Chrome(path)
URL = "http://marketdata.krx.co.kr/mdi#document=13020101"
driver.get(URL)
time.sleep(3)

input_element = driver.find_element_by_css_selector("div.cal-area>input")
input_element.clear()
input_element.send_keys("20201125")
input_element.send_keys(Keys.ENTER)

time.sleep(3)
searchbutton = driver.find_element_by_css_selector("div.design-center>button")
searchbutton.click()

time.sleep(3)
buttons = driver.find_elements_by_css_selector("span.button-mdi-group>button")
for button in buttons:
    buttonName = button.text
    if buttonName == 'CSV':
        button.click()
        time.sleep(3)

downloadFolder = """C:\\Users\\ray/Downloads/*"""
list_of_files = glob.glob(downloadFolder)
latest_file = max(list_of_files, key=os.path.getctime)

savedir = "D:\\pystock\\data\\"
toPath = os.path.join(savedir, "20201125.csv")
csv_name = os.path.join(toPath)
shutil.move(latest_file, toPath)