滚动条控制操作
==
##### 案例：
打开我要自学网页面，然后将滚动条拖到最底部，然后再拖到顶部
```python
from  selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.51zxw.net/")
sleep(2)

#将滚动调拖到最底部
js="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(2)

#将滚动条拖到最顶部
js="var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(3)

driver.quit()
```
