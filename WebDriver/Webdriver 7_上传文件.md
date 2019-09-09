上传文件
==
##### 案例：
在百度搜索上传本地图片进行搜索。
```python
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_css_selector(".soutu-btn").click()
sleep(3)
#上传文件（图片）操作
driver.find_element_by_css_selector(".upload-pic").send_keys(r"E:\Python_script\Webdriver\shuiyin.png")

sleep(3)
# driver.quit()
```
