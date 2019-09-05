from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('fender美精贝斯')
sleep(2)
driver.find_element_by_xpath('//*[@id="su"]').click()
sleep(3)
driver.close()