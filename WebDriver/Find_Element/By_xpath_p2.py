from selenium import  webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.51zxw.net')
driver.find_element_by_xpath('//*[@id="middle"]/table[3]/tbody/tr/td[1]/div/ul/li[2]/a/div[1]/img').click()

