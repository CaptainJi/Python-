

Webdriver概述
==
Webdriver (Selenium2）是一种用于Web应用程序的自动测试工具它提供了一套友好的API，与Selenium 1（Selenium-RC）相比，Webdriver 的API更容易理解和使用，其可读性和可维护性也大大提高。Webdriver完全就是一套类库，不依赖于任何测试框架，除了必要的浏览器驱动，不需要启动其他进程或安装其他程序，也不必像Selenium 1那样需要先启动服务。<br>
## 支持浏览器
•	Firefox （FirefoxDriver）<br>
•	IE（InternetExplorerDriver）<br>
•	Opera（OperaDriver）<br>
•	Chrome （ChromeDriver）<br>
•	safari（SafariDriver）<br>
## 支持语言
•	Java<br>
•	C#<br>
•	PHP<br>
•	Python<br>
•	Perl<br>
•	Ruby<br>
## 安装，卸载、查看
安装：pip install selenium==XXXX<br>
卸载 pip uninstall selenium<br>
查看版本号：
pip show selenium<br>
或使用pychram内的pip安装<br>
## 多浏览器运行
### 启动Firefox
•	1.FireFox 48以上版本<br>
•	Selenium 3.X +FireFox驱动——geckodriver<br>
•	2.Firefox 48 以下版本<br>
•	Selenium2.X 内置驱动<br>
•	驱动下载地址[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)<br>
### 启动IE浏览器
•	IE 9以上版本<br>
•	Selenium3.X +IE驱动<br>
•	IE 9以下版本<br>
•	Selenium 2.X +IE驱动<br>
### 启动Chrome浏览器
selenium2.x/3.x +Chrome驱动<br>
**注意**<br>
各个驱动下载地址： [http://www.seleniumhq.org/download/](http://www.seleniumhq.org/download/)<br>
浏览器位数的版本和驱动版本要一致！<br> 如果是32bit浏览器而Driver是64bit则会导致脚本运行失败！<br>



## 第一个自动化测试脚本

##### 案例：<br>
•	启动Chrome浏览器，<br>
•	首先打开百度页面，打印网页标题，等待3秒<br>
•	打开qq首页，打印网页标题，再等待2秒<br>
•	关闭浏览器。<br>


```Python
from selenium import webdriver
from time import sleep

#加载浏览器驱动:注意浏览器名称首字母大写
driver=webdriver.Chrome()

#打开百度首页
driver.get("http://www.baidu.com")
#打印网页title
print(driver.title)
sleep(3)

#打开百度首页
driver.get("http://www.qq.com")
print(driver.title)
sleep(3)

#关闭浏览器
driver.quit()
```
