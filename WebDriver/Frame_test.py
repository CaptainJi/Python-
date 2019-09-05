from selenium import webdriver
from time import sleep
import os #获取路径模块

#os.path.abspath 表示获得文件当前路径;当前文件指当前编写的源文件
#os.path.dirname 表示获得文件的上一级目录，使用方法：os.path.dirname(os.path.abspath('.'))



dir=os.path.abspath('.')#获取当前文件的绝对路径
file_path=dir+r'\Frame.html'#需要调用的文件路径=父路径+文件名或子路径名

driver=webdriver.Chrome()
driver.get(file_path)

driver.switch_to.frame('search')#跳转frame嵌套

driver.find_element_by_css_selector('#query').send_keys('Webdriver')
sleep(2)
driver.find_element_by_css_selector('#stb').click()
sleep(2)
driver.quit()


