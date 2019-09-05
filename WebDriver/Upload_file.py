from selenium import webdriver
from time import sleep
import os

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(1)
driver.find_element_by_css_selector('#form > span.bg.s_ipt_wr.quickdelete-wrap > span').click()
sleep(1)
dir=os.path.abspath('.')
pic_path=dir+r'\test.jpg'
sleep(2)
driver.find_element_by_css_selector('#form > div > div.soutu-state-normal > div.upload-wrap > input').send_keys(pic_path)
sleep(10)

