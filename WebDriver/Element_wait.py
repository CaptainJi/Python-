from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(1)

driver.find_element_by_css_selector('#kw').send_keys('Selenium学习')

element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
sleep(2)
element.click()
sleep(3)
driver.quit()
