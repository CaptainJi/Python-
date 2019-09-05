元素定位
==
元素的定位应该是自动化测试的核心，要想操作一个元素，首先应该识别这个元素。<br>
webdriver提供了一系列的元素定位方法，常用的有以下几种<br>
•	id<br>
•	name<br>
•	class name<br>
•	link text<br>
•	partial link text<br>
•	tag name<br>
•	xpath<br>
•	css selector<br>

##### 案例：<br>
打开百度首页，在搜索框自动输入“Webdriver”关键词，然后点击搜索按钮，查看搜索页面。<br>

## id与name 定位
```Python
from  selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")


driver.find_element_by_id("kw").send_keys("Webdriver")
driver.find_element_by_name("wd").send_keys("Webdriver")

sleep(2)
driver.find_element_by_id("su").click()
```



## tag_name定位
打开我要自学网页面，在用户名输入框输入用户名“selenium”<br>

```Python
from  selenium import webdriver
from  time import sleep

driver=webdriver.Chrome()

driver.get("http://www.51zxw.com")

#定位标签名为input的元素
driver.find_element_by_tag_name("input").send_keys("selenium")

#获取页面所有标签名称为“input”的标签。
driver.find_elements_by_tag_name("input")[0].send_keys("selenium")

sleep(3)

driver.quit()
```


## class_name定位
根据标签中属性class来进行定位的一种方法<br>

```python
from  selenium import webdriver
from  time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.find_element_by_class_name("s_ipt").send_keys("Selenium 我要自学网")
sleep(2)

driver.find_element_by_id("su").click()
sleep(3)

driver.quit()
```
## link_text定位
link_text定位就是根据超链接文字进行定位。<br>

```python
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.51zxw.net/")

driver.find_element_by_link_text('程序开发').click()
sleep(3)
driver.find_element_by_partial_link_text('神秘面纱').click()
```
## XPath定位
XPath即为XML路径语言，它是一种用来确定XML文档中某部分位置的语言。XPath基于XML的树状结构，提供在数据结构树中找寻节点的能力。<br>
### 1.xpath绝对与相对定位<br>
```python
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")

# 绝对路径定位
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("51zxw")

# 利用元素熟悉定位--定位到input标签中为kw的元素
driver.find_element_by_xpath("//input[@id='kw']").send_keys("Selenium")

# 定位input标签中name属性为wd的元素
driver.find_element_by_xpath("//input[@name='wd']").send_keys("Selenium")

# 定位所有标签元素中，class属性为s_ipt的元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("Python3")

driver.find_element_by_id('su').click()

sleep(3)
driver.quit()
```
### 2.Xpath层级与逻辑定位
```Python
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.51zxw.net/")
#层级和属性结合定位--自学网首页输入用户和名密码
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys("51zxw")
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys("66666")

#逻辑运算组合定位
driver.find_element_by_xpath("//input[@class='loinp' and @name='username']").send_keys("51zxw")

sleep(3)
driver.quit()
```

## Css定位
Selenium极力推荐使用CSS 定位，而不是XPath来定位元素，原因是CSS 定位比XPath 定速度快，语法也更加简洁。 <br>
##### CSS常用定位方法
1.	find_element_by_css_selector（）<br>
2.	#id id选择器根据id属性来定位元素<br>
3.	.class  class选择器，根据class属性值来定位元素<br>
4.	[attribute='value'] 根据属性来定位元素<br>
5.	element>element 根据元素层级来定位 父元素>子元素<br>

```python
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
#根据id来定位
driver.find_element_by_css_selector('#kw').send_keys("Selenium 我要自学网")

#根据class定位
driver.find_element_by_css_selector('.s_ipt').send_keys('python')

#通过属性来定位
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("selenium")

sleep(2)
driver.find_element_by_id('su').click()

driver.get("http://www.51zxw.net")

#通过元素层级来定位
driver.find_element_by_css_selector("form#loginForm>ul>input").send_keys("51zxw")

sleep(2)
driver.quit()
```
## 下拉菜单元素定位
##### 案例：
在我要自学网登录页面选择指定的保留时间。<br>
### 1.根据选项元素标签定位
```python
from selenium import webdriver
from  time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("http://www.51zxw.net")
sleep(2)

#根据option标签来定位
driver.find_elements_by_tag_name('option')[1].click()
driver.find_element_by_css_selector("[value='2']").click()

sleep(2)
driver.quit()
```

### 2.使用Select类定位
```Python
from selenium import webdriver
from  time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("http://www.51zxw.net")
sleep(2)
#利用Select类来进行定位
select = Select(driver.find_element_by_css_selector("[name='CookieDate']"))

select.select_by_index(2)
select.select_by_visible_text("留一年")
select.select_by_value("1")

sleep(2)
driver.quit()
```
Select只对<select>标签的下拉菜单有效；我要自学网页面改版，已无法测试
### 3.定位非<select>标签的下拉菜单

定位非<select>标签的下拉菜单中的选项，需要两个步骤，先定位到下拉菜单，再对其中的选项进行定位。
```python
# 先定位到下拉菜单
ul = driver.find_element_by_css_selector("div#select2_container > ul")
# 再对下拉菜单中的选项进行选择
ul.find_element_by_id("li2_input_2").click()
```
### 4.定位输入检索式选择框
定位这种类型的选择框分三个步骤，先定位输入框输入关键字，然后定位检索出来的选择列表框，最后定位相应的值。
```python
# 先定位输入框输入关键字
driver.find_element_by_id('id').send_keys('ab')
# 然后定位ul
ul = driver.find_element_by_css_selector(".ui-autocomplete-items")
# 最后定位里面所有值
li = ul.find_elements_by_tag_name('li')
# 选取想要的值
li[0].click() # 0代表选择第一个值
```


## frame嵌套页面元素定位

##### 案例：
在Frame.html文件种定位搜狗搜索页面，进行搜索操作。<br>
```Python
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
#设置网页文件路径，r代表路径转义
file_path=r'E:\Python_script\Webdriver\Frame.html'
#路径转义另一种写法
# file_path='E:\\Python_script\\Webdriver\\Frame.html'
driver.get(file_path)

#切换到frame页面内
driver.switch_to.frame("search")

#定位到搜索框按钮输入关键词
driver.find_element_by_css_selector("#query").send_keys("Python")
sleep(3)

driver.find_element_by_css_selector("#stb").click()

sleep(3)
driver.quit()
```
## 元素等待

### 概念
•	显式等待是针对某一个元素进行相关等待判定；<br>
•	隐式等待不针对某一个元素进行等待;全局元素等待。<br>
### 相关模块
•	WebDriverWait 显示等待针对元素必用<br>
•	expected_conditions 预期条件类（里面包含方法可以调用，用于显示等待）<br>
•	NoSuchElementException 用于隐式等待抛出异常<br>
•	By 用于元素定位<br>

```Python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait		#注意字母大写
from selenium.webdriver.support import expected_conditions as EC #as：为调用方便将expected_conditions重命名为EC
from selenium.common.exceptions import NoSuchElementException
```

### 显式等待
##### 案例：
检测百度页面搜索按钮是否存在，存在就输入关键词“自学网 Selenium” 然后点击搜索<br>
```python
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

### 隐式等待
```python
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
