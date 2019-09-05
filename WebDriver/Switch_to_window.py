from selenium import webdriver
from time import sleep
#打开百度主页
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
#获取网页窗口句柄
window_handle=driver.current_window_handle
sleep(2)
#点击网页报备
driver.find_element_by_css_selector('#jgwab').click()
sleep(2)
#回到百度主页窗口
driver.switch_to.window(window_handle)
sleep(2)
driver.quit()