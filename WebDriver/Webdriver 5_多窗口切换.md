## 多窗口切换操作
使用webdriver中的current_window_handle获取窗口句柄<br>
使用switch_to.window切换窗口
##### 案例：
打开百度主页，然后打开网站报备页面，再回到百度页面

```python
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
```
