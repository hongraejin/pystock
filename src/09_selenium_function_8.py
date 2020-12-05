from selenium import webdriver
import time

path = "D:\\chromedriver.exe"
driver = webdriver.Chrome(path)
time.sleep(1) # 로딩시간 대기

URL = "https://python.org"
driver.get(URL)

# 검색창에 "pandas" 입력
time.sleep(3)
input_element = driver.find_element_by_css_selector('form.search-the-site>fieldset>input.search-field')
input_element.clear()
input_element.send_keys('pandas')

# 모든 버튼 찾기
time.sleep(3)
button_elements = driver.find_elements_by_css_selector("button")

# 모든 버튼 테그의 입력값 text로 추출하기
for button in button_elements:
    text_in_button = button.text
    # 버튼 안의 Text 가 "GO" 이면 click()
    if text_in_button =="GO":
        button.click()
