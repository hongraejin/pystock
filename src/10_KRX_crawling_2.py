from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import glob
import shutil

# chromedriver 경로 설정
path = "D:\\chromedriver.exe"

# 브라우저 실행 후 전체종목 검색창으로 이동
driver = webdriver.Chrome(path)
URL = "http://marketdata.krx.co.kr/mdi#document=13020101"
driver.get(URL)

time.sleep(3)
input_element = driver.find_element_by_css_selector("div.cal-area>input.schdate")
input_element.clear()
input_element.send_keys("20201125")
input_element.send_keys(Keys.ENTER)
