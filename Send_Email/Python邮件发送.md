Python邮件发送
==
## SMTP（Simple Mail Transfer Protocol）

即简单邮件传输协议。它是一组用于从源地址到目的地址传输邮件的规范，通过它来控制邮件的中转方式。SMTP 协议属于TCP/IP协议簇，它帮助每台计算机在发送或中转信件时找到下一个目的地。SMTP 服务器就是遵循 SMTP 协议的发送邮件服务器。

### SMTP 认证

- SMTP 认证，简单地说就是要求必须在提供了账户名和密码之后才可以登录 SMTP 服务器，这就使得那些垃圾邮件的散播者无可乘之机。
- 增加 SMTP 认证的目的是为了使用户避免受到垃圾邮件的侵扰。

**更多资料：** http://help.163.com/09/1223/14/5R7P6CJ600753VB8.html<br>

### smtplib模块
Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。<br><br>
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。<br>
**注意：**使用前需要开启SMTP服务<br>

##### 案例：
使用163邮箱来结合smtp模块发送邮件 准备工作：
```py
import smtplib                           #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.header import Header         #定义邮件标题

#发送邮箱服务器
smtpserver='smtp.163.com'

#发送邮箱用户名密码
user='yuexiaolu2015@163.com'
password='…'

#发送和接收邮箱
sender='yuexiaolu2015@163.com'
receive='yuexiaolu2015@126.com'

#发送邮件主题和内容
subject='Web Selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才!</h1></html>'

#HTML邮件正文
msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='yuexiaolu2015@163.com'
msg['To'] = 'yuexiaolu2015@126.com'

#SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)

#HELO 向服务器标识用户身份
smtp.helo(smtpserver)
#服务器返回结果确认
smtp.ehlo(smtpserver)
#登录邮箱服务器用户名和密码
smtp.login(user,password)

print("开始发送邮件...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("邮件发送完成！")
```
## 发送带附件的邮件
##### 案例：
发送E:\Python_script\目录下 logo.png图片文件到指定的邮箱
```py
import smtplib                           #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.mime.multipart import MIMEMultipart  #用于传送附件

#发送邮箱服务器
smtpserver='smtp.163.com'

#发送邮箱用户名密码
user='yuexiaolu2015@163.com'
password='070337shu'

#发送和接收邮箱
sender='yuexiaolu2015@163.com'
receives=['yuexiaolu2015@126.com','yuexiaolu2015@sina.com']


#发送邮件主题和内容
subject='Web Selenium 附件发送测试'
content='<html><h1 style="color:red">我要自学网，自学成才!</h1></html>'


#构造附件内容
send_file=open(r"E:\Python_script\logo.png",'rb').read()

att=MIMEText(send_file,'base64','utf-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment;filename="logo.png"'

#构建发送与接收信息
msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
msgRoot['subject']=subject
msgRoot['From']=sender
msgRoot['To'] = ','.join(receives)
msgRoot.attach(att)


#SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)

#HELO 向服务器标识用户身份
smtp.helo(smtpserver)
#服务器返回结果确认
smtp.ehlo(smtpserver)
#登录邮箱服务器用户名和密码
smtp.login(user,password)

print("Start send email...")

smtp.sendmail(sender,receives,msgRoot.as_string())

smtp.quit()
print("Send End！")
```
## 整合测试报告发送
##### 案例：
获取…\Test_Baidu\test_report目录下最新的测试报告
```py
import os #用于访问操作系统功能的模块

#报告存放位置
report_dir='./test_report'

#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
lists=os.listdir(report_dir)

#按时间顺序对该目录文件夹下面的文件进行排序
lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
print(lists)
print("latest report is :"+lists[-1])

#输出最新报告的路径
file=os.path.join(report_dir,lists[-1])
print(file)
```
Python os模块相关知识： http://www.cnblogs.com/MnCu8261/p/5483657.html<br>
lambda 介绍 http://www.cnblogs.com/evening/archive/2012/03/29/2423554.html<br>
## 发送测试报告
##### 案例：
将E:\Python_script\unittest\Test_Baidu生成的最新测试报告发送到指定邮箱。

```py
import unittest
from BSTestRunner import BSTestRunner
import time
import smtplib                           #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.header import Header         #定义邮件标题
import os

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver='smtp.163.com'
    # 发送邮箱用户名密码
    user = 'yuexiaolu2015@163.com'
    password = '…'

    # 发送和接收邮箱
    sender = 'yuexiaolu2015@163.com'
    receives = ['yuexiaolu2015@126.com', 'yuexiaolu2015@sina.com']

    # 发送邮件主题和内容
    subject = 'Web Selenium 自动化测试报告'

    # HTML邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send Email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send Email end!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(("new report is :" + lists[-1]))

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    test_dir='./test_case'
    report_dir='./test_report'


    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + 'result.html'

    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title="Test Report", description="baidu search")
        runner.run(discover)
    f.close()

    #h获取最新测试报告
    latest_report=latest_report(report_dir)
    #发送邮件报告
    send_mail(latest_report)
```

**163邮箱发生失败的常见问题**<br>
http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html
