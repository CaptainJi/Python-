from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://www.51zxw.net")
sleep(2)

# 根据option标签来定位
driver.find_elements_by_tag_name('option')[1].click()
driver.find_element_by_css_selector("[value='2']").click()

sleep(2)
driver.quit()