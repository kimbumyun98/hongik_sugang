# 00. 라이브러리
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import urllib
import time
import random
import sys
import re
import os
import pyautogui
from selenium.webdriver.common.alert import Alert

login_id = ''
login_pw = ''

dr = webdriver.Chrome("C:/Users/KimBumYun/Desktop/Github/2023/Instagram_Webcawling/chromedriver.exe")
dr.set_window_size(1280, 1440)
dr.get('https://sugang.hongik.ac.kr/cn1000.jsp')

id_box = dr.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input')
pw_box = dr.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input')
login_button = dr.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td/input')

act = ActionChains(dr)
act.send_keys_to_element(id_box, login_id).send_keys_to_element(pw_box, login_pw).click(login_button).perform()

while True:
    first_box = dr.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table[2]/tbody/tr[1]/td/table/tbody/tr[19]/td/a')
    act.click(first_box).perform()
    second_box = dr.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div[2]/table/tbody/tr/td/form/table/tbody/tr[22]/td/input[2]')
    act.click(second_box).perform()
    da = Alert(dr)
    da.accept()
    db = Alert(dr)
    db.accept()