from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
#打开网站
driver.get('http://www.qq.com')
#最大化窗口
# driver.maximize_window()
#找到css元素“搜索框”，并输入
driver.find_element_by_css_selector('#sougouTxt').send_keys('fender美精贝斯')
sleep(1)
#鼠标悬停:鼠标操作记得加上perform()函数执行操作
# above=driver.find_element_by_css_selector('#searchSelected')
ActionChains(driver).move_to_element(driver.find_element_by_css_selector('#searchSelected')).perform()
sleep(1)
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="searchTab"]/ul[2]/li[2]')).click().perform()
sleep(1)
driver.find_element_by_css_selector('#searchBtn').click()
sleep(1)
# driver.back()
# sleep(1)
# driver.forward()
# sleep(1)
driver.close()