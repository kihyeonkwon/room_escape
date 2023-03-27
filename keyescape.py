import datetime
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# 세팅
booking_time = datetime.datetime(2023, 4, 1, 10, 0, 0)
place = '우주라이크'
whendate = '31'
theme = 'US'
whentime = '17:55  '
personNumber = '6 명'
myName = '권기현'
myPhone1 = '3265'
myPhone2 = '6909'

# # calculate the number of seconds until the booking time
# time_delta = booking_time - datetime.datetime.now()
# time.sleep(time_delta.total_seconds())

# 자동종료 해제
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 세팅
browser = webdriver.Chrome(chrome_options=chrome_options)

# navigate to the ticket booking website
browser.get('https://keyescape.co.kr/web/home.php?go=rev.make')


placeBtn = browser.find_element(By.XPATH, f"//*[text()='{place}']")
placeBtn.click()

time.sleep(1)


date = browser.find_element(By.XPATH, f"//*[text()='{whendate}']")
date.click()

time.sleep(1)


themeBtn = browser.find_element(By.XPATH, f"//*[text()='{theme}']")
themeBtn.click()


wait = WebDriverWait(browser, 20)
new_child_element = wait.until(presence_of_element_located(
    (By.XPATH, f"//*[text()='{whentime}']")))
print('found')
new_child_element.click()

time.sleep(1)


# 예약하기 버튼클릭
reserve = browser.find_element(By.CLASS_NAME, "b")
reserve.click()


# 새페이지 대기
wait = WebDriverWait(browser, 10)
new_page_element = wait.until(
    EC.presence_of_element_located((By.NAME, 'name')))

nameInput = browser.find_element(By.NAME, 'name')
mobile2Input = browser.find_element(By.NAME, 'mobile2')
mobile3Input = browser.find_element(By.NAME, 'mobile3')
personInput = browser.find_element(By.NAME, 'person')

nameInput.send_keys(myName)
mobile2Input.send_keys(myPhone1)
mobile3Input.send_keys(myPhone2)
personInput.click()
personNumberBtn = browser.find_element(
    By.XPATH, f"//*[text()='{personNumber}']")
personNumberBtn.click()


# last_name_element.send_keys('Doe')
# email_element.send_keys('johndoe@example.com')

# submit the form
# submit_button_element = browser.find_element_by_id('submit_button_id')
# submit_button_element.click()
# close the browser window
# browser.quit()
