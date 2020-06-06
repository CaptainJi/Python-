安通风表在线状态监控
====
### 说明
监控风表在线状态，当出现掉线风表时发送邮件提醒到特定邮箱<br>
软件使用Selenium操作浏览器进行登录操作后使用bs4分析数据，发现特定数据后发送报警邮件给指定邮箱。
### 如何使用
软件依赖Chrome 81版浏览器，使用前需先安装81版Chrome；文件夹中已提供该版本离线安装包。<br>
使用Python 3.7 + pyinstaller 3.6 编译成功，开始使用Python3.8 + pyinstaller 3.6进行编译后，本机可运行，到其他没有环境的机器上运行不了，<br>
查看各种文档尝试各种方法也解决不了。查看pyinstaller官方文档发现只支持到3.7，最新3.8还未支持。最后还是换回了Python3.7才成功。

### 文件夹说明
- config:日志配置文件
- data：监控资源文件
- driver:chromedriver驱动
- log：日志文件
- reports:监控报告
- screenshots：截图文件
- warning：掉线报警文件