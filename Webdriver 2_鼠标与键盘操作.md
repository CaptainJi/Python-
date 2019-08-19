## 鼠标操作
实现思路<br>
•	需要引入ActionChains类<br>
•	然后定位相关元素<br>
•	在ActionChains().调用相关鼠标操作方法<br>

```
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

```
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
## 元素等待

### 概念
•	显示等待是针对某一个元素进行相关等待判定；<br>
•	隐式等待不针对某一个元素进行等待;全局元素等待。<br>
### 相关模块
•	WebDriverWait 显示等待针对元素必用<br>
•	expected_conditions 预期条件类（里面包含方法可以调用，用于显示等待）<br>
•	NoSuchElementException 用于隐式等待抛出异常<br>
•	By 用于元素定位<br>

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait		    #注意字母大写
from selenium.webdriver.support import expected_conditions as EC 	
from selenium.common.exceptions import NoSuchElementException
```
#### 显示等待
##### 案例：
检测百度页面搜索按钮是否存在，存在就输入关键词“自学网 Selenium” 然后点击搜索<br>
```
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")


driver.find_element_by_css_selector("#kw").send_keys("自学网 Selenium")

sleep(2)

#显示等待--判断搜索按钮是否存在
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"su")))
element.click()
sleep(3)

driver.quit()
```

#### 隐式等待

```
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

sleep(2)

driver.implicitly_wait(5) #隐式等待时间设定 5秒

#检测搜索框是否存在
try:
	print(ctime())
	driver.find_element_by_css_selector("#kw").send_keys("Python")
	driver. find_element_by_css_selector("#su").click
except NoSuchElementException as msg:
	print(msg)
finally:
	print(ctime())

sleep(3)
driver.quit()
```

