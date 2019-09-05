from LoginClass import *
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://localhost')
driver.implicitly_wait(10)

Login().user_login(driver)
sleep(3)
Login().user_logout(driver)
sleep(3)
driver.quit()