Cookie处理
==
## 什么是Cookie
Cookie是储存在用户本地终端上的数据，实际上是一小段的文本信息。
Cookie作用
帮助 Web 站点保存有关访问者的信息，方便用户的访问。如记住用户名密码实现自动登录。
##### 案例：
查看访问我要自学网时的Cookie内容
```Python
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.51zxw.net/")

#获取cookie全部内容
cookie=driver.get_cookies()
#打印全部cookile信息
print(cookie)
#打印cookie第一组信息
print(cookie[0])

#添加cookie
driver.add_cookie({'name':'51zxw','value':'www.51zxw.net'})
for cookie in driver.get_cookies():
    print("%s --- %s" %(cookie['name'],cookie['value']))

driver.quit()
```
## 自动化测试验证码问题
### 验证码作用
不少网站在用户登录、用户提交信息等登录和输入的页面上使用了验证码技术。验证码技术可以有效防止恶意用户对网站的滥用，使得网站可以有效避免用户信息失窃、保证网站稳定安全性。
但是验证码给自动化测试带来一些不便，使脚本无法正常运行覆盖功能模块。
### 如何解决
#### 1.去掉验证码
这是最简单的方法，对于开发人员来说，只是把验证码的相关代码注释掉即可，如果是在测试环境，这样做可省去了测试人员不少麻烦，如果自动化脚本是要在正式环境跑，这样就给系统带来了一定的风险。
#### 2.设置万能码
去掉验证码的主要是安全问题，为了应对在线系统的安全性威胁，可以在修改程序时不取消验证码，而是程序中留一个“后门”---设置一个“万能验证码”，只要用户输入这个“万能验证码”，程序就认为验证通过，否则按照原先的验证方式进行验证。
#### 3.验证码识别技术（OCR）
例如可以通过Python-tesseract 来识别图片验证码，Python-tesseract是光学字符识别Tesseract OCR引擎的Python封装类。能够读取任何常规的图片文件(JPG, GIF ,PNG , TIFF等)。不过，目前市面上的验证码形式繁多，目前任何一种验证码识别技术，识别率都不是100% 。
#### 4.记录cookie
通过向浏览器中添加cookie 可以绕过登录的验证码。

### 基于Cookie绕过验证码自动登录
##### 案例：
使用Cookie绕过百度验证码自动登录账户。
```python
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.baidu.com/")

#手动添加cookie
driver.add_cookie({'name':'BAIDUID','value':'9E4BF1D44014…(根据实际获取值填写)'})
driver.add_cookie({'name':'BDUSS','value':'根据实际抓包获取值填写'})

sleep(2)
driver.refresh()
sleep(3)
driver.quit()
```







参考文档：
http://www.cnblogs.com/fnng/
