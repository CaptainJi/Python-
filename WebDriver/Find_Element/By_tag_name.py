from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('fender美精贝斯')
driver.find_element_by_id('su').click()
sleep(2)
driver.close()