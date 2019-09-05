from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)

driver.implicitly_wait(5)

try:
    start_time=ctime()
    driver.find_element_by_css_selector('#kw').send_keys('Python')
    driver.find_element_by_css_selector('#su').click()
except NoSuchElementException as msg:
    print(msg)
finally:
    end_time=ctime()


sleep(3)
driver.quit()