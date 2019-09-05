from selenium import webdriver
from time import *
import os

driver=webdriver.Chrome()
driver.get('http://www.qq.com')
dir=os.path.abspath('.')
#截图到源文件目录下
driver.get_screenshot_as_file(dir+r'\Screenshot.jpg')
sleep(2)
driver.get('http://www.baidu.com')
driver.get_screenshot_as_file(dir+r'\Screenshot.png')
sleep(1)
driver.quit()