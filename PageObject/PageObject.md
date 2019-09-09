Page Object
==
Page Object是Selenium自动化测试项目开发实践的最佳设计模式之一，通过对界面元素和功能模块的封装减少冗余代码，同时在后期维护中，若元素定位或功能模块发生变化，只需要调整页面元素或功能模块封装的代码，提高测试用例的可维护性。<br>
**BasePage.py**
```py
from  time import sleep

class Page():
    '''页面基础类'''

    #初始化
    def __init__(self, dirver):
        self.base_url = 'http://localhost'
        self.driver = dirver
        self.timeout = 10

    #打开不同的子页面
    def _open(self, url):
        url_ = self.base_url + url
        print("Test page is： %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, 'Did ont land on %s' % url_

    def open(self):
        self._open(self.url)

    #元素定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
```


**LoginPage.py**
```py
from BasePage import *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    '''首页登录页面'''

    url='/'

    #定位器
    username_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    submit_loc=(By.NAME,'Submit')

    #用户名输入框元素
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    #密码输入框元素
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

#登录功能模块封装
def test_user_login(driver,username,password):
    '''测试用户名密码是否可以登录'''

    login_page=LoginPage(driver)
    login_page.open()

    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()
```


**loin_test.py**
```py
from LoginPage import *
from selenium import webdriver

driver=webdriver.Chrome()

username = 'test'
password = '123456'
test_user_login(driver, username, password)

sleep(3)
driver.quit()
```










**参考文档：**
http://www.liaoxuefeng.com/ <br>
http://blog.csdn.net/menglei8625/article/details/7721746  <br>
http://blog.csdn.net/bravezhe/article/details/7659198  <br>
http://blog.csdn.net/spritzdance/article/details/5362220  <br>
