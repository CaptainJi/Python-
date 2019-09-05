from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

cookie=driver.get_cookies()
print(cookie)

driver.add_cookie({'name':'captain','value':'www.baidu.com'})
for cookie in driver.get_cookies():

    print('%s--%s'%(cookie['name'],cookie['value']))

driver.quit()