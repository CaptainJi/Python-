from selenium import webdriver
from time import *

driver=webdriver.Chrome()
driver.get('http://www.51zxw.net')
sleep(2)
#定义JavaScript变量“document.documentElement.scrollTop=10000”意为纵向滚筒条距离顶部10000，也就是拉动到底部
js='var action=document.documentElement.scrollTop=10000'
#调用JavaScript变量
driver.execute_script(js)
sleep(2)
#回到顶部
js='var action=document.documentElement.scrollTop=0'
driver.execute_script(js)
sleep(2)
#“document.documentElement.scrollLeft=10000”意为横向滚动条距离左侧10000
js='var action=document.documentElement.scrollLeft=10000'
driver.execute_script(js)
sleep(2)
#回到左侧
js='var action=document.documentElement.scrollLeft=0'
driver.execute_script(js)

sleep(2)
driver.quit()
