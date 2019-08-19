鼠标与键盘操作
==
---
## 鼠标操作
实现思路<br>
•	需要引入ActionChains类<br>
•	然后定位相关元素<br>
•	在ActionChains().调用相关鼠标操作方法<br>

```Python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_css_selector("#kw").send_keys("Python")

# 获取搜索框元素对象
element=driver.find_element_by_css_selector("#kw")

sleep(3)
#双击操作
ActionChains(driver).double_click(element).perform()

sleep(2)

#右击操作
ActionChains(driver).context_click(element).perform()

sleep(3)

#鼠标悬停
above=driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(above).perform()

sleep(4)
driver.quit()
```



## 键盘操作
##### 案例：
在百度搜索关键词“Python” 然后将关键词复制或剪切到搜狗搜索框进行搜索<br>
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("Python")

sleep(2)
#键盘全选操作 Ctrl+A
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')

#键盘选择复制或剪切操作 Ctrl+C
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'x')

#打开搜狗页面
driver.get("http://www.sogou.com/")
sleep(2)

#粘贴复制内容
driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL,'v')
sleep(2)

#点击搜索按钮
# driver.find_element_by_xpath("//input[@id='stb']").click()
driver.find_element_by_css_selector("#stb").click()

sleep(3)
driver.quit()
```
