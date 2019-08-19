SeleniumIDE
### 浏览器
•	Chrome<br>
•	安装完成后设置菜单栏<br>
•	关闭浏览器自动更新<br>

### Selenium IDE简介
Selenium IDE是一款浏览器插件，用于记录和播放用户与浏览器的交互。使用它来创建简单的脚本或协助进行探索性测试。
### Selenium IDE安装
•	1.官网下载插件后本地安装 http://www.seleniumhq.org/download/<br>
•	2.浏览器搜索插件安装<br>
### Selenium打开运行
•	工具栏——>Selenium IDE<br>
•	直接点击菜单栏Selenium 图标<br>
### Selenium IDE 自动化实战
#### 任务1：
•	自动在百度搜索“我要自学网” 然后在搜索结果页面点击进入自学网主页
#### 任务2
##### 实现自学网自动登录个人账号
•	Test2017<br>
•	123456test<br>
##### 步骤
1.	输入测试 Base URL<br>
2.	打开录制按钮<br>
3.	在浏览器界面进行相关操作<br>
4.	回放录制的操作（注意：回放时浏览器一定要处于打开状态）<br>
5.	保存测试脚本<br>
导入已保存的脚本
文件——> Open——> 选择要导入的脚本
### Selenium IDE脚本编辑与操作
##### 1. 编辑一行命令<br>
在Table标签下选中某一行命令，命令由command、Target、value三部分组成。可以对这三部分内容那进行编辑。
##### 2. 插入命令。<br>
在某一条命令上右击，选择“insert new command”命令，就可以插入一个空白，然后对空白行进程编辑。<br>
##### 3. 插入注释<br>
鼠标右击选择“insert new comment”命令插入注解空白行，本行内容不被执行，可以帮助我们更好的理解脚本，插入的内容以紫色字体显示。<br>
##### 4. 移动命令或注解<br>
有时我们需要移动某行命令的顺序，我们只需要左击鼠标拖动到相应的位置即可。<br>
##### 5.删除命令<br>
选择单个或多个命令，然后点击鼠标右键选择“Delete”<br>
##### 6.命令执行<br>
选定要执行的命令点击单个执行按钮即可，注意：有一些命令必须依赖于前面命令的运行结果才能成功执行，否则会导致执行失败。<br>

### Selenium IDE常用命令

##### open(url)命令
（1）作用：打开指定的URL，URL可以为相对或是绝对URL；<br>
（2）Target：要打开的URL；value值为空<br>
•	当Target为空，将打开Base URL中填写的页面；<br>
•	当Target不为空且值为相对路径，将打开Base URL + Target页面。如，假设Base URL为http://www.51zxw.net，而Target为/list.aspx?cid=451，则执行open命令时，将打开http://www.51zxw.net/list.aspx?cid=451<br>
•	当Target以http://开头时，将忽略Base URL，直接打开Target的网址；<br>
##### pause(waitTime)<br>
（1）作用：暂停脚本运行<br>
（2）waitTime：等待时间，单位为ms；<br>
##### goBack()
（1）作用：模拟单击浏览器的后退按钮； （2）由于没有参数，所以Target和Value可不填；<br>
##### refresh()
（1）作用：刷新当前页；<br>
（2）由于没有参数，所以Target和Value可不填；<br>
##### windowMaximize()
（1）作用：将当前的窗口最大化，即设置为全屏显示；<br> （2）由于没有参数，所以Target和Value可不填；<br>
##### click（locator）
（1）作用：单击一个链接、按钮、复选框或单选按钮；<br>
（2）如果该单击事件导致新的页面加载，命令将会加上后缀“AndWait”，即“clickAnd Wait”，或“waitForPageToLoad”命令<br>；
##### type(locator,value)
（1）作用：向指定输入域中输入指定值；也可为下拉框、复选框和单选框按钮赋值<br>
（2）Target：元素的定位表达式；<br>
（3）Value：要输入的值；<br>
##### select(selectLocator,optionLocator)
（1）作用：模拟人工单击下拉列表框；<br>
selectLocator：指向指定选择元素的元素定位器；<br>
optionLocator：选项的选择器（默认为标签）；<br>
（2）选项的选择方式两种 label 和Value<br>
•	label=文本值，基于选项的文本进行匹配（默认方式），如label=three；<br>
•	value=真实值，基于选项的真实值进行匹配，如value=3；<br>
##### close()
（1）作用：模拟用户单击窗口上的关闭按钮；<br>
（2）由于没有参数，所以Target和Value可不填；<br>
### 断言与验证
#### 断言
验证应用程序的状态是否同所期望的一致。 常见的断言包括:验证页面内容，如标题是否为X或当前位置是否正确等等。<br>
断言被用于4种模式+5种手段:<br>
##### Assert
Assert 断言失败时，该测试将终止。<br>
##### verify
Verify 断言失败时，该测试将继续执行，并将错误记入日显示屏。也就是说允许此单个验证通过。确保应用程序在正确的页面上。提高脚本的伸缩性。<br>
##### waitfor
Waitfor用于等待某些条件变为真。可用于AJAX应用程序的测试。 如果该条件为真，他们将立即成功执行。如果该条件不为真，则将失败并暂停测试。直到超过当前所设定的超时时间。 一般跟setTimeout时间一起用<br>
##### store
store 定义变量，可以获取页面的相关元素进行判断。<br>
5种手段：<br>
•	Title 获取页面的标题<br>
•	Value 获取元素的值<br>
•	Text 获取元素文本信息<br>
•	Table 获得元素标签<br>
•	ElementPresnt 获得当前元素。<br>
##### 断言常用的有：<br>
assertTitle（检查当前页面的title是否正确）<br>
assertValue（检查输入框的值， 单选或复选框的值）<br>
VerifyValue() 验证元素的值。<br>
##### 断言设置方法
1.浏览器页面点击鼠标右键->Show All Available commands->选择具体的断言方式，脚本回自动加载选定的断言命令<br>
2.直接在脚本页面编辑<br>
