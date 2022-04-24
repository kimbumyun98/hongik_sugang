import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time

my_id = 'B789008'
my_pw = 'zmfrqd$0614'

#url 지정
url="https://sugang.hongik.ac.kr/cn1000.jsp"

#드라이버 로드
driver = webdriver.Chrome('C:/Users/KimBumYun/Desktop/Github/hongik_sugang/chromedriver.exe')
driver.get(url)

id_box = driver.find_element_by_name('p_userid')
pw_box = driver.find_element_by_name('p_passwd')
login_button = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td/input')

id_box.send_keys(my_id)
#time.sleep(1)
pw_box.send_keys(my_pw)
#time.sleep(1)
login_button.click()
#time.sleep(5)

logout_button = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/div/input')

logout_button.click()

time.sleep(5)

driver.close()