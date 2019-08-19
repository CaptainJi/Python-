from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.51zxw.net')
driver.find_element_by_link_text('程序开发').click()
sleep(2)
driver.find_element_by_partial_link_text('逻辑思维').click()
sleep(2)
driver.find_element_by_partial_link_text('小学奥数').click()
sleep(2)
driver.close()
