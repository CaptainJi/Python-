import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

smtpserver='smtp.163.com'

user=''
password=''

sender=''
receive=''

now=time.strftime('%Y-%m-%d %H:%M:%S')
suject='测试报告'+now
content='<html><h1 style="color:red">测试报告</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(suject,'utf-8')
msg['From']=''
msg['To']=''

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print('开始发送邮件……')
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print('发送完成！')