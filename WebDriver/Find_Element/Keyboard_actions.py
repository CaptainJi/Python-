from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

drive=webdriver.Chrome()
drive.get('http://www.baidu.com')
drive.find_element_by_css_selector('#kw').send_keys('Python')
sleep(1)
#键盘操作
#全选
drive.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
sleep(0.5)
#复制或剪切
# drive.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
drive.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'x')
sleep(0.5)

drive.get('http://www.sogou.com')
#粘贴
drive.find_element_by_css_selector('.sec-input').send_keys(Keys.CONTROL,'v')
sleep(2)
drive.find_element_by_css_selector('#stb').click()
sleep(4)
drive.close()

