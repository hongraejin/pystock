from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import glob
import shutil
import pandas as pd

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

time.sleep(3)
search_button = driver.find_element_by_css_selector("div.design-center>button")
search_button.click()

time.sleep(3)
buttons = driver.find_elements_by_css_selector("span.button-mdi-group>button")
for button in buttons:
    button_name = button.text
    if button_name == "CSV":
        button.click()
        time.sleep(10)  # 데이터 다운로드 시간 대기

download_folder = "C:\\Users\\ray\\Downloads"
list_of_files = glob.glob(os.path.join(download_folder,'*'))
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

save_folder = "D:\\pystock\\data\\KRX"
to_path = os.path.join(save_folder,'20201125.csv')
shutil.move(latest_file,to_path)

import pandas as pd

def get_search_datestring(timestamp):
    timestring = str(timestamp) # pd.date_range() 리스트의 값들을 문자열로 변환
    date = timestring[:-9] # 년도-월-일  문자열 추출
    date_for_input = date.replace("-","") # 2020-01-01 → 20200101
    return date_for_input

start = '2020-01-01'
end = '2020-11-25'
date_stamp_list = pd.date_range(start=start, end=end, freq='B')
dateList = list(map(get_search_datestring, date_stamp_list))
print(dateList)

