from LoginPage import *
from selenium import webdriver

driver=webdriver.Chrome()

username='test'
password='123456'

test_user_login(driver,username,password)
sleep(3)
driver.quit()

driver.find_element