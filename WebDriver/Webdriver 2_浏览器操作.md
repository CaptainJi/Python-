浏览器操作
===
##### 案例：
•	浏览器窗口大小设置<br>
•	页面前进后退<br>
•	页面刷新<br>

```Python
from  selenium import webdriver
from time import  sleep

driver=webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")
#最大化网页窗口
driver.maximize_window()
sleep(2)

driver.get("http://www.qq.com")
driver.set_window_size(400,800)
driver.refresh()
sleep(2)
#后退
driver.back()
sleep(2)
#前进
driver.forward()

sleep(2)
driver.quit()
```
