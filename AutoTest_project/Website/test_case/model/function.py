from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    base_dir=os.path.dirname(func_path)
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')

    base=base_dir.split('/Website')[0]
    print(base)
    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = '@163.com'
    password = ''

    sender = '@163.com'
    receives = ['', '@qq.com']

    subject = '自动化测试报告'
    # content = '<html><h1 style="color:red">我要自学网，自学成才！</h1></html>'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("开始发送邮件……")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("邮件发送完成!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("最后一个报告是 " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file

if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver,'baidu.png')
    driver.quit()