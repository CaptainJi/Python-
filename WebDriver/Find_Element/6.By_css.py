from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
#根据id来定位
driver.find_element_by_css_selector('#kw').send_keys("Selenium 我要自学网")

#根据class定位
driver.find_element_by_css_selector('.s_ipt').send_keys('python')

#通过属性来定位
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("selenium")

sleep(2)
driver.find_element_by_id('su').click()

driver.get("http://www.51zxw.net")

#通过元素层级来定位
driver.find_element_by_css_selector("form#loginForm>ul>input").send_keys("51zxw")

sleep(2)
driver.quit()
